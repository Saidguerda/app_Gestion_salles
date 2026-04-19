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




