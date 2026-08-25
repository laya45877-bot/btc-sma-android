from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import ccxt
import pandas as pd
import numpy as np
import threading

class TradingBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10

        # Title Label
        title_label = Label(
            text="[b]BTC SMA TRADING BOT[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=40,
            color=(0.2, 0.8, 1, 1)
        )
        self.add_widget(title_label)

        # Developer Credit / Owner Name
        dev_label = Label(
            text="Developed by: [b]Kyaw Thet Aung(Zeyo)[/b]",
            markup=True,
            font_size='15sp',
            size_hint_y=None,
            height=30,
            color=(0.9, 0.7, 0.2, 1)
        )
        self.add_widget(dev_label)

        # Price Display
        self.price_label = Label(
            text="BTC/USDT Price: Loading...",
            font_size='18sp',
            size_hint_y=None,
            height=35,
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.price_label)

        # SMA Values
        self.sma_label = Label(
            text="SMA (20): -- | SMA (50): --",
            font_size='15sp',
            size_hint_y=None,
            height=30,
            color=(0.8, 0.8, 0.8, 1)
        )
        self.add_widget(self.sma_label)

        # Trading Signal
        self.signal_label = Label(
            text="Signal: WAITING FOR DATA",
            font_size='18sp',
            size_hint_y=None,
            height=40,
            color=(1, 1, 0, 1)
        )
        self.add_widget(self.signal_label)

        # Log Area
        self.log_label = Label(
            text="System initialized...\nWaiting to fetch data...\n",
            font_size='13sp',
            size_hint_y=None,
            color=(0.7, 1, 0.7, 1),
            halign='left',
            valign='top'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.log_label)
        self.add_widget(scroll)

        # Refresh Button
        self.fetch_btn = Button(
            text="Refresh Market Data",
            font_size='16sp',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.fetch_btn.bind(on_press=self.trigger_fetch)
        self.add_widget(self.fetch_btn)

        # Auto fetch on start
        Clock.schedule_once(lambda dt: self.trigger_fetch(None), 1)

    def append_log(self, msg):
        self.log_label.text += f"\n{msg}"

    def trigger_fetch(self, instance):
        self.append_log("Fetching market data from Binance...")
        threading.Thread(target=self.fetch_data, daemon=True).start()

    def fetch_data(self):
        try:
            exchange = ccxt.binance()
            ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=60)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            
            df['sma20'] = df['close'].rolling(window=20).mean()
            df['sma50'] = df['close'].rolling(window=50).mean()

            latest_close = df['close'].iloc[-1]
            latest_sma20 = df['sma20'].iloc[-1]
            latest_sma50 = df['sma50'].iloc[-1]

            if latest_sma20 > latest_sma50:
                signal = "BUY SIGNAL (Bullish / Golden Cross)"
                sig_color = (0, 1, 0, 1)
            else:
                signal = "SELL / BEARISH SIGNAL"
                sig_color = (1, 0.3, 0.3, 1)

            def update_ui(dt):
                self.price_label.text = f"BTC/USDT Price: ${latest_close:,.2f}"
                self.sma_label.text = f"SMA (20): ${latest_sma20:,.2f} | SMA (50): ${latest_sma50:,.2f}"
                self.signal_label.text = f"Signal: {signal}"
                self.signal_label.color = sig_color
                self.append_log(f"Data updated successfully! Close: ${latest_close:,.2f}")

            Clock.schedule_once(update_ui, 0)

        except Exception as e:
            def update_err(dt):
                self.append_log(f"Error fetching data: {str(e)}")
            Clock.schedule_once(update_err, 0)

class BTCSMABotApp(App):
    def build(self):
        self.title = "BTC SMA Bot by Kyaw Thet Aung(Zeyo)"
        return TradingBotUI()

if __name__ == '__main__':
    BTCSMABotApp().run()
