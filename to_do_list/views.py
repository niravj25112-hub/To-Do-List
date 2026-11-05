from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from to_do_list.models import To_Do_List

# Create your views here.
def home(request):
    tasks = To_Do_List.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            To_Do_List.objects.create(
                title=title,
                description=description
            )
            return redirect('home')

    return render(request, 'add_task.html')

def edit_task(request, id):
    std_id = get_object_or_404(To_Do_List, id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            std_id.title = title
            std_id.description = description
            std_id.save()

            return redirect('home')

    return render(request, 'edit_task.html', {'std_id': std_id})

def delete_task(request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    std_id = get_object_or_404(To_Do_List, id=id)
    std_id.delete()
    return redirect('home')

def update_task(request,id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    task_update = get_object_or_404(To_Do_List, id=id)
    task=request.POST.get('done')=="True"
    task_update.done=task
    task_update.save()
    return redirect('home')
