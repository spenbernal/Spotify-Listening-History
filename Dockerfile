FROM postgres:latest

ENV POSTGRES_USER=SpencerBernal
ENV POSTGRES_PASSWORD=Maryland2003
ENV POSTGRES_DB=Spotifydb

COPY spotify_top_tracks.csv /docker-entrypoint-initdb.d/
COPY spotify_top_featured_artists.csv /docker-entrypoint-initdb.d/
COPY spotify_top_artists.csv /docker-entrypoint-initdb.d/

COPY init.sql /docker-entrypoint-initdb.d/