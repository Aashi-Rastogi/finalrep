from django.conf.urls import url
from registration import views as reg_views
urlpatterns = [
         url(r'^index/', reg_views.index),
    url(r'^update/', reg_views.update),
    url(r'^delete/', reg_views.delete),
]