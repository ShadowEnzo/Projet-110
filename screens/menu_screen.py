from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file("kv/menu_screen.kv")

class MenuScreen(Screen):
    def on_pre_enter(self):
        role = self.manager.app.utilisateur_role
        if role == "admin":
            self.ids.btn_gestion_utilisateurs.disabled = False
            self.ids.btn_gestion_utilisateurs.opacity = 1
        else:
            self.ids.btn_gestion_utilisateurs.disabled = True
            self.ids.btn_gestion_utilisateurs.opacity = 0
