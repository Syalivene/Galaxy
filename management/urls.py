from django.urls import path
from .import views

app_name = 'management'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('synthetic_report/', views.synthetic_report, name='synthetic_report'),
    path('accounts/', views.accounts, name='accounts'),
    path('new_finance/', views.new_finance, name='new_finance'),
    path('finances_outputs/', views.finances_outputs, name='finances_outputs'),
    path('finances_inputs/', views.finances_inputs, name='finances_inputs'),
    path('accounts_balance/', views.accounts_balance, name='accounts_balance'),
    path('accounts/<int:pk>/', views.account_details, name='account_details'),
    path('transaction/<int:pk>/', views.transaction_details, name='transaction_details'),
]
