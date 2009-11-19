import django_filters
from satchmo_store.shop.models import Order

class OrderFilterSet(django_filters.FilterSet):
    time_stamp = django_filters.DateRangeFilter()
    class Meta:
        model = Order
        fields = ['status', 'method', 'time_stamp']

    def __init__(self, *args, **kwargs):
        super(OrderFilterSet, self).__init__(*args, **kwargs)
        self.filters['status'].field.choices.insert(0, ('','All',))
        self.filters['method'].field.choices.insert(0, ('','All',))
