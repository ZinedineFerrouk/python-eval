import platform
import cpuinfo
import socket
import os


# Classe System qui va contenir toutes les infos dont on a besoin pour les afficher dans le front
class System:
    #Constructeur qui sera appelé à chaque instanciation de la classe
    def __init__(self):
        self.system = platform.system()
        self.architecture = platform.architecture()
        self.processor = cpuinfo.get_cpu_info()["brand_raw"]
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.username = os.getlogin()

    # Méthode qui permet de mettre toutes les variables du constructeur dans un dictionnaire python
    # une méthode to_array simple
    def to_dict(self):
        return {
            "systeme": self.system,
            "architecture": self.architecture,
            "processeur": self.processor,
            "hostname": self.hostname,
            "ip": self.ip,
            "username": self.username
        }
