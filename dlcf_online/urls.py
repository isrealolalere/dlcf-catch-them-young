from unicodedata import name
from django.urls import path
from dlcf_online import views

urlpatterns = [
    path('', views.index, name='home'),
    path('freshers', views.all_freshers, name='freshers'),
    path('update/<int:id>', views.update, name='update-fresher'),
    path('fresher-info/<int:id>', views.fresher_info, name='fresher-info'),
    path('search', views.search, name='search'),
]