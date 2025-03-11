from django.urls import path

from myapiapp import views

urlpatterns = [
    path('groups/', views.GroupsListView.as_view()),
]
