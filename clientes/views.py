from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from .models import Nota
from .forms import NotaForm


def Index(request):
    notas = Nota.objects.all()
    form = NotaForm()

    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"notas":notas, "form":form}
    return render(request, 'lista.html', context)


def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def instagram(request):
    return render(request, 'instagram.html')


def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'form': form})


def nota_delete(request,id):
    nota = get_object_or_404(Nota, pk=id)
    form = NotaForm(request.POST or None, request.FILES or None, instance=nota)

    if request.method == 'POST':
        nota.delete()
        return redirect('/')

    return render(request, 'nota_delete_confirm.html', {'form': form})
