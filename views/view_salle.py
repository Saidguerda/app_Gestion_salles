import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle
from models.salle import Salle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()
        self.title("Gestion des salles")
        self.geometry("600x500")

        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Code").grid(row=0, column=0)
        self.code = ctk.CTkEntry(self.cadreInfo)
        self.code.grid(row=0, column=1)

        ctk.CTkLabel(self.cadreInfo, text="Libellé").grid(row=1, column=0)
        self.libelle = ctk.CTkEntry(self.cadreInfo)
        self.libelle.grid(row=1, column=1)

        ctk.CTkLabel(self.cadreInfo, text="Type").grid(row=2, column=0)
        self.type = ctk.CTkEntry(self.cadreInfo)
        self.type.grid(row=2, column=1)

        ctk.CTkLabel(self.cadreInfo, text="Capacité").grid(row=3, column=0)
        self.capacite = ctk.CTkEntry(self.cadreInfo)
        self.capacite.grid(row=3, column=1)



