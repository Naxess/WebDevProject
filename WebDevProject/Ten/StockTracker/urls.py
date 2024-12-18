from django.urls import path
from StockTracker import views

app_name = 'stockapp'

urlpatterns = [
    path('', views.stock_app_home_view, name='stock_app_home'),
    path('stock_history', views.stock_historical_visualizer_view, name='stock_history'),
]
