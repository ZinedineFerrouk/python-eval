import json


class Personne:
    def __init__(self, nom, prenom, age, date_de_naissance, genre):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.date_de_naissance = date_de_naissance
        self.genre = genre

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "date_de_naissance": self.date_de_naissance,
            "genre": self.genre
        }


if __name__ == "__main__":
    personne = Personne("FERROUK", "Zinedine", 24, "1998-06-26", "Homme")
    personne_dict = personne.to_dict()
    personne_json = json.dumps(personne_dict)
    print(personne_json)
