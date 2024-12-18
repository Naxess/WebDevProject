import os
import re
import django
import pandas
import pathlib
import datetime
import sqlalchemy
import urllib.error

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ten.settings')
django.setup()

DATABASE_NAME = 'stock_data.sqlite3'
DATABASE_PATH = os.path.join(pathlib.Path(__file__).resolve().parent, DATABASE_NAME)
SQLITE_URI = f'sqlite:///{DATABASE_PATH}'
SQL_ENGINE = sqlalchemy.create_engine(SQLITE_URI)


def print_stock_data_from_sql():
    print("print_stock_data_from_sql() initiated")
    with SQL_ENGINE.connect() as sql_connection:
        # Retrieve list of tables
        get_tables_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"'
        table_list = [row.name for row in sql_connection.execute(sqlalchemy.text(get_tables_query))]
        print(table_list)

        for ticker in table_list:
            print(f'{ticker}'.center(10, '-'))
            print(pandas.read_sql_table(ticker, sql_connection))
    print("print_stock_data_from_sql() concluded")


def download_stock_data_to_sql(*tickers):
    print("download_stock_data_to_sql() initiated")
    with SQL_ENGINE.connect() as sql_connection:
        # Downloads CSV data and uses it to update each SQL table
        invalid_tickers_list = []
        for ticker in tickers:
            # Filters out any supplied tickers that contain numbers
            if not bool(re.match('^[A-Z]+$', str(ticker).upper())):
                invalid_tickers_list.append(ticker)
                continue
            try:
                url_csv_to_df = pandas.read_csv((
                    f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=0"
                    f"&period2=9999999999&interval=1d&events=history&includeAdjustedClose=true"
                ))
                if not url_csv_to_df.empty:
                    url_csv_to_df.to_sql(ticker, sql_connection, if_exists='replace')
            except urllib.error.HTTPError:
                invalid_tickers_list.append(ticker)
                continue
    if invalid_tickers_list:
        print(f'Invalid tickers: {invalid_tickers_list}')
    print("download_stock_data_to_sql() concluded")


def update_existing_stock_data():
    print("update_existing_stock_data() initiated")
    with SQL_ENGINE.connect() as sql_connection:
        # Retrieve list of tables from SQL database
        get_tables_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"'
        table_list = [row.name for row in sql_connection.execute(sqlalchemy.text(get_tables_query))]

        if not table_list:
            # table_list = ['RDDT']
            return

        # Downloads CSV data and uses it to update each SQL table
        for ticker in table_list:
            url_csv_to_df = pandas.read_csv((
                f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=0"
                f"&period2=9999999999&interval=1d&events=history&includeAdjustedClose=true"
            ))
            if not url_csv_to_df.empty:
                url_csv_to_df.to_sql(ticker, SQL_ENGINE, if_exists='replace')
    print("update_existing_stock_data() concluded")


def date_validation_and_reformatting(start_date=None, end_date=None):
    """
    Validates whether the provided start and end dates values are valid dates.
    Reformats dates to match the specified convention.

    start_date & end_date:
        Expected data type: str
        Expected format of value (yyyy-mm-dd): %Y-%m-%d
    """
    todays_date = datetime.date.today().strftime('%Y-%m-%d')
    if start_date:
        try:
            start_date_as_datetime = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            start_date = start_date_as_datetime.strftime('%Y-%m-%d')
            if start_date > todays_date:
                start_date = None
        except (ValueError, Exception) as e:
            print(f'Supplied start date produced an error: "{e}". Excluding start date from range.')
            start_date = None
    if end_date:
        try:
            end_date_as_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            end_date = end_date_as_datetime.strftime('%Y-%m-%d')
            if end_date > todays_date:
                end_date = todays_date
        except (ValueError, Exception) as e:
            print(f'Supplied start date produced an error: "{e}". Excluding start date from range.')
            end_date = None
    if start_date and end_date and (start_date > end_date):
        print(f'{start_date} is later than {end_date}')
        start_date, end_date = None, None
    return start_date, end_date


