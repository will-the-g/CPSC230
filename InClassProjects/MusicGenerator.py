import random
def get_tempo(min=60, max=180):
    return random.randint(min, max)

def get_key():
    KEYS = ['Ab','A','Bb','B','C','C#','Db','D','Eb','E','F','F#','Gb','G']
    key = random.choice(KEYS)
    position = KEYS.index(key)
    return key, position
def get_progression(key_position, n_chords=4):
    CHORDS = [
        "Ab Bbm Cm Db Eb Fm Gdim",
        "A Bm C#m D E F#m G#dim",
        "Bb Cm Dm Eb F Gm Adim",
        "B C#m D#m E F# G#m A#dim",
        "C Dm Em F G Am Bdim",
        "C# D#m E#m F# G# A#m B#dim",
        "Db Ebm Fm Gb Ab Bbm Cdim",
        "D Em F#m G A Bm C#dim",
        "Eb Fm Gm Ab Bb Cm Ddim",
        "E F#m G#m A B C#m D#dim",
        "F Gm Am Bb C Dm Edim",
        "F# G#m A#m B C# D#m E#dim",
        "Gb Abm Bbm Cb Db Ebm Fdim",
        "G Am Bm C D Em F#dim",
    ]
    chords_in_key = CHORDS[key_position].split()
    chords = []
    for i in range(n_chords):
        chords.append(random.choice(chords_in_key))
    return ' '.join(chords)
option = input('Would you like to make a song?')
while option != 'no':
    option = input('Would you like to set a range for tempo?')
    if option == 'yes':
        min = int(input('Input a minimum'))
        max = int(input('Input a maximum'))
        tempo = get_tempo(min, max)
    else:
        tempo = get_tempo()
    key, position = get_key() 
    option = input('Would you like to change the number of chords from the default of 4')
    if option == 'yes':
        chords = int(input('Input the number of chords'))
        print(f"Tempo: {tempo}, Key: {key}, \nProgression 1: {get_progression(position, chords)} \nProgression 2: {get_progression(position, chords)} \nProgression 3: {get_progression(position, chords)} ")
    else:
        print(f"Tempo: {tempo}, Key: {key}, \nProgression 1: {get_progression(position)} \nProgression 2: {get_progression(position)} \nProgression 3: {get_progression(position)} ")
    option = input('Would you like to make another song')



