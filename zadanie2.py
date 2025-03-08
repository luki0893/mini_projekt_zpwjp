class Movie:

    def __init__(self, tytul, rok, ocena):
        self.tytul = tytul
        self.rok = rok
        self.ocena = ocena


    def __repr__(self):
        return f"\nTytuł: {self.tytul}, rok: {self.rok}, ocena: {self.ocena}."


movies = [
        Movie("Skazani na Shawshank", 1994, 8.7),
        Movie("Zielona mila", 1999, 8.6),
        Movie("Nietykalni", 2011, 8.5),
        Movie("Ojciec chrzestny", 1972, 8.6),
        Movie("Lista Schindlera", 1993, 8.3),
        Movie("Pulp Fiction", 1994, 8.3),
        Movie("Pianista", 2002, 8.2),
        Movie("Gladiator", 2000, 8.1),
        Movie("Szeregowiec Ryan", 1998, 8.0),
        Movie("Interstellar", 2014, 7.9),
        Movie("Wróg u bram", 2001, 7.8)
]

print(movies)

# sortowanie po ocenie rosnąco i malejąco
movies_sorted_by_rating_asc = sorted(movies, key=lambda movie: movie.ocena)
movies_sorted_by_rating_desc = sorted(movies, key=lambda movie: movie.ocena, reverse=True)

# sortowanie po roku produkcji rosnąco i malejąco
movies_sorted_by_year_asc = sorted(movies, key=lambda movie: movie.rok)
movies_sorted_by_year_desc= sorted(movies, key=lambda movie: movie.rok, reverse=True)

# sortowanie alfabetyczne po tytule
movies_sorted_by_title = sorted(movies, key=lambda movie: movie.tytul)

print("\nFilmy posortowane alfabetycznie po tytule")
print(movies_sorted_by_title)