def retrieve_stock_data_from_sql(*tickers, start_date=None, end_date=None):
    """
    tickers:
        Expected data types of elements: str
    start_date & end_date:
        Expected data type: str
        Expected format of value (yyyy-mm-dd): %Y-%m-%d
    """
    print("retrieve_stock_data_from_sql() initiated")

    # Verify if dates are valid
    if start_date or end_date:
        start_date, end_date = date_validation_and_reformatting(start_date, end_date)

    stock_data_dict = {}
    with SQL_ENGINE.connect() as sql_connection:
        # Retrieve list of tables
        get_tables_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"'
        table_list = [row.name for row in sql_connection.execute(sqlalchemy.text(get_tables_query))]

        if not table_list:
            return None

        if tickers:
            existing_tables_list = []
            nonexisting_tables_list = []

            for ticker in tickers:
                existing_tables_list.append(ticker) if ticker in table_list else nonexisting_tables_list.append(ticker)
            table_list = existing_tables_list

            if nonexisting_tables_list:
                print(f'No stock data for these tickers in our database: {nonexisting_tables_list}')

        for ticker in table_list:
            # Returns a dataframe containing the contents of the SQL table
            stock_data_dataframe = pandas.read_sql_table(ticker, sql_connection)

            # Filter the dataframe by the start/end dates, if provided
            if start_date and not end_date:
                stock_data_dataframe = stock_data_dataframe.loc[(stock_data_dataframe['Date'] >= start_date)]
            elif not start_date and end_date:
                stock_data_dataframe = stock_data_dataframe.loc[(stock_data_dataframe['Date'] <= end_date)]
            elif start_date and end_date:
                stock_data_dataframe = stock_data_dataframe.loc[
                    (stock_data_dataframe['Date'] >= start_date) & (stock_data_dataframe['Date'] <= end_date)]

            stock_data_dict[ticker] = stock_data_dataframe
    print("retrieve_stock_data_from_sql() concluded")
    return table_list, stock_data_dict


def purge_sql_database(*tickers):
    print('purge_sql_database() initiated')
    with SQL_ENGINE.connect() as sql_connection:
        get_tables_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"'
        table_list = [row.name for row in sql_connection.execute(sqlalchemy.text(get_tables_query))]

        if tickers:
            existing_tickers_list = []
            nonexisting_tickers_list = []
            for ticker in tickers:
                ticker = str(ticker).upper()
                if ticker not in table_list:
                    nonexisting_tickers_list.append(ticker)
                else:
                    existing_tickers_list.append(ticker)
            print(f'No data for tickers: {nonexisting_tickers_list}')
            table_list = existing_tickers_list

        for ticker in table_list:
            drop_table_query = f'DROP TABLE {ticker}'
            sql_connection.execute(sqlalchemy.text(drop_table_query))
    print('purge_sql_database() concluded')


def get_ticker_list_from_sql():
    with SQL_ENGINE.connect() as sql_connection:
        # Retrieve list of tables from SQL database
        get_tables_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"'
        table_list = [row.name for row in sql_connection.execute(sqlalchemy.text(get_tables_query))]
    return sorted(table_list)


if __name__ == '__main__':
    # Columns: index, Date, Open, High, Low, Close, Adj Close, Volume
    print("stock_data_manage.py initiated")
    # download_stock_data_to_sql('RDDT', 'INTJ', 'BOLD')
    # download_stock_data_to_sql()
    # download_stock_data_to_sql('39jfa4', 'aad3', 'ZGA', 'ZG')
    update_existing_stock_data()
    # print(retrieve_stock_data_from_sql('BOLD', 'CAVA'))
    # print(retrieve_stock_data_from_sql('A3FA3', 'CAVA'))
    # purge_sql_database('rddt')
    # purge_sql_database()
    # print(get_ticker_list_from_sql())
    # print_stock_data_from_sql()
    print("stock_data_manage.py concluded")
