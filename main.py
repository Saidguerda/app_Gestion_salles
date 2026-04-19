from Data.dao_salle import DataSalle
from models.salle import Salle

dat = DataSalle()

try:
    conn = dat.get_connection()
    print("Connexion réussie")
    conn.close()
except Exception as e:
    print("Erreur connexion :", e)
s1 = Salle("S5", "Salle Info", "Laboratoire", 30)
s2 = Salle("S4", "Salle Réunion", "Bureau", 20)
s3 = Salle("S0", "Salle Classe", "Classe", 40)

dat.insert_salle(s1)
dat.insert_salle(s2)
dat.insert_salle(s3)

s1_modif = Salle("S5", "Salle Informatique", "Lab", 35)
dat.update_salle(s1_modif)

dat.get_salle("S5").afficher_infos()

for s in dat.get_salles():
    s.afficher_infos()

dat.delete_salle("S5")