from django.conf.urls import url
from users import views
urlpatterns = [
    url(r'^home$',views.home),
    url(r'^register$',views.register),
    url(r'^register_server/$',views.register_server),
    url(r'^login$',views.login),
    url(r'^index$',views.index),
    url(r'^logout$',views.logout)
]






















