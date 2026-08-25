
import threading
import time
from datetime import datetime

import ccxt
import pandas as pd
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

KV = r"""
<RootWidget>:
    orientation: "vertical"
    padding: dp(12)
    spacing: dp(8)

    Label:
        text: "BTC SMA 9/21 Trading Bot"
        font_size: "22sp"
        bold: True
        size_hint_y: None
        height: dp(42)

    GridLayout:
        cols: 2
        size_hint_y: None
        height: dp(170)
        spacing: dp(6)

        Label:
            text: "Symbol"
        Label:
            text: root.symbol

        Label:
            text: "Price"
        Label:
            text: root.price

        Label:
            text: "SMA 9"
        Label:
            text: root.sma9

        Label:
            text: "SMA 21"
        Label:
            text: root.sma21

        Label:
            text: "Signal"
        Label:
            text: root.signal

        Label:
            text: "Mode"
        Label:
            text: "PAPER TRADING"

    BoxLayout:
        size_hint_y: None
        height: dp(50)
        spacing: dp(8)

        Button:
            text: "START BOT"
            on_release: root.start_bot()

        Button:
            text: "STOP BOT"
            on_release: root.stop_bot()

    Label:
        text: root.status
        text_size: self.width, None
        halign: "left"
        valign: "top"

    Label:
        text: root.log_text
        text_size: self.width, self.height
        halign: "left"
        valign: "top"
"""

Builder.load_string(KV)


class RootWidget(BoxLayout):
    symbol = StringProperty("BTC/USDT")
    price = StringProperty("-")
    sma9 = StringProperty("-")
    sma21 = StringProperty("-")
    signal = StringProperty("WAIT")
    status = StringProperty("Stopped")
    log_text = StringProperty("Paper trading is ON. No real orders will be sent.")

    running = BooleanProperty(False)
    thread = None
    exchange = None
    in_position = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exchange = ccxt.binance({
            "enableRateLimit": True,
            "options": {"defaultType": "spot"},
        })

    def add_log(self, msg):
        def update(_):
            now = datetime.now().strftime("%H:%M:%S")
            self.log_text = f"[{now}] {msg}\n" + self.log_text[:1800]
        Clock.schedule_once(update)

    def start_bot(self):
        if self.running:
            return
        self.running = True
        self.status = "Running..."
        self.add_log("Bot started.")
        self.thread = threading.Thread(target=self.bot_loop, daemon=True)
        self.thread.start()

    def stop_bot(self):
        self.running = False
        self.status = "Stopped"
        self.add_log("Bot stopped.")

    def fetch_data(self):
        bars = self.exchange.fetch_ohlcv(
            self.symbol, "15m", limit=100
        )
        df = pd.DataFrame(
            bars,
            columns=["timestamp", "open", "high", "low", "close", "volume"]
        )
        df["sma9"] = df["close"].rolling(9).mean()
        df["sma21"] = df["close"].rolling(21).mean()
        return df

    def bot_loop(self):
        while self.running:
            try:
                df = self.fetch_data()

                # Use completed candles only.
                prev = df.iloc[-3]
                last = df.iloc[-2]
                current = float(df.iloc[-1]["close"])

                p9 = float(last["sma9"])
                p21 = float(last["sma21"])

                buy = (
                    float(last["sma9"]) > float(last["sma21"])
                    and float(prev["sma9"]) <= float(prev["sma21"])
                )
                sell = (
                    float(last["sma9"]) < float(last["sma21"])
                    and float(prev["sma9"]) >= float(prev["sma21"])
                )

                def update_ui(_):
                    self.price = f"${current:,.2f}"
                    self.sma9 = f"{p9:,.2f}"
                    self.sma21 = f"{p21:,.2f}"
                    self.signal = "BUY" if buy else ("SELL" if sell else "WAIT")
                    self.status = "Running — Paper Trading"
                Clock.schedule_once(update_ui)

                if buy and not self.in_position:
                    self.in_position = True
                    self.add_log(f"BUY SIGNAL @ ${current:,.2f} (paper only)")
                elif sell and self.in_position:
                    self.in_position = False
                    self.add_log(f"SELL SIGNAL @ ${current:,.2f} (paper only)")
                else:
                    self.add_log(
                        f"Price ${current:,.2f} | SMA9 {p9:,.2f} | SMA21 {p21:,.2f}"
                    )

            except Exception as e:
                self.add_log(f"Error: {type(e).__name__}: {e}")

            # Check once per minute, but stop promptly if requested.
            for _ in range(60):
                if not self.running:
                    break
                time.sleep(1)


class TradingApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    TradingApp().run()
