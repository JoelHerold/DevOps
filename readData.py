import streamlit as st
import sqlalchemy as db
import pandas as pd

# load data from MySQL //  https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91


hostname = "127.0.0.1"
dbname = "python"
uname = "root"
pwd = "12345678"

# Create SQLAlchemy engine to connect to MySQL Database
engine = db.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                          .format(host=hostname, db=dbname, user=uname, pw=pwd))

connection = engine.connect()

# https://thinkingneuron.com/reading-data-from-mysql-database-in-python/

df = pd.read_sql('SELECT * FROM financial_data', con=connection)

print(df.head())

st.write("""
helllo
o
""")

df_line_chart = df

x = st.slider('Percentage')

st.line_chart(df[['Sales($)', 'Profit($)', 'Discounts($)']].head(int(len(df) * (x / 100))))


st.table(df[['Sales($)', 'Profit($)', 'Discounts($)']].head(int(len(df) * (x / 100))).sum())

if x > 0:
    st.table(df[['Sales($)', 'Profit($)', 'Discounts($)']].head(int(len(df) * (x / 100))).describe())

# Visualize
