from django.contrib import admin
from django.db.models import Q
from .models import EnergyInsight

class DropdownFilter(admin.SimpleListFilter):
    template = 'admin/dropdown_filter.html'

class EndYearFilter(DropdownFilter):
    title = 'End Year'
    parameter_name = 'end_year'

    def lookups(self, request, model_admin):
        years = EnergyInsight.objects.values_list('end_year', flat=True).distinct().order_by('end_year')
        return [(str(year), str(year)) for year in years if year]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(end_year=self.value())

class TopicFilter(DropdownFilter):
    title = 'Topic'
    parameter_name = 'topic'

    def lookups(self, request, model_admin):
        topics = EnergyInsight.objects.values_list('topic', flat=True).distinct().order_by('topic')
        return [(topic, topic) for topic in topics if topic]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(topic__icontains=self.value())

class SectorFilter(DropdownFilter):
    title = 'Sector'
    parameter_name = 'sector'

    def lookups(self, request, model_admin):
        sectors = EnergyInsight.objects.values_list('sector', flat=True).distinct().order_by('sector')
        return [(sector, sector) for sector in sectors if sector]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(sector=self.value())

class RegionFilter(DropdownFilter):
    title = 'Region'
    parameter_name = 'region'

    def lookups(self, request, model_admin):
        regions = EnergyInsight.objects.values_list('region', flat=True).distinct().order_by('region')
        return [(region, region) for region in regions if region]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(region=self.value())

class PestleFilter(DropdownFilter):
    title = 'PESTLE'
    parameter_name = 'pestle'

    def lookups(self, request, model_admin):
        pestles = EnergyInsight.objects.values_list('pestle', flat=True).distinct().order_by('pestle')
        return [(pestle, pestle) for pestle in pestles if pestle]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(pestle=self.value())

class SourceFilter(DropdownFilter):
    title = 'Source'
    parameter_name = 'source'

    def lookups(self, request, model_admin):
        sources = EnergyInsight.objects.values_list('source', flat=True).distinct().order_by('source')
        return [(source, source) for source in sources if source]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(source=self.value())

class CountryFilter(DropdownFilter):
    title = 'Country'
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        countries = EnergyInsight.objects.values_list('country', flat=True).distinct().order_by('country')
        return [(country, country) for country in countries if country]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country=self.value())

class EnergyInsightAdmin(admin.ModelAdmin):
    list_filter = (
        EndYearFilter,
        TopicFilter,
        SectorFilter,
        RegionFilter,
        PestleFilter,
        SourceFilter,
        CountryFilter,
    )

admin.site.register(EnergyInsight, EnergyInsightAdmin)