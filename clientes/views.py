from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


@login_required
def persons_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome and sobrenome:
        nome = nome.lower()
        sobrenome = sobrenome.lower()
        pessoas = {}

        for elemento in Person.objects.values():
            pessoas[elemento['id']] = elemento['nome'].lower()

        listaPessoasErradas = []
        listaPessoas = []

        for pessoa in pessoas.keys():
            listaPessoas.append(pessoa)
            if pessoas[pessoa] != nome:
                listaPessoasErradas.append(pessoa)

        if listaPessoas == listaPessoasErradas:
            return render(request, 'person.html', {'persons':'noUser'})

        else:
            persons = Person.objects.filter(sobrenome__icontains=sobrenome.lower()).exclude(id__in=listaPessoasErradas)
            return render(request, 'person.html', {'persons': persons})

    elif nome:
        persons = Person.objects.filter(nome__icontains=nome)
        return render(request, 'person.html', {'persons': persons})
    elif sobrenome:
        persons = Person.objects.filter(sobrenome__icontains=sobrenome)
        return render(request, 'person.html', {'persons': persons})
    else:
        persons = Person.objects.all()
        return render(request, 'person.html', {'persons': persons})


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
