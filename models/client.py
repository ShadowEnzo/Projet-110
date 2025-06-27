from database.database import get_connexion

def ajouter_client(nom, telephone, adresse):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        INSERT INTO clients (nom, telephone, adresse)
        VALUES (?, ?, ?)
    """, (nom, telephone, adresse))
    conn.commit()
    conn.close()

def get_client(client_id):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        SELECT * FROM clients WHERE id = ?
    """, (client_id,))
    client = curseur.fetchone()
    conn.close()
    return client

def lister_clients():
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM clients")
    clients = curseur.fetchall()
    conn.close()
    return clients

def supprimer_client(client_id):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    conn.close()
