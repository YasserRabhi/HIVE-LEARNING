
import pandas as pd
df = pd.read_csv('nyc-flights.csv')
df.to_parquet('nyc-flights.parquet')
