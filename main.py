from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BTCSMAApp(App):
    def build(self):
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title Label with Name
        self.title_label = Label(
            text='BTC SMA Bot\nby Kyaw Thet Aung (Zeyo)',
            font_size=22,
            halign='center',
            valign='middle'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        layout.add_widget(self.title_label)
        
        # Status Label
        self.status_label = Label(
            text='Status: Ready to run',
            font_size=16,
            halign='center'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)
        
        # Action Button
        self.btn = Button(
            text='Check BTC SMA',
            size_hint=(1, 0.2),
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.btn.bind(on_press=self.on_button_click)
        layout.add_widget(self.btn)
        
        return layout

    def on_button_click(self, instance):
        self.status_label.text = 'Fetching BTC data...'
        # နောက်ပိုင်း ကိုကို့ရဲ့ Bot logic တွေကို ဒီနေရာမှာ ထည့်လို့ရပါတယ်

if __name__ == '__main__':
    BTCSMAApp().run()
