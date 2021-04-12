from django.forms import ModelForm
from .models import Person
from .forms import PersonForm

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

def persons_new(request):
    pass