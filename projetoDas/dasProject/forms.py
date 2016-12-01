from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={'multiple': True}))