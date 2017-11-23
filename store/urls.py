from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add_product, name='add_product'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail_product, name='detail_product')
]