from django.urls import path
from users.views import PaymentsListView

app_name = 'users'

urlpatterns = [
    path("payments/", PaymentsListView.as_view(), name='paymentsList'),
]