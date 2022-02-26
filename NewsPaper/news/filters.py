from django_filters import FilterSet, DateTimeFromToRangeFilter
from django_filters.widgets import DateRangeWidget, RangeWidget
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    dateCreation = DateTimeFromToRangeFilter(lookup_expr=(
        'icontains'), widget=RangeWidget(attrs={'type': 'datetime-local'}))


class Meta:
    model = Post
    # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
    fields = ('author', 'dateCreation', 'categoryType')