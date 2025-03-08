class Playlist:

    def __init__(self):
        self.lista_utworow = []

    def __add__(self, other):
        if isinstance(other, Playlist):
            nowa_lista = Playlist()
            nowa_lista.lista_utworow = self.lista_utworow + other.lista_utworow
            return nowa_lista
        elif isinstance(other, str):
            self.lista_utworow.append(other)
            return self

    def __radd__(self, other):
        if isinstance(other, str):
            nowa_lista = Playlist()
            nowa_lista.lista_utworow = [other] + self.lista_utworow
            return nowa_lista

    def __getitem__(self, index):
        return self.lista_utworow[index]

    def __setitem__(self, index, utwor):
        if isinstance(utwor, str):
            self.lista_utworow[index] = utwor

    def __repr__(self):

        return f"Playlist({self.lista_utworow})"

p1 = Playlist()
p2 = Playlist()

# Dodanie utworów do list utworów
p1 + "Highway to hell"
p1 + "Summertime sadness"

p2 + "Stairways to heaven"
p2 + "Born to die"
print(p1)
print(p2)
print(p1[0])
p1[0] = "Whatever happens"


# Połączenie dwóch list utworów
polaczona_lista = p1 + p2
print(polaczona_lista)

# Dodanie utworu do nowo stworzonej listy utworów
nowa_lista =  "Thunderstruck" + polaczona_lista
print(nowa_lista)

