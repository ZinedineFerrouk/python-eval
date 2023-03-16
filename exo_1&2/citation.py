import random


class CitationsAleatory:
    def __init__(self):
        self._citations = [
            "La douleur d'aujourd'hui est la victoire de demain. - Rocky",
            "Coca bien frais chacal - Arouf Gangsta",
            "Si vous avez rêvé de cela, vous pouvez le faire. - Mohammed Ali",
            "N'arrêtez pas de vous entraîner juste parce que quelque chose est difficile.",
            "Tout ce qui vaut la peine d'être fait est difficile. - Mohammed Ali",
            "Ce n'est pas le succès qui importe, c'est l'effort. - Rocky"
        ]

    def citation_aleatoire(self):
        return random.choice(self._citations)


if __name__ == "__main__":
    citation = (CitationsAleatory().citation_aleatoire())
    print(citation)