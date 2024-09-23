from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError


class UserBioForms(forms.Form):
    name = forms.CharField(max_length=10)
    age = forms.IntegerField(label='Your age', min_value=16, max_value=60)
    bio = forms.CharField(label='Biography', widget=forms.Textarea)


def validate_file_name(file: InMemoryUploadedFile) -> None:
    if file.name and 'virus' in file.name:
        raise ValidationError('file name should not contain "virus"')

class UploadFileForm(forms.Form):
    file = forms.FileField()