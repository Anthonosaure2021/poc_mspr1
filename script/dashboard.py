import socket
import nmap
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

def get_local_ip_and_hostname():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip, hostname

def get_connected_devices_count():
    # Insérez ici votre logique pour compter les appareils connectés sur le LAN
    return 10

def get_network_scan_results():
    # Exécutez votre analyse réseau et obtenez les résultats
    nm = nmap.PortScanner()
    nm.scan('10.1.2.0/8', arguments='-p 1-65535')
    return nm.all_hosts()

def get_wan_latency():
    # Exécutez un ping sur une cible WAN et mesurez la latence
    ping_result = subprocess.run(['ping', '-c', '5', 'google.com'], capture_output=True)
    latency_output = ping_result.stdout.decode()
    # Analysez la sortie du ping pour extraire la latence moyenne
    # Par exemple, en utilisant une expression régulière ou en séparant les lignes et en analysant les valeurs
    latency = "10 ms"  # Exemple
    return latency

def get_application_version():
    # Insérez ici votre logique pour obtenir la version de l'application
    return "1.0"

@app.route('/')
def dashboard():
    local_ip, hostname = get_local_ip_and_hostname()
    connected_devices_count = get_connected_devices_count()
    network_scan_results = get_network_scan_results()
    wan_latency = get_wan_latency()
    application_version = get_application_version()
    return render_template('dashboard.html', local_ip=local_ip, hostname=hostname, connected_devices_count=connected_devices_count, network_scan_results=network_scan_results, wan_latency=wan_latency, application_version=application_version)

if __name__ == '__main__':
    # Modifier le port sur lequel Flask écoute en spécifiant l'argument port
    app.run(debug=True, host='0.0.0.0', port=8080)  # Flask écoutera sur le port 8080
