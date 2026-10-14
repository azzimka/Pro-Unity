from django.urls import path
from .views import index, register, view_data, category_detail

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('view-data/', view_data, name='view_data'),
    path('category/<slug:slug>/', category_detail, name='category_detail_url'),
]
