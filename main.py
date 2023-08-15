from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.icon_definitions import md_icons

from bardapi import Bard

import os

os.environ["_BARD_API_KEY"] = "Zwgdrpi8hkvaoMEylsSyuCpTG2ygEMlayjYkG4QG5_nAqLRlTeG_2R9Npstk57EIP9ZJGQ."
    
class BearAI(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #self.root = BoxLayout(orientation="vertical")
        self.root = BoxLayout(orientation="vertical", spacing="10dp", padding="10dp")
        
        header = BoxLayout(orientation="horizontal", spacing="10dp", size_hint_y=None, height="100dp", )
        #header.add_widget(Image(source="chat_icon.png", size_hint=(None, None), size=("30dp", "30dp")))
        header.add_widget(MDLabel(text="BearAI", font_name="uo.ttf", theme_text_color="Secondary", font_style="H5", markup=True ))
        self.root.add_widget(header)

        self.chat_history = MDScrollView()
        self.chat_box = MDLabel(size_hint_y=None, valign="top", padding="10dp", markup=True)
        self.chat_box.bind(texture_size=self._set_chat_box_height)
        self.chat_history.add_widget(self.chat_box)
        self.root.add_widget(self.chat_history)

        self.input_box = MDTextField(hint_text="Type a message...", size_hint_y=None, height="40dp"  )
        self.send_button = MDFillRoundFlatButton(text="Send", size_hint=(None, None), size=("40dp", "40dp"))
        self.send_button.bind(on_press=self.send_message)
        input_layout = MDBoxLayout(orientation="horizontal", spacing="10dp", padding="10dp", size_hint_y=None, height="60dp")
        input_layout.add_widget(self.input_box)
        input_layout.add_widget(self.send_button)
        self.root.add_widget(input_layout)
        

        return self.root

    def _set_chat_box_height(self, instance, size):
        instance.height = size[1]

    def send_message(self, instance):
        user_message = self.input_box.text
        if user_message.strip() != "":
            self.add_message("You", user_message)
            self.input_box.text = ""
            bot_response = self.get_bot_response(user_message)
            self.add_message("Bot", bot_response)
            self.chat_history.scroll_to(self.chat_box)

    def add_message(self, sender, message):
        self.chat_box.text += f"\n[b]{sender}[/b]: {message}\n"

    def get_bot_response(self, user_message):
        # You can implement your chatbot logic here
        # For simplicity, let's just echo the user's message
        return (Bard().get_answer(str(user_message))['content'])

if __name__ == "__main__":
    BearAI().run()
