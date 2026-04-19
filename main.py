from Data.dao_salle import DataSalle
from models.salle import Salle

dat = DataSalle()

try:
    conn = dat.get_connection()
    print("Connexion réussie")
    conn.close()
except Exception as e:
    print("Erreur connexion :", e)
s1 = Salle("S1", "Salle Info", "Laboratoire", 30)
s2 = Salle("S2", "Salle Réunion", "Bureau", 20)
s3 = Salle("S3", "Salle Classe", "Classe", 40)

dat.insert_salle(s1)
dat.insert_salle(s2)
dat.insert_salle(s3)