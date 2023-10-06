from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,  get_object_or_404
from .models import toDoList,Message
from .forms import toDoListForm,MessageForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView,View,DeleteView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



# Create your views here.
# def home(request):
#     todolist = toDoList.objects.all().order_by("dueDate")
#     for i in todolist:
#         i.phantram=i.progress
#         if i.phantram>80:
#             i.mau='bg-green'
#         elif i.phantram>60:
#             i.mau='bg-purple'
#         elif i.phantram>40:
#             i.mau='bg-cyan'
#         elif i.phantram>20:
#             i.mau='bg-yellow'
#         else:
#             i.mau='bg-red'    
#         i.progress*=5
#     data ={'tasks':todolist} 
#     return render(request,'app/home.html',data)



# def add(request):
#     if request.method=='POST':
#         taskName=request.POST.get('taskName')
#         progress=request.POST.get('progress')
#         dueDate=request.POST.get('dueDate')
#         toDoList.objects.create(taskName=taskName,progress=progress,dueDate=dueDate)
#     return redirect('/')

# def formEdit(request,id):
#     list = toDoList.objects.get(id=id)
#     data={
#         'task': list
#     }
#     return render(request,'app/formEdit.html',data)
# def edit(request):
#     id=request.POST.get('id')
#     toDoList.objects.get(id=id)
#     taskName=request.POST.get('taskName')
#     progress=request.POST.get('progress')
#     dueDate=request.POST.get('dueDate')
#     toDoList(id=id,taskName=taskName,progress=progress,dueDate=dueDate).save()
#     return redirect('/')

# def delete(request,id):
#     toDoList.objects.get(id=id).delete()
#     return redirect('/')

# def search(request):
#     todolist = toDoList.objects.filter(taskName__icontains=request.POST.get('search'))
#     for i in todolist:
#         i.phantram=i.progress
#         if i.phantram>80:
#             i.mau='bg-green'
#         elif i.phantram>60:
#             i.mau='bg-purple'
#         elif i.phantram>40:
#             i.mau='bg-cyan'
#         elif i.phantram>20:
#             i.mau='bg-yellow'
#         else:
#             i.mau='bg-red'    
#         i.progress*=5
#     data ={'tasks':todolist} 
#     return render(request,'app/home.html',data)


class HomeListView(LoginRequiredMixin,ListView):
    model = toDoList
    template_name = 'app/home.html'
    context_object_name = 'tasks'
    ordering = 'dueDate'

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        todolist = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        todolist2 = todolist['tasks'].filter(userId=user_id)  # Lọc theo user id
        for i in todolist2:
            if i.dueDate < timezone.now():
                i.dueDate = 'Quá hạn '+str(timezone.now()-i.dueDate)
            i.phantram = i.progress
            if i.phantram == 100:
                i.mau = 'bg-green'
                i.dueDate = 'Đã hoàn thành'
            elif i.phantram > 80:
                i.mau = 'bg-green'
            elif i.phantram > 60:
                i.mau = 'bg-purple'
            elif i.phantram > 40:
                i.mau = 'bg-cyan'
            elif i.phantram > 20:
                i.mau = 'bg-yellow'
            else:
                i.mau = 'bg-red'
            i.progress *= 5
        data ={'tasks':todolist2,'users': users} 
        return data

class DeleteView(DeleteView):
    model = toDoList
    success_url = '/home'

    
class AddView(View):
    def post(self, request): 
        taskName = request.POST.get('taskName') 
        progress = request.POST.get('progress') 
        dueDate = request.POST.get('dueDate') 
       
        if request.POST.get('userId') != 'None':
            userId = request.POST.get('userId') 
        else:
            userId = 0
        toDoList.objects.create(taskName=taskName, progress=progress, dueDate=dueDate, userId=userId) 
        return redirect('home')
    
class FormEditView(View):
    def get(self, request, pk):
        list = toDoList.objects.get(id=pk)
        data = {'task': list}
        return render(request, 'app/formEdit.html', data)

class EditView(View):
    def post(self,request):
        id=request.POST.get('id')
        data = toDoList.objects.get(id=id)
        taskName=request.POST.get('taskName')
        progress=request.POST.get('progress')
        dueDate=request.POST.get('dueDate')
        data.taskName = taskName
        data.progress = progress
        data.dueDate = dueDate
        data.save()
        return redirect('home')
    
class SearchView(View):
    def post(self,request):
        todolist = toDoList.objects.filter(taskName__icontains=request.POST.get('search'),userId=self.request.user.id)
        for i in todolist:
            if i.dueDate < timezone.now():
                i.dueDate = 'Quá hạn '+str(timezone.now()-i.dueDate)
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
        return render(request,'app/home.html',data)

class LoginView(LoginView):
    template_name = 'app/login.html'
    
    def get_success_url(self):
        return 'home'
    
    def form_invalid(self, form):
        errors = form.errors.values()
        context = self.get_context_data(form=form, errors=errors)
        return self.render_to_response(context)
    

class LogoutView(LogoutView):
    next_page='/'


class test(View):
    def get(self, request):
        return render(request,'app/test.html')


class SortView(LoginRequiredMixin,ListView):
    model = toDoList
    template_name = 'app/home.html'
    context_object_name = 'tasks'
    ordering = 'progress'

    def get_context_data(self, **kwargs):
        todolist = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        todolist2 = todolist['tasks'].filter(userId=user_id)  # Lọc theo user id
        for i in todolist2:
            if i.dueDate < timezone.now():
                i.dueDate = 'Quá hạn '+str(timezone.now()-i.dueDate)
            i.phantram = i.progress
            if i.phantram == 100:
                i.mau = 'bg-green'
                i.dueDate = 'Đã hoàn thành'
            elif i.phantram > 80:
                i.mau = 'bg-green'
            elif i.phantram > 60:
                i.mau = 'bg-purple'
            elif i.phantram > 40:
                i.mau = 'bg-cyan'
            elif i.phantram > 20:
                i.mau = 'bg-yellow'
            else:
                i.mau = 'bg-red'
            i.progress *= 5
        data ={'tasks':todolist2} 
        return data

def chat_view(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    messages = Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            content = form.cleaned_data['content']
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect('chat_view', receiver_id=receiver_id)

    context = {
        'receiver': receiver,
        'messages': messages,
        'form': form
    }

    return render(request, 'app/chat_view.html', context)



# class BackView(View):
#     def get(self, request):
#         # Lấy đường dẫn trang trước đó từ request.META
#         previous_page = request.META.get('HTTP_REFERER')
#         if previous_page:
#             return redirect(previous_page)
#         return redirect('home')
