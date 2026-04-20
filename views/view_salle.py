import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle
from models.salle import Salle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
