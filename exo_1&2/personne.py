import json


# ------------------------------
# Class Personne
# ------------------------------
class Personne:
    # ------------------------------
    # Constructor
    # ------------------------------
    def __init__(self, nom, prenom, age, date_de_naissance, genre):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._date_de_naissance = date_de_naissance
        self._genre = genre

    # ------------------------------
    # Getters
    # ------------------------------
    @property
    def getNom(self):
        return self._nom

    @property
    def getPrenom(self):
        return self._prenom

    @property
    def getAge(self):
        return self._age

    @property
    def getNaissance(self):
        return self._date_de_naissance

    @property
    def getGenre(self):
        return self._genre

    # ------------------------------
    # Setters
    # ------------------------------

    def setNom(self, value):
        self._nom = value

    def setPrenom(self, value):
        self._prenom = value

    def setAge(self, value):
        self._age = value

    def setDate_de_naissance(self, value):
        self._date_de_naissance = value

    def setGenre(self, value):
        self._genre = value

    # ------------------------------
    # Méthode toArray
    # ------------------------------
    def to_dict(self):
        return {
            "nom": self.getNom,
            "prenom": self.getPrenom,
            "age": self.getAge,
            "date_de_naissance": self.getNaissance,
            "genre": self.getGenre
        }


if __name__ == "__main__":
    personne_dict = (Personne("FERROUK", "Zinedine", 24, "1998-06-26", "Homme").to_dict())
    personne_json = json.dumps(personne_dict)
    print(personne_json)
