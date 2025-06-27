from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from controllers.vente_controller import VenteController
from controllers.client_controller import ClientController
from controllers.produit_controller import ProduitController
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("kv/vente_screen.kv")

class VenteScreen(Screen):
    clients = ListProperty([])
    produits = ListProperty([])
    panier = ListProperty([])
    message = StringProperty("")
    total = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vente_ctrl = VenteController()
        self.client_ctrl = ClientController()
        self.produit_ctrl = ProduitController()
        self.charger_clients()
        self.charger_produits()
        self.panier = []

    def charger_clients(self):
        self.clients = self.client_ctrl.charger_clients()

    def charger_produits(self):
        self.produits = self.produit_ctrl.charger_produits()

    def ajouter_au_panier(self, produit_id, quantite):
        try:
            quant = int(quantite)
            if quant <= 0:
                self.message = "Quantité doit être > 0"
                return
        except:
            self.message = "Quantité invalide"
            return

        produit = self.produit_ctrl.get_produit(produit_id)
        if not produit:
            self.message = "Produit introuvable"
            return

        prix_total = produit[3] * quant  # prix_unitaire * quant

        # Vérifier si déjà dans panier
        for item in self.panier:
            if item['produit_id'] == produit_id:
                item['quantite'] += quant
                item['prix_total'] += prix_total
                self.calculer_total()
                self.message = "Produit ajouté au panier"
                return

        self.panier.append({
            'produit_id': produit_id,
            'nom': produit[1],
            'quantite': quant,
            'prix_total': prix_total
        })
        self.calculer_total()
        self.message = "Produit ajouté au panier"

    def supprimer_du_panier(self, produit_id):
        self.panier = [item for item in self.panier if item['produit_id'] != produit_id]
        self.calculer_total()

    def calculer_total(self):
        self.total = sum(item['prix_total'] for item in self.panier)

    def valider_vente(self, client_id, utilisateur_id=1):
        # utilisateur_id statique pour test, à adapter
        if not self.panier:
            self.message = "Le panier est vide"
            return

        if not client_id:
            self.message = "Sélectionnez un client"
            return

        vente_id = self.vente_ctrl.creer_vente(client_id, utilisateur_id, self.panier)
        self.panier = []
        self.calculer_total()
        self.message = f"Vente enregistrée (ID: {vente_id})"
        self.charger_produits()  # pour rafraîchir stock si tu as gestion stock dans controller
