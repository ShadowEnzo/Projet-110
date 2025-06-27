from controllers.client_controller import ClientController

def test_clients():
    ctrl = ClientController()

    print("Ajout d'un client...")
    ctrl.ajouter_client("Jean Dupont", "0340000000", "Antananarivo")

    print("Liste des clients :")
    for client in ctrl.charger_clients():
        print(client)

    print("Suppression du client ID 1...")
    ctrl.supprimer_client(1)

    print("Liste des clients mise à jour :")
    print(ctrl.charger_clients())

if __name__ == "__main__":
    test_clients()
