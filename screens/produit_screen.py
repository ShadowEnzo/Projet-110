import random
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from controllers.produit_controller import ProduitController
from kivy.properties import ListProperty, StringProperty

Builder.load_file("kv/produit_screen.kv")

class ProduitScreen(Screen):
    produits = ListProperty([])
    message = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = ProduitController()
        self.charger_produits()

    def charger_produits(self):
        self.produits = self.controller.charger_produits()
        self.ids.produit_list.clear_widgets()
        for produit in self.produits:
            produit_id = produit[0]
            nom = produit[1]
            categorie = produit[2]
            prix = produit[3]
            stock = produit[4]
            btn = Button(
                text=f"{nom} | Cat: {categorie} | Prix: {prix} | Stock: {stock}",
                size_hint_y=None,
                height=40
            )
            btn.bind(on_release=lambda btn, p_id=produit_id: self.supprimer_produit(p_id))
            self.ids.produit_list.add_widget(btn)

    def ajouter_produit(self, nom, categorie, prix, stock):
        try:
            prix_val = float(prix)
            stock_val = int(stock)
            if not nom:
                self.message = "Le nom du produit est obligatoire."
                return
            self.controller.ajouter_produit(nom, categorie, prix_val, stock_val)
            self.message = "Produit ajouté avec succès."
            self.charger_produits()
        except ValueError:
            self.message = "Prix et stock doivent être des nombres valides."

    def supprimer_produit(self, produit_id):
        self.controller.supprimer_produit(produit_id)
        self.message = "Produit supprimé."
        self.charger_produits()

    def importer_produits_exemple(self):
        exemples = [
            ("Riz local 5kg", "Aliment sec", 8000),
            ("Spaghetti 500g", "Aliment sec", 3000),
            ("Farine de blé 1kg", "Aliment sec", 2500),
            ("Bonbons mix", "Confiserie", 500),
            ("Biscuit sachet", "Snack", 1500),
            ("Chocolat tablette", "Snack", 2500),
            ("Savon 100g", "Hygiène", 1000),
            ("Dentifrice 75ml", "Hygiène", 1500),
            ("Papier toilette (4 rouleaux)", "Hygiène", 2500),
            ("Liquide vaisselle 1L", "Ménager", 3000),
            ("Poudre à laver 500g", "Ménager", 2500),
            ("Allumettes boîte", "Ménager", 200),
            ("Huile 1L", "Condiment", 6500),
            ("Sel fin 1kg", "Condiment", 1000),
            ("Sucre 1kg", "Condiment", 2500),
        ]
        for nom, cat, prix in exemples:
            stock = random.randint(10, 100)
            self.controller.ajouter_produit(nom, cat, prix, stock)

        self.message = "Produits d'exemple ajoutés avec succès."
        self.charger_produits()
