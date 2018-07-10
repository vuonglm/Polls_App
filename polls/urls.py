from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
	# /polls/
	url(r'^$', views.index, name = 'index'),	
	# /polls/5/
	url(r'^(?P<question_id>\d+)/$', views.detail, name = 'detail'),	
	# /polls/5/results/
	url(r'^(?P<question_id>\d+)/results/$', views.results, name = 'results'),	
	# polls/5/vote/
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name = 'vote'),
]