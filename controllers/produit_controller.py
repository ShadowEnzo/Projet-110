from models.produits import ajouter_produit, mettre_a_jour_stock, get_produit, supprimer_produit, lister_produits

class ProduitController:
    def __init__(self):
        self.produits = []

    def charger_produits(self):
        self.produits = lister_produits()
        return self.produits

    def ajouter_produit(self, nom, categorie, prix_unitaire, stock):
        if not nom:
            raise ValueError("Le nom du produit est obligatoire.")
        ajouter_produit(nom, categorie, prix_unitaire, stock)

    def modifier_stock(self, produit_id, nouvelle_quantite):
        mettre_a_jour_stock(produit_id, nouvelle_quantite)

    def supprimer_produit(self, produit_id):
        supprimer_produit(produit_id)

    def get_produit(self, produit_id):
        return get_produit(produit_id)
