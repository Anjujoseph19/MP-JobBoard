import django_filters
from job.models import Job
from company.models import Company

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title']

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = ['state']