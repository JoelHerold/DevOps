# https://www.kaggle.com/datasets/chitwanmanchanda/fraudulent-transactions-data

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Date, DateTime, Float

"""

Load Data into Pandas Dataframe

"""

df = pd.read_csv("cleaned_data.csv")

"""

Push data into Database with SQL ALCHEMY

Insert your database credentials

"""

hostname = "127.0.0.1"
dbname = "python"
uname = "root"
pwd = "12345678"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table https://www.w3resource.com/pandas/dataframe/dataframe-to_sql.php
df.to_sql('financial_data', engine, index=False, if_exists='replace',
          dtype={'UnitsSold':Float,'ManufacturingPrice($)': Float, 'Date': Date, 'Profit($)': Float})
