from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context_process = {
        'result': result,
        'a': a,
        'b': b,
    }
    return render(request,
                  'requestsdataapp/request-query-params.html',
                  context=context_process)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestsdataapp/user-bio-form.html')


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        if fs.size(filename) > 1048576:
            fs.delete(filename)
            print('Deleted file >>>', myfile.name)
            return HttpResponse(f'<b>Error file size</b>\n'
                                f'<p>File bigger than max size(1mb)</p>')

    return render(request, 'requestsdataapp/file-upload.html')