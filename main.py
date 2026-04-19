from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

try:
    conn = dao.get_connection()
    print("Connexion réussie")
    conn.close()
except Exception as e:
    print("Erreur connexion :", e)