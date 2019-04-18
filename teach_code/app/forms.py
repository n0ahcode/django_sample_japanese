from django import forms
from .models import CodeModel



class CodeModelForm(forms.ModelForm):
    class Meta:
        model = CodeModel
        fields = ['title','text','name','tags']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
