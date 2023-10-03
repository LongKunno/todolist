from django.shortcuts import redirect, render
from .models import toDoList

# Create your views here.
def home(request):
    todolist = toDoList.objects.all().order_by("dueDate")
    for i in todolist:
        i.phantram=i.progress
        if i.phantram>80:
            i.mau='bg-green'
        elif i.phantram>60:
            i.mau='bg-purple'
        elif i.phantram>40:
            i.mau='bg-cyan'
        elif i.phantram>20:
            i.mau='bg-yellow'
        else:
            i.mau='bg-red'    
        i.progress*=5
    data ={'tasks':todolist} 
    return render(request,'pages/home.html',data)

def add(request):
    if request.method=='POST':
        taskName=request.POST.get('taskName')
        progress=request.POST.get('progress')
        dueDate=request.POST.get('dueDate')
        toDoList.objects.create(taskName=taskName,progress=progress,dueDate=dueDate)
    return redirect('/')

def formEdit(request,id):
    list = toDoList.objects.get(id=id)
    data={
        'task': list
    }
    return render(request,'pages/formEdit.html',data)
def edit(request):
    id=request.POST.get('id')
    toDoList.objects.get(id=id)
    taskName=request.POST.get('taskName')
    progress=request.POST.get('progress')
    dueDate=request.POST.get('dueDate')
    toDoList(id=id,taskName=taskName,progress=progress,dueDate=dueDate).save()
    return redirect('/')

def delete(request,id):
    toDoList.objects.get(id=id).delete()
    return redirect('/')

def search(request):
    todolist = toDoList.objects.filter(taskName__icontains=request.POST.get('search'))
    for i in todolist:
        i.phantram=i.progress
        if i.phantram>80:
            i.mau='bg-green'
        elif i.phantram>60:
            i.mau='bg-purple'
        elif i.phantram>40:
            i.mau='bg-cyan'
        elif i.phantram>20:
            i.mau='bg-yellow'
        else:
            i.mau='bg-red'    
        i.progress*=5
    data ={'tasks':todolist} 
    return render(request,'pages/home.html',data)