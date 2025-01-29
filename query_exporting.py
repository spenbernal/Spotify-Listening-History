import psycopg2
import pandas as pd
import queries

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='Spotifydb', 
    user='SpencerBernal',
    password='Maryland2003'
    )

for idx, query in enumerate(queries.query):
    df = pd.read_sql(query, conn)
    df.to_csv(f'query_{idx+1}_result.csv', mode= 'w',index= False)
    
conn.close()
    