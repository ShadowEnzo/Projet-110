from models.client import ajouter_client, get_client, lister_clients, supprimer_client

class ClientController:
    def __init__(self):
        self.clients = []

    def charger_clients(self):
        self.clients = lister_clients()
        return self.clients

    def ajouter_client(self, nom, telephone, adresse):
        if not nom:
            raise ValueError("Le nom du client est obligatoire.")
        ajouter_client(nom, telephone, adresse)

    def supprimer_client(self, client_id):
        supprimer_client(client_id)

    def get_client(self, client_id):
        return get_client(client_id)
