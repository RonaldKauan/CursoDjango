from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'sobrenome', 'idade', 'salario', 'bio', 'foto']
