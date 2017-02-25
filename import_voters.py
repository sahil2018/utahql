import csv
import pandas
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:password@127.0.0.1/database')

df = pandas.read_csv('voters.csv')
df = df.drop(df.columns[range(34, 93)], axis=1) # columns 35-93 are bunk
df.to_sql('voters', con=engine)

print 'Done'
