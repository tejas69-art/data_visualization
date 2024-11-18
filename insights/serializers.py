from rest_framework import serializers
from insights.models import EnergyInsight

class EnergyInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyInsight
        fields = ['intensity', 'likelihood', 'relevance', 'end_year', 'country', 'topic', 'region']