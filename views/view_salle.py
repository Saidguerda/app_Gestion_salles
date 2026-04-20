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

        self.cadreActions = ctk.CTkFrame(self)
        self.cadreActions.pack(pady=10)

        self.btnAjouter = ctk.CTkButton(self.cadreActions, text="Ajouter",command=self.ajouter_salle)
        self.btnAjouter.grid(row=0, column=0)

        self.btnModifier = ctk.CTkButton(self.cadreActions, text="Modifier",command=self.modifier_salle)
        self.btnModifier.grid(row=0, column=1)

        self.btnSupprimer = ctk.CTkButton(self.cadreActions, text="Supprimer",command=self.supprimer_salle)
        self.btnSupprimer.grid(row=0, column=2)

        self.btnRechercher = ctk.CTkButton(self.cadreActions, text="Rechercher",command=self.rechercher_salle)
        self.btnRechercher.grid(row=0, column=3)

        self.cadreList = ctk.CTkFrame(self)
        self.cadreList.pack(pady=10)

        self.treeList = ttk.Treeview(self.cadreList,columns=("code", "libelle", "type", "capacite"),show="headings")
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.treeList.pack()

    def ajouter_salle(self):
            s = Salle(self.code.get(), self.libelle.get(), self.type.get(), int(self.capacite.get()))
            self.service_salle.ajouter_salle(s)

    def modifier_salle(self):
            s = Salle(self.code.get(), self.libelle.get(), self.type.get(), int(self.capacite.get()))
            self.service_salle.modifier_salle(s)

    def supprimer_salle(self):
            self.service_salle.supprimer_salle(self.code.get())

    def rechercher_salle(self):
        s = self.service_salle.rechercher_salle(self.code.get())
        if s:
            self.libelle.delete(0, "end")
            self.libelle.insert(0, s.libelle)

            self.type.delete(0, "end")
            self.type.insert(0, s.type)

            self.capacite.delete(0, "end")
            self.capacite.insert(0, s.capacite)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))



