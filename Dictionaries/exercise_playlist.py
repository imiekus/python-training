playlist = {
    'title': 'Some songs to listen',
    'author': 'Jan Kowalski',
    'songs':  [
        {'title': 'Happy Song', 'artist': ['Happy Artist'], 'duration': 2.5},
        {'title': 'Sad Song', 'artist': ['Sad Artist', 'Depressed Ardist'], 'duration': 3.5},
        {'title': 'Neutral Song', 'artist': ['Normal Artist'], 'duration': 4.5},
        {'title': 'Calming Song', 'artist': ['Calm Artist', 'Sleepy Artist'], 'duration': 2.5},
        {'title': 'Depressing Song', 'artist': ['Depressed Artist', 'Sad Artist'], 'duration': 5.5}
    ]
    }

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)