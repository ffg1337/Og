from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from main import *
#:import Factory kivy.factory.Factory
from  kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition, CardTransition, SwapTransition, \
    FadeTransition, WipeTransition, FallOutTransition, RiseInTransition

import webbrowser



class MenuScreen(Screen):
    pass


class NewGameScreen(Screen):
    pass

# class NewGameCheckUser: pass
class ScreenOfNewGame0(Screen): pass


class ScreenOfNewGame1(Screen): pass


class ScreenOfNewGame2(Screen): pass


class ScreenOfNewGame3(Screen): pass


class ScreenOfNewGame4(Screen): pass


class ScreenOfNewGame5(Screen): pass


class ScreenOfNewGame6(Screen): pass


class ScreenOfNewGame7(Screen): pass


class ScreenOfNewGame8(Screen): pass


class ScreenOfNewGame9(Screen): pass


class ScreenOfNewGame10(Screen): pass


class ContinueGameScreen(Screen): pass



class AboutGameScreen(Screen):

    def any_Function(instnce):
        webbrowser.open('https://vk.com/binarybin')


class SettingsScreen3(Screen):
    pass


class SettingsScreen4(Screen):
    pass
