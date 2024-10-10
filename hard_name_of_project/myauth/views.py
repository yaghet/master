from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile


# View для регистрации нового пользователя
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)

        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


# View для просмотра информации о пользователе
class AboutMyView(TemplateView):
    template_name = 'myauth/about-me.html'


# View для перенаправления пользователя после Logout
class MyLogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('myauth:login')

# View для установки данных в cookies пользователя
def set_cookie_view(request: HttpRequest) -> HttpResponse:
     response = HttpResponse('Cookie set')
     response.set_cookie('feez', 'bee', max_age=3600)
     return response


# View для чтения данных из cookies пользователя
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('feez', 'default_value')
    return HttpResponse(f'Cookie value {value!r}')


# View для установки данных в session пользователя
def set_session_view(request) -> HttpResponse:
    request.session['foobar'] = 'info of session'
    return HttpResponse('Session set')


# View для чтения данных из session пользователя
def get_session_view(request) -> HttpResponse:
     value = request.session.get('foobar', 'default')
     return HttpResponse(f'Session value {value!r}')


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"one": "True", "zero": "False"})