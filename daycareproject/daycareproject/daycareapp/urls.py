from django.conf.urls import url

from . import views

from .views import EducatorList, ClassDetail, AboutView, educator_list

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^<int:educator_id>/$', views.find_educator, name='detail'),# ex: /educator/5/
    url('^educatorlist/$', EducatorList.as_view(), name='educators'),
    url('^educators/$', educator_list, name='educator'),
    url('^class/$', ClassDetail.as_view(), name='class'),
    url('^about/$', AboutView.as_view()),

]