from django.conf.urls import include,url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',views.home,name='student_home'),
    url(r'^list_json/$', login_required(views.student_list_json.as_view()), name="student_list_json"),
    url(r'^home/$',views.home_json,name='student_home_json'),
    url(r'^freelancer/$',views.home_freelancer,name='student_home_freelancer'),
    url(r'^new/$', views.student_new, name='student_new'),
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^(?P<pk>\d+)/remove$', views.student_remove, name='student_remove'),
    url(r'^(?P<pk>\d+)/edit$', views.student_edit, name='student_edit'),
    url(r'^list_json/$', login_required(views.student_list_json.as_view()), name="student_list_json"),
]