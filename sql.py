import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='Spotifydb', 
    user='SpencerBernal',
    password='Maryland2003')

cur = conn.cursor()

cur.execute('DELETE FROM featured_artists')
cur.execute('DELETE FROM top_artists')
cur.execute('DELETE FROM top_tracks')

with open('spotify_top_artists.csv', 'r') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        row = row[1:]
        cur.execute('''
                INSERT INTO top_artists (subgenre, artist_id, artist, popularity, followers, genre)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', tuple(row))
        
with open('spotify_top_tracks.csv', 'r') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        row = row = row[1:]
        cur.execute('''
                INSERT INTO top_tracks (duration, explicit, track_id, track, 
                popularity, album, album_release_date, album_total_tracks, artist, 
                artist_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', tuple(row))


with open('spotify_top_featured_artists.csv', 'r') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        row = row[1:]
        cur.execute('''
                    INSERT INTO featured_artists (track_id, track, artist, artist_id)
                    VALUES (%s, %s, %s, %s)
                    ''', tuple(row))

conn.commit()
cur.close()
conn.close()