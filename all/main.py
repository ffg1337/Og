import kivy


kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder

from  kivy.factory import Factory
from secret import *
from resolution import *
from windows import *
from saving import *

class TitleApp(App):
    title = "With Inheritance of BLMother"
    global sm
    sm = ScreenManager()

    def build(self):
        Builder.load_file('../styles/aboutgame.kv')
        Builder.load_file('../styles/continuegame.kv')
        Builder.load_file('../styles/mainwidow.kv')
        Builder.load_file('../styles/newgame.kv')
        # Set icon
        self.icon = '../img/icon.png'

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(NewGameScreen(name='NewGameScreen'))

        sm.add_widget(ScreenOfNewGame0(name='ScreenOfNewGame0'))
        sm.add_widget(ScreenOfNewGame1(name='ScreenOfNewGame1'))
        sm.add_widget(ScreenOfNewGame2(name='ScreenOfNewGame2'))
        sm.add_widget(ScreenOfNewGame3(name='ScreenOfNewGame3'))
        sm.add_widget(ScreenOfNewGame4(name='ScreenOfNewGame4'))
        sm.add_widget(ScreenOfNewGame5(name='ScreenOfNewGame5'))
        sm.add_widget(ScreenOfNewGame6(name='ScreenOfNewGame6'))
        sm.add_widget(ScreenOfNewGame7(name='ScreenOfNewGame7'))
        sm.add_widget(ScreenOfNewGame8(name='ScreenOfNewGame8'))
        sm.add_widget(ScreenOfNewGame9(name='ScreenOfNewGame9'))
        sm.add_widget(ScreenOfNewGame10(name='ScreenOfNewGame10'))

        sm.add_widget(ContinueGameScreen(name='ContinueGameScreen'))

        sm.add_widget(AboutGameScreen(name='AboutGameScreen'))

        return sm


    if __name__ == '__main__':
        Resolution().check()
        TitleApp().run()
