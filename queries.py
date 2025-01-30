query = [None for i in range(5)]

#Query 1: Show top 10 listened to songs, with their track name, 
# artist, popularity, corresponding album, genre, and time length 
query[0] = '''
            WITH tracks_in_time AS (
                SELECT track, (duration / 60000) AS minutes, ((duration % 60000) / 1000) AS seconds
                FROM top_tracks
                LIMIT 10
            ),
            artists_and_tracks AS(
                SELECT tt.track, tt.artist, tt.popularity, tt.album, ta.genre
                FROM top_tracks tt JOIN top_artists ta ON ta.artist = tt.artist
                LIMIT 10
            ) 
            SELECT aat.track, aat.artist, aat.popularity, 
            aat.album, aat.genre, CONCAT(tit.minutes, ':', LPAD(tit.seconds::TEXT, 2, '0')) AS length
            FROM artists_and_tracks aat 
            JOIN tracks_in_time tit ON aat.track = tit.track;
            '''
            
#Query 2: Display percentages of my top genres from my top tracks
query[1] = '''
            WITH total_tracks AS (
                SELECT COUNT(*) AS total_count
                FROM top_tracks tt JOIN top_artists ta ON tt.artist = ta.artist
            )
            SELECT ta.genre, COUNT(*) AS artist_count_per_genre, ROUND(COUNT(*) * 100.0 / (SELECT total_count FROM total_tracks), 2) as genre_percentage
            FROM top_tracks tt JOIN top_artists ta ON tt.artist = ta.artist
            GROUP BY ta.genre
            ORDER BY genre_percentage DESC;
            '''
            
#Query 3: Display percentages of top genres from my top artists
query[2] = '''
            WITH length_of_top_artists AS (
                SELECT COUNT(*) AS total_count
                FROM top_artists
            )
            SELECT genre, COUNT(*) AS artist_count_per_genre,ROUND(COUNT(*) * 100.0 / (SELECT total_count FROM length_of_top_artists), 2) as genre_percentage
            FROM top_artists
            GROUP BY genre
            ORDER BY genre_percentage DESC;
            '''

#Query 4: Display most listened to artists from top 
# tracks and display number of songs listened to by them 
query[3] = '''
            SELECT tt.artist, ta.genre, ta.followers,
            COUNT(*) AS track_count, 
            RANK() OVER (ORDER BY COUNT(*) DESC, tt.artist) AS rank
            FROM top_tracks tt JOIN top_artists ta ON tt.artist = ta.artist
            GROUP BY tt.artist, ta.genre, ta.followers
            ORDER BY track_count DESC, tt.artist
            LIMIT 10;
            '''

#Query 5: Show the 10 most listened to artists including featured artists, 
# amount of total songs they have, and their follower count
query[4] = '''
            WITH all_artists AS (
                SELECT artist, track 
                FROM top_tracks
                UNION ALL
                SELECT artist, track 
                FROM featured_artists
            )
            SELECT aa.artist, ta.followers, COUNT(*) AS track_count, 
            RANK() OVER (ORDER BY COUNT(*) DESC, aa.artist) AS rank
            FROM all_artists aa LEFT OUTER JOIN top_artists ta ON aa.artist = ta.artist
            GROUP BY aa.artist, ta.followers
            ORDER BY track_count DESC, aa.artist
            LIMIT 10;
            '''