import tkinter as tk
import os

window = tk.Tk()
window.title("Interface Administrateur")
window.geometry("300x200")
window.iconbitmap(r"C:\Users\Ilan\Desktop\s\administrateur.ico")
window.config(bg="#0e537a")

def popup():
    # Crée la fenêtre popup
    pop = tk.Toplevel(window)
    pop.title("Fichier ou dossier à ouvrir")
    pop.geometry("400x150")
    pop.iconbitmap(r"C:\Users\Ilan\Desktop\s\administrateur.ico")
    pop.config(bg="#0e537a")

    label = tk.Label(pop, text="Entrez le chemin du fichier ou dossier à ouvrir :", 
                     bg="#0e537a", fg="white", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(pop, width=50)
    entry.pack(pady=5)
    entry.focus()

    def valider():
        chemin = entry.get()
        try:
            os.startfile(chemin)
            pop.destroy()
        except Exception as e:
            erreur_label.config(text=f"Erreur : {e}")

    bouton_valider = tk.Button(pop, text="Ouvrir", command=valider, 
                              bg="#0e537a", fg="white", font=("Arial", 12))
    bouton_valider.pack(pady=10)

    erreur_label = tk.Label(pop, text="", bg="#0e537a", fg="red", font=("Arial", 10))
    erreur_label.pack()

bouton = tk.Button(window, text="Ouvrir fichier/dossier", command=popup, 
                   bg="#0e537a", fg="white", font=("Arial", 12))
bouton.pack(pady=40)

window.mainloop()
