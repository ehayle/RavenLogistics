# listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings_index, name="listings_index"),
    path("post/<int:pk>/", views.listings_detail, name="listings_detail"),
    path("category/<category>/", views.listings_category, name="listings_category"),
]