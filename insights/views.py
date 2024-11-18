from rest_framework import viewsets
from django_filters import rest_framework as filters
from insights.models import EnergyInsight
from .serializers import EnergyInsightSerializer

class EnergyInsightFilter(filters.FilterSet):
    intensity = filters.NumberFilter()
    likelihood = filters.NumberFilter()
    relevance = filters.NumberFilter()
    year = filters.NumberFilter(field_name='end_year')
    country = filters.CharFilter(lookup_expr='icontains')
    topics = filters.CharFilter(field_name='topic', lookup_expr='icontains')
    region = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EnergyInsight
        fields = ['intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region']

class EnergyInsightViewSet(viewsets.ModelViewSet):
    queryset = EnergyInsight.objects.all()
    serializer_class = EnergyInsightSerializer
    filterset_class = EnergyInsightFilter