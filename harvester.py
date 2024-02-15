import tkinter as tk
import threading
import os
import paramiko
import subprocess
import socket

def execute_scan():
    # Exécuter le script de scan réseau dans un thread séparé
    threading.Thread(target=run_scan).start()

def update_project():
    # Informations de connexion SSH
    hostname = '192.168.189.238'
    username = 'user'
    password = 'user'

    # Commande à exécuter sur le serveur distant pour mettre à jour le projet
    command = 'python3 /srv/partage/script/update_script.py'

    try:
        # Établir une connexion SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        # Exécuter la commande sur le serveur distant
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Afficher la sortie de la commande
        output = stdout.read().decode()
        print(output)

        # Fermer la connexion SSH
        ssh_client.close()

        # Afficher un message de succès dans l'interface graphique
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output)
    except Exception as e:
        error_message = f"Erreur lors de la connexion SSH : {e}"
        print(error_message)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, error_message)

def run_scan():
    # Lancer le script client_gui.py pour afficher les résultats d'analyse réseau
    script_path = os.path.join("Z:/script/", "nmap_client.py")
    subprocess.run(["py", script_path])

def fetch_data_from_server(request):
    # Fonction pour envoyer une demande au serveur et récupérer les données
    HOST = '10.1.2.1'  # Adresse IP du serveur
    PORT = 12345        # Port sur lequel le serveur écoute

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(request.encode())
        data = client_socket.recv(4096).decode()
        return data

def fetch_application_version():
    # Fonction pour récupérer la version de l'application depuis le serveur
    request = "get_application_version"
    version = fetch_data_from_server(request)
    return version
def update_display():
    # Mettre à jour les informations affichées dans l'interface graphique en récupérant les données du serveur
    application_version = fetch_application_version()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Version de l'application : 1.0 {application_version}")

def get_remote_hostname(remote_ip):
    try:
        hostname = socket.gethostbyaddr(remote_ip)[0]
        return hostname
    except Exception as e:
        print(f"Erreur lors de la récupération du nom d'hôte : {e}")
        return None

# Adresse IP de la machine distante
remote_ip = '10.1.2.1'  # Remplacez par l'adresse IP de la machine distante

# Appel de la fonction pour récupérer le nom d'hôte
hostname = get_remote_hostname(remote_ip)

# Affichage du résultat
if hostname:
    print(f"Nom d'hôte de la machine distante : {hostname}")
else:
    print("Impossible de récupérer le nom d'hôte de la machine distante.")


# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface principale")

# Ajouter un bouton pour afficher les résultats
results_button = tk.Button(root, text="Lancer le scan du réseau", command=execute_scan)
results_button.pack(pady=5)

# Ajouter un bouton pour mettre à jour le projet
update_button = tk.Button(root, text="Mettre à jour le projet", command=update_project)
update_button.pack(pady=5)

# Ajouter un bouton pour récupérer les données du serveur
fetch_data_button = tk.Button(root, text="Récupérer les données du serveur", command=update_display)
fetch_data_button.pack(pady=5)

# Ajouter une zone de texte pour afficher les résultats ou les messages d'erreur
result_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
result_text.pack(pady=5)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
