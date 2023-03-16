import platform
import cpuinfo
import socket
import os


# ------------------------------
# Classe System qui va contenir toutes les infos dont on a besoin pour les afficher dans le front
# ------------------------------
class System:
    # ------------------------------
    # Constructeur qui sera appelé à chaque instanciation de la classe
    # ------------------------------
    def __init__(self):
        self._system = platform.system()
        self._architecture = platform.architecture()
        self._release = platform.release()
        self._processor = cpuinfo.get_cpu_info()["brand_raw"]
        self._hostname = socket.gethostname()
        self._ip = socket.gethostbyname(self._hostname)
        self._username = os.getlogin()

    # ------------------------------
    # Getters
    # ------------------------------
    @property
    def getSystem(self):
        return self._system

    @property
    def getArchitecture(self):
        return self._architecture

    @property
    def getRelease(self):
        return self._release

    @property
    def getProcessor(self):
        return self._processor

    @property
    def getHostname(self):
        return self._hostname

    @property
    def getIp(self):
        return self._ip

    @property
    def getUsername(self):
        return self._username

    # ------------------------------
    # Méthode qui permet de mettre toutes les variables du constructeur dans un dictionnaire python
    # une méthode to_array simple
    # ------------------------------
    def to_dict(self):
        return {
            "systeme": self.getSystem,
            "architecture": self.getArchitecture,
            "release": self.getRelease,
            "processeur": self.getProcessor,
            "hostname": self.getHostname,
            "ip": self.getIp,
            "username": self.getUsername
        }
