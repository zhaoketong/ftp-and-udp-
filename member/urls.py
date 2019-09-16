from member import views
from django.conf.urls import url

urlpatterns = [
    url(r'^reg$',views.reg),
    url(r'^info$',views.info),
    url(r'^rech$',views.rech),
    url(r'^rech_server$',views.rech_server),
    url(r'^consume$',views.consume),
    url(r'^consume_server$',views.consume_server),
    url(r'^rech_record$',views.rech_record),
    url(r'^con_record$',views.con_record),
    url(r'^member_list$',views.member_list),
]








