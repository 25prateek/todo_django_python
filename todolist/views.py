from django.shortcuts import render,HttpResponse
from todolist.models import Task
# Create your views here.
def home(request):
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(tasktitle=title,taskdesc=desc)
        ins.save()
        context={'success':True}

    return render(request,'index.html',context)
def task(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render(request,'task.html',context)
    