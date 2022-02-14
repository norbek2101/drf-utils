from django.urls import path
from apps.views import UtilView

urlpatterns = [
     path('utils/', UtilView.as_view(), name='get api'),
]