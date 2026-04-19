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

    def supprimer_salle(self, code):
        if code == "":
            print("Code vide")
            return False
        else:
            self.dao.delete_salle(code)
            print("Salle supprimée")
            return True

    def rechercher_salle(self, code):
        if code == "":
            print("Code vide")
            return False
        else:
            s = self.dao.get_salle(code)
            if s:
                print("Salle trouvée")
                s.afficher_infos()
                return True
            else:
                print("Salle non trouvée")
                return False

    def recuperer_salles(self):
        liste = self.dao.get_salles()
        if liste:
            for s in liste:
                s.afficher_infos()
            return True
        else:
            print("Aucune salle")
            return False