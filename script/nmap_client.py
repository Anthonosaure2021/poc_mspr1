# client_gui.py
import tkinter as tk
import socket

# Paramètres du client
HOST = '10.1.2.1'
PORT = 12345

# Créer la fenêtre tkinter
window = tk.Tk()
window.title("Résultats d'analyse réseau")

# Créer la zone de texte pour afficher les résultats
result_text = tk.Text(window, wrap=tk.WORD, height=20, width=80)
result_text.pack()

# Créer un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Établir la connexion avec le serveur
client_socket.connect((HOST, PORT))

# Recevoir les résultats de l'analyse depuis le serveur
analysis_results = client_socket.recv(4096).decode()

# Afficher les résultats dans la zone de texte
result_text.insert(tk.END, analysis_results)

# Fermer la connexion
client_socket.close()

# Lancer la boucle principale de l'interface graphique
window.mainloop()
