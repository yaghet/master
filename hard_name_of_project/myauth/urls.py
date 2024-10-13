from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    get_cookie_view,
    set_cookie_view,
    get_session_view,
    set_session_view,
    MyLogoutPage,
    AboutMyView,
    RegisterView,
    FooBarView,
    UpdateAvatarView,
    ListUsersView,
    UserDetailView,
)

app_name = 'myauth'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='myauth/login.html',
             redirect_authenticated_user=True,
         ),
         name='login',
    ),
    path('logout/', MyLogoutPage.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about-me/', AboutMyView.as_view(), name='about-me'),
    path('avatar-update/<int:pk>/', UpdateAvatarView.as_view(), name='avatar-update'),

    path('list-users/', ListUsersView.as_view(), name='list-users'),
    path('user-detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('cookie/get/', get_cookie_view, name='cookie-get'),
    path('cookie/set/', set_cookie_view, name='cookie-set'),

    path('session/get/', get_session_view, name='session-get'),
    path('session/set/', set_session_view, name='session-set'),

    path('foobar', FooBarView.as_view(), name='foobar')
]
