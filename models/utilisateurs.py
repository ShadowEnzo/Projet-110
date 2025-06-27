from database.database import get_connexion

def ajouter_utilisateur(nom, email, mot_de_passe, role):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        INSERT INTO utilisateurs (nom, email, mot_de_passe, role) 
        VALUES(?, ?, ?, ?)        
    """, (nom, email, mot_de_passe, role))
    conn.commit()
    conn.close()

def verifier_utlisateur(email, mot_de_passe):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        SELECT * FROM utilisateurs WHERE email = ? AND mot_de_passe = ?
    """,(email, mot_de_passe))
    utilisateur = curseur.fetchone()
    conn.close()
    return utilisateur

def obtenir_role(email):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        SELECT role FROM utilisateurs WHERE email = ? 
    """,(email,))
    resultat = curseur.fetchone()
    conn.close()
    return resultat

def supprimer_utilisateur(id):
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("""
        DELETE FROM utilisateurs WHERE id = ?
    """,(id,))
    conn.commit()
    conn.close()

def lister_utilisateurs():
    conn = get_connexion()
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM utilisateurs")
    utilisateurs = curseur.fetchall()
    conn.close()
    return utilisateurs

    