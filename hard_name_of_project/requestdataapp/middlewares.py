from django.http import HttpRequest, HttpResponse
import time

def set_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0
        self.response_count = 0
        self.exceptions_count = 0
        self.ip_requests = {}
        self.start = 0

    def __call__(self, request: HttpRequest):
        ip = request.META['REMOTE_ADDR']

        '''Реализация 2 задачи: Если нет ip адреса в словаре, то добавляется ip в словарь и далее
        прибавляется значение к нему при каждом вызове страницы(но не более 10) + сохраняется время первого
        вызова страницы
        Если разница более 60 секунд, очищается словарь и время первого вызова( страница снова доступна!) ) 
        '''

        if ip not in self.ip_requests:
            self.ip_requests[ip] = 1
            self.start = time.time()

        else:
            self.ip_requests[ip] += 1

            if (self.ip_requests[ip] > 10) and (time.time() - self.start < 60):
                return HttpResponse(f'<h1>Sorry, this page is not available now</h1>\n'
                                    f'Too many request')
            elif time.time() - self.start > 60:
                self.ip_requests.clear()
                self.start = 0


        self.request_count += 1
        print('Count request: ', self.response_count)

        response = self.get_response(request)
        self.response_count += 1
        print('Count response', self.response_count)

        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('Exception count', self.exceptions_count)
