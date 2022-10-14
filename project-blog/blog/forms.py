from django import forms

from blog.models import Cidade, SugestaoPost

from django.forms import ModelForm


class BuscaPostForm(forms.Form):

    busca = forms.CharField(label='Busca', max_length=100, required=False)
    cidades = forms.ModelMultipleChoiceField(label='Cidades',
                                             queryset=Cidade.objects.all(),
                                             required=False)    


class SugestaoPostForm(ModelForm):

    class Meta:
        model = SugestaoPost
        exclude = ()