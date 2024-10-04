from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, HttpResponse
from django.views import View


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