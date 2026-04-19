from Data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, s):
        if s.code == "" or s.libelle == "" or s.type == "" or s.capacite == "":
            print("Champs vides")
            return False
        else:
            if int(s.capacite) < 1:
                print("Capacité invalide")
                return False
            else:
                self.dao.insert_salle(s)
                print("Salle ajoutée")
                return True

    def modifier_salle(self, s):
        if int(s.capacite) < 1:
            print("Capacité invalide")
            return False
        else:
            self.dao.update_salle(s)
            print("Salle modifiée")
            return True