class Song:
    #every method takes self as the first parameter
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.n_streams = 0

    # __str__ method  defines how python should print out instance of our Song Object
    def __str__(self):
        return f"{self.title} by {self.artist} \nStreams: {self.n_streams}"
    # Play method is a custome method for our class song that increases the number of steams by 1
    def play(self):
        print('Now playing: ' + self.title)
        self.n_streams += 1


my_list_object = []
my_list_object.append(2)

my_song_object = Song('Single Ladies','Beyonce')
print(my_song_object)
sorry = Song('Sorry','Justin Beiber')
playlist = [my_song_object, sorry]
print(sorry)
# Plays the song 10 times
for i in range(10):
    sorry.play()
print(sorry)
print(my_song_object)
