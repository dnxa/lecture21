from .views  import all_authors_view, top_3_view, classics_view
from django.urls import path

urlpatterns = [
    path('', all_authors_view),
    path('top3/', top_3_view, name = 'top_3_view'),
    path('classics/', classics_view, name = 'classics_view'),
]