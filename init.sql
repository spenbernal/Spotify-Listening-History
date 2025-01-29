CREATE TABLE top_tracks (
    duration INT,
    explicit BOOLEAN,
    track_id TEXT PRIMARY KEY,
    track TEXT,
    popularity INT, 
    album TEXT,
    album_release_date DATE,
    album_total_tracks INT,
    artist TEXT,
    artist_id TEXT
);

CREATE TABLE top_artists (
    subgenre TEXT, 
    artist_id TEXT PRIMARY KEY,
    artist TEXT,
    popularity INT,
    followers INT,
    genre TEXT
);

CREATE TABLE featured_artists (
    track_id TEXT,
    track TEXT,
    artist TEXT,
    artist_id TEXT,
    PRIMARY KEY (track_id, artist_id),
    FOREIGN KEY (track_id) REFERENCES top_tracks(track_id)
);