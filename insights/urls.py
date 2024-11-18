from django.urls import path
from . import views

urlpatterns = [
    path('insights/', views.EnergyInsightList.as_view(), name='insight-list'),
]
