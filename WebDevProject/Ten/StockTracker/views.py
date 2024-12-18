import re
import datetime
import stock_data_management
from django.shortcuts import render
from StockTracker.forms import StockDataForm, DownloadStockDataForm


# Create your views here.
def stock_app_home_view(request):
    return render(request, 'StockTracker/stock_app_home.html')


def stock_historical_visualizer_view(request):
    ticker_one = None
    ticker_two = None
    ticker_three = None
    start_date = None  # (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = None
    tickers_list = []
    download_ticker_list = None

    if request.method == "POST":
        stock_data_form = StockDataForm(request.POST)
        download_stock_data_form = DownloadStockDataForm(request.POST)

        if stock_data_form.is_valid() and download_stock_data_form.is_valid():
            stock_data_form_data = stock_data_form.cleaned_data
            download_stock_data_form_data = download_stock_data_form.cleaned_data

            download_ticker_list = re.sub(r'[^a-zA-Z0-9,]', '',
                                          str(download_stock_data_form_data['download_ticker_list']).upper()).split(',')

            ticker_one = re.sub(r'[^a-zA-Z0-9,]', '', str(stock_data_form_data['ticker_one']).upper())
            ticker_two = re.sub(r'[^a-zA-Z0-9,]', '', str(stock_data_form_data['ticker_two']).upper())
            ticker_three = re.sub(r'[^a-zA-Z0-9,]', '', str(stock_data_form_data['ticker_three']).upper())

            try:
                start_date = datetime.datetime.strftime(stock_data_form_data['start_date'], '%Y-%m-%d')
            except (ValueError, Exception) as e:
                start_date = None
            try:
                end_date = datetime.datetime.strftime(stock_data_form_data['end_date'], '%Y-%m-%d')
            except (ValueError, Exception) as e:
                end_date = None

            if start_date or end_date:
                start_date, end_date = stock_data_management.date_validation_and_reformatting(start_date, end_date)
        else:
            print(stock_data_form.errors)
    else:
        stock_data_form = StockDataForm()

    context = {'stock_data_form': stock_data_form, 'download_stock_data_form': DownloadStockDataForm()}

    if download_ticker_list:
        print(f'Tickers pending evaluation: {download_ticker_list}')
        parsed_download_ticker_list = []
        for ticker in download_ticker_list:
            if len(ticker):
                parsed_download_ticker_list.append(str(ticker).strip(' '))
        if parsed_download_ticker_list:
            print(f'Downloading data for tickers: {parsed_download_ticker_list}')
            stock_data_management.download_stock_data_to_sql(*download_ticker_list)
            # return HttpResponseRedirect('/stock_app/stockcharts/')

    for ticker in [ticker_one, ticker_two, ticker_three]:
        if ticker:
            tickers_list.append(ticker)

    if tickers_list:
        verified_table_list, stock_data_dict = stock_data_management.retrieve_stock_data_from_sql(*tickers_list,
                                                                                                  start_date=start_date,
                                                                                                  end_date=end_date)

        # Available columns: index, Date, Open, High, Low, Close, Adj Close, Volume
        if verified_table_list:
            if ticker_one in verified_table_list:
                ticker_one_data = stock_data_dict[ticker_one]
                ticker_one_dict = {
                    'ticker_one_name': ticker_one.upper(),
                    "ticker_one_dates": ticker_one_data['Date'].values.tolist(),
                    "ticker_one_opens": ticker_one_data['Open'].values.tolist(),
                    "ticker_one_closes": ticker_one_data['Close'].values.tolist(),
                    "ticker_one_adj_closes": ticker_one_data['Adj Close'].values.tolist(),
                    "ticker_one_volumes": ticker_one_data['Volume'].values.tolist()
                }
                context.update(ticker_one_dict)

            if ticker_two in verified_table_list:
                ticker_two_data = stock_data_dict[ticker_two]
                ticker_two_dict = {
                    'ticker_two_name': ticker_two.upper(),
                    "ticker_two_dates": ticker_two_data['Date'].values.tolist(),
                    "ticker_two_opens": ticker_two_data['Open'].values.tolist(),
                    "ticker_two_closes": ticker_two_data['Close'].values.tolist(),
                    "ticker_two_adj_closes": ticker_two_data['Adj Close'].values.tolist(),
                    "ticker_two_volumes": ticker_two_data['Volume'].values.tolist()
                }
                context.update(ticker_two_dict)

            if ticker_three in verified_table_list:
                ticker_three_data = stock_data_dict[ticker_three]
                ticker_three_dict = {
                    'ticker_three_name': ticker_three.upper(),
                    "ticker_three_dates": ticker_three_data['Date'].values.tolist(),
                    "ticker_three_opens": ticker_three_data['Open'].values.tolist(),
                    "ticker_three_closes": ticker_three_data['Close'].values.tolist(),
                    "ticker_three_adj_closes": ticker_three_data['Adj Close'].values.tolist(),
                    "ticker_three_volumes": ticker_three_data['Volume'].values.tolist()
                }
                context.update(ticker_three_dict)

    return render(request, 'StockTracker/stock_history.html', context)
