# reachengine/urls.py
from django.conf.urls import url
from reachengine import views
from django.urls import path

urlpatterns = [
	url('^$', views.HomePageView.as_view()),
	url('about.html', views.AboutPageView.as_view()),
	path('^$', views.get_hashtags, name="fetchHashTag"),
]