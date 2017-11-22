from django.conf.urls import url, include
from .views import do_search, all_products




urlpatterns= [
    url(r'^$', all_products, name='all_products'),
    url(r'^search/', do_search, name='search'),
]



