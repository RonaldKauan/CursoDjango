from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm



@login_required
def persons_list(request):

    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome and sobrenome:
        persons = Person.objects.filter(nome__icontains=nome) | Person.objects.filter(sobrenome__icontains=sobrenome)
        Person.usuario = True
        return render(request, 'person.html', {'persons': persons})
    elif nome:
        persons = Person.objects.filter(nome__icontains=nome)
        Person.usuario = True
        return render(request, 'person.html', {'persons': persons})
    elif sobrenome:
        persons = Person.objects.filter(sobrenome__icontains=sobrenome)
        Person.usuario = True
        return render(request, 'person.html', {'persons': persons})
    else:
        noUser = Person.objects.all()
        Person.usuario = False
        return render(request, 'person.html', {'persons': noUser})



@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})