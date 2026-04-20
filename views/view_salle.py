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

