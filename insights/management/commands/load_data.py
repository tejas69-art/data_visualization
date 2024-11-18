from django.core.management.base import BaseCommand
from insights.models import EnergyInsight
import json

class Command(BaseCommand):
    help = 'Load data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                intensity = entry.get('intensity', None)
                likelihood = entry.get('likelihood',None)
                relevance = entry.get('relevance',None)
                if isinstance(intensity, str) and not intensity.isdigit():
                    intensity = 0  
                if not intensity:
                    intensity = 0
                if isinstance(likelihood, str) and not likelihood.isdigit():
                    likelihood = 0  
                if not likelihood:
                    likelihood = 0
                if isinstance(relevance, str) and not relevance.isdigit():
                    relevance = 0  
                if not relevance:
                    relevance = 0
                EnergyInsight.objects.create(
                    end_year=entry.get('end_year', ''),
                    intensity=intensity,
                    sector=entry['sector'],
                    topic=entry['topic'],
                    insight=entry['insight'],
                    url=entry['url'],
                    region=entry['region'],
                    start_year=entry.get('start_year', ''),
                    impact=entry.get('impact', ''),
                    added=entry['added'],
                    published=entry['published'],
                    country=entry['country'],
                    relevance=relevance,
                    pestle=entry['pestle'],
                    source=entry['source'],
                    title=entry['title'],
                    likelihood=likelihood
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
