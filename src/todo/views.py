from django.shortcuts import render

from .forms import ToDo
from .models import DoList
from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
)

# Create your views here.



def home(request):
    list_of_objects = list(DoList.objects.all())
    if request.method == 'GET':

        context = {'a': list_of_objects}
        return render(request, 'home.html', context)

    elif request.method == "POST":
        if request.POST.get("save"):
            for item in list_of_objects:
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complite = True
                else:
                    item.complite = False

                item.save()

        elif request.POST.get("newItem"):
            context = {'form': ToDo()}
            return render(request, 'add_new.html', context)

    return redirect('home')


def add_new(request):
    list_of_objects = list(DoList.objects.all())
    if request.method == 'GET':
        context = {'form': ToDo()}
        return render(request, 'add_new.html', context)
    elif request.method == 'POST':
        form = ToDo(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_do = DoList.objects.create(
                line=data.get('line'),

            )
            list_of_objects.append(new_do)
            return redirect('home')
        else:
            errors = form.errors

            return HttpResponse(f'{errors}')
    else:
        return HttpResponse('Wrong request method')


def edit_record(request, do_id):
    list_of_objects = list(DoList.objects.all())
    try:
        doing = DoList.objects.get(id=do_id)
    except:
        return render(request, 'some_error.html')

    if request.method == 'GET':
        context = {
            'do_id': do_id,
            'form': ToDo(
                initial={
                    'line': doing.line,

                },
            ),
        }

        return render(request, 'edit_record.html', context)
    elif request.method == 'POST':
        list_of_objects = list(DoList.objects.all())
        form = ToDo(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            DoList.objects.filter(id=do_id).update(
                line=data.get('line'),

            )
            changed_do = list(DoList.objects.filter(id=do_id))
            for i in list_of_objects:
                if i.id == do_id:
                    index = list_of_objects.index(i)
                    list_of_objects[index] = changed_do[0]
                    break

            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def remove_record(request, do_id):
    list_of_objects = list(DoList.objects.all())
    try:
        do = DoList.objects.get(id=do_id)
    except:
        return render(request, 'some_error.html')
    do.delete()
    for i in list_of_objects:
        if i.id == do_id:
            index = list_of_objects.index(i)
            break

    del list_of_objects[index]
    return redirect('home')
