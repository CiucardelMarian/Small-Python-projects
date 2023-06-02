class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.number_of_ratings = 0
        self.ratings = []

    def rate(self, rating: int):
        self.number_of_ratings += 1
        self.ratings.append(rating)

    def __str__(self):
        genres_string = ', '.join(self.genres)
        if self.number_of_ratings > 0:
            return f'{self.title} ({self.seasons} seasons) \ngenres: {genres_string} \n{self.number_of_ratings} ratings, average {sum(self.ratings) / len(self.ratings):.1f} points'
        return f'{self.title} ({self.seasons} seasons) \ngenres: {genres_string} \nno ratings'


def minimum_grade(rating: float, s_list: list):
    new_list = []
    for item in s_list:
        if sum(item.ratings) / len(item.ratings) >= rating:
            new_list.append(item)
    return new_list


def includes_genre(genre: str, s_list: list):
    new_list = []
    for item in s_list:
        if genre in item.genres:
            new_list.append(item)
    return new_list


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
