import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.menu_screen import MenuScreen
from screens.client_screen import ClientScreen
from screens.produit_screen import ProduitScreen
from screens.vente_screen import VenteScreen
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.home_screen import HomeScreen

class EpicerieApp(App):
    def ___init__(self, **kwargs):
        super().__init__(**kwargs)
        self.utilisateur_role = None
        
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ClientScreen(name="clients"))
        sm.add_widget(ProduitScreen(name="produits"))
        sm.add_widget(VenteScreen(name="ventes"))

        sm.current = "login"
        return sm

if __name__ == "__main__":
    EpicerieApp().run()
