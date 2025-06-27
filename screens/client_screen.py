import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from controllers.client_controller import ClientController
from kivy.properties import ListProperty, StringProperty
from kivy.uix.button import Button

Builder.load_file("kv/client_screen.kv")

class ClientScreen(Screen):
    clients = ListProperty([])
    message = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ClientController()
        self.charger_clients()

    def charger_clients(self):
        self.clients = self.controller.charger_clients()
        self.ids.client_list.clear_widgets()
        for client in self.clients:
            btn = Button(
                text=f"{client[1]} - {client[2]} - {client[3]}",
                size_hint_y=None,
                height=40
            )
            btn.bind(on_release=lambda btn, c_id=client[0]: self.supprimer_client(c_id))
            self.ids.client_list.add_widget(btn)

    def ajouter_client(self, nom, telephone, adresse):
        try:
            self.controller.ajouter_client(nom, telephone, adresse)
            self.message = "Client ajouté avec succès."
            self.charger_clients()
        except Exception as e:
            self.message = f"Erreur : {str(e)}"

    def supprimer_client(self, client_id):
        self.controller.supprimer_client(client_id)
        self.message = "Client supprimé."
        self.charger_clients()
