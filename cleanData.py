import pandas as pd

df = pd.read_csv("FinancialSample.csv", sep=";")

# remove whitespaces in header
df.columns = df.columns.str.replace(' ', '')
"""
def is_currency(pandas_column):
    for index in pandas_column:
        index.replace('.', '')
        index.replace(' ', '')

    return pandas_column


def is_text(pandas_column):
    return True


def is_date(pandas_column):
    pd.to_datetime(pandas_column, format='%d.%m.%Y')


#is_date(df['Date'])
#is_currency(df['GrossSales'])

"""


def is_date(dataframe_column):
    return pd.to_datetime(dataframe_column, format='%d.%m.%Y')

def to_float(dataframe_column):
    return dataframe_column.str.replace(',','.')


def is_currency(dataframe_column):
    #if dataframe_column.str[2] == "-":
    #    print("test")


    dataframe_column = dataframe_column.str.replace('-', '0')
    dataframe_column = dataframe_column.str.replace(' ', '')
    dataframe_column = dataframe_column.str.replace('(', '')
    dataframe_column = dataframe_column.str.replace(')', '')
    dataframe_column = dataframe_column.str.replace('.', '')
    dataframe_column = dataframe_column.str.replace(',', '.')
    dataframe_column = dataframe_column.str.replace('$', '')
    return dataframe_column


def is_currency_change_name():
    # print(df.columns.values.tolist())
    temp_list = df.columns.values.tolist()
    for index in range(5, 12):
        temp_list[index] = str(temp_list[index]) + "($)"

    df.columns = temp_list


#transform all currency columns
df['GrossSales'] = is_currency(df['GrossSales'])
df['Discounts'] = is_currency(df['Discounts'])
df['ManufacturingPrice'] = is_currency(df['ManufacturingPrice'])
df['SalePrice'] = is_currency(df['SalePrice'])
df['Sales'] = is_currency(df['Sales'])
df['COGS'] = is_currency(df['COGS'])
df['Profit'] = is_currency(df['Profit'])

#safe the currency in the header instead in every row
is_currency_change_name()

#transform units sold to floats
df['UnitsSold']= to_float(df['UnitsSold'])

#change to datime object
df['Date']=is_date(df['Date'])

print(df['Date'])

df.to_csv("cleaned_data.csv")
