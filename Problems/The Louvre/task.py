class Painting:
    museum = 'the Louvre'
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

t = input()
a = input()
y = input()

art = Painting(t, a, y)

print(f'"{art.title}" by {art.artist} ({art.year}) hangs in {Painting.museum}.')

