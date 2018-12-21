from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from .views import Container_types,Extrafield_instance,Container_types_instance,Adduser,Extrafield_operations,Relationship_view,RuntimeR	

urlpatterns=[
url(r'^user/',csrf_exempt(Adduser.as_view()),name='add_get_user'),
url(r'^container-types/',csrf_exempt(Container_types.as_view()),name='container_types'),
url(r'^extra-fields/(?P<ct_id>\d+)',csrf_exempt(Extrafield_instance.as_view()),name='container_updation'),
url(r'^extra-fields/',csrf_exempt(Extrafield_instance.as_view()),name='extra_field_updation'),
url(r'^container-instances/container-type/(?P<ct_id>\d+)',csrf_exempt(Container_types_instance.as_view()),name='container_types'),
url(r'^container-instances/(?P<ci_id>\d+)',csrf_exempt(Container_types_instance.as_view()),name='container_types'),
url(r'^search-by-ef/',csrf_exempt(Extrafield_operations.as_view()),name='add_get_user'),
url(r'^relation/',csrf_exempt(Relationship_view.as_view()),name='relation_establish'),
#url(r'^relation/',csrf_exempt(Relationship_view.as_view()),name='relation_update'),
url(r'^container-relation-instances/(?P<ci_id>\d+)',csrf_exempt(RuntimeR.as_view()),name='container_instance'),



]