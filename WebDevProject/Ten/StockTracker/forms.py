from django import forms
from stock_data_management import get_ticker_list_from_sql


class DownloadStockDataForm(forms.Form):
    download_ticker_list = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter ticker symbol(s) here. Example: AMZN, AAPL, IBM'
    }))


def get_ticker_choices():
    ticker_choices = [(ticker, ticker) for ticker in get_ticker_list_from_sql()]
    ticker_choices.insert(0, (None, 'Click here to select a ticker'))
    return ticker_choices


class StockDataForm(forms.Form):
    ticker_one = forms.ChoiceField(required=False, choices=get_ticker_choices, widget=forms.Select(attrs={
        'class': 'form-select',
    }))

    ticker_two = forms.ChoiceField(required=False, choices=get_ticker_choices, widget=forms.Select(attrs={
        'class': 'form-select',
    }))

    ticker_three = forms.ChoiceField(required=False, choices=get_ticker_choices, widget=forms.Select(attrs={
        'class': 'form-select',
    }))

    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))

    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))
