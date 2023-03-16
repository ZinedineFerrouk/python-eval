import random


class Citation:
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return self.phrase


class CitationsAleatoires:
    def __init__(self):
        self.citations = [
            Citation("La douleur d'aujourd'hui est la victoire de demain. - Rocky"),
            Citation("Coca bien frais chacal - Arouf Gangsta"),
            Citation("Si vous avez rêvé de cela, vous pouvez le faire. - Mohammed Ali"),
            Citation("N'arrêtez pas de vous entraîner juste parce que quelque chose est difficile."
                     "Tout ce qui vaut la peine d'être fait est difficile. - Mohammed Ali"),
            Citation("Ce n'est pas le succès qui importe, c'est l'effort. - Rocky")
        ]

    def citation_aleatoire(self):
        return random.choice(self.citations)


if __name__ == "__main__":
    citations_aleatory = CitationsAleatoires()
    citation = citations_aleatory.citation_aleatoire()
    print(citation)