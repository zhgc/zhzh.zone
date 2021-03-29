
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'), # 怎么说呢，感觉自己是不是被二手教材耽误了，这个写法...
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
