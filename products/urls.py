from django.conf.urls import url, include
from .views import do_search, all_products, product_detail




urlpatterns= [
    url(r'^$', all_products, name='all_products'),
    url(r'^search/', do_search, name='search'),
    url(r'^(\d+)$', product_detail, name="detail"),
]



