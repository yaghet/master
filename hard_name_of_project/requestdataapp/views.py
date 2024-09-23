from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserBioForms, UploadFileForm


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
    context_form = {
        'form': UserBioForms(),
    }
    return render(request, 'requestsdataapp/user-bio-form.html', context=context_form)


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            my_file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)

            if fs.size(filename) > 1048576:
                fs.delete(filename)
                print('Deleted file >>>', my_file.name)
                return HttpResponse(f'<b>Error file size</b>\n'
                                    f'<p>File bigger than max size(1mb)</p>')
    else:
        form = UploadFileForm()
    context_file = {
        'form': form,
    }
    return render(request, 'requestsdataapp/file-upload.html', context=context_file)