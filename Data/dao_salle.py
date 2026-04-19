import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("data/config.json", "r") as fichier:
            config = json.load(fichier)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO salle VALUES (%s,%s,%s,%s)",
                       (salle.code, salle.libelle, salle.type, salle.capacite))
        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s",
                       (salle.libelle, salle.type, salle.capacite, salle.code))
        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        connection = self.get_connection()
        cursor = connection.cursor()
        requete = "SELECT * FROM salle WHERE code=%s"
        cursor.execute(requete, (code,))
        resultat = cursor.fetchone()
        cursor.close()
        connection.close()

        if resultat:
            return resultat
        return None

    def get_salles(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        requete = "SELECT * FROM salle"
        cursor.execute(requete)
        resultats = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultats



