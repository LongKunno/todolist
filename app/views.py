from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import toDoList,Message
from .forms import MessageForm
from django.views.generic import ListView,View,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import random
from django.core.paginator import Paginator
from datetime import timedelta
from django.db.models import Q




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

        paginator = Paginator(todolist2, 10)
        num_pages = paginator.num_pages
        page_range = list(range(1, num_pages + 1))

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data= {'page_range':page_range,'tasks': page_obj ,'users': users}
        return data

class DeleteView(LoginRequiredMixin,DeleteView):
    model = toDoList
    success_url = '/home'

    
class AddView(LoginRequiredMixin,View):
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
    
class FormEditView(LoginRequiredMixin,View):
    def get(self, request, pk):
        list = toDoList.objects.get(id=pk)
        data = {'task': list}
        return render(request, 'app/formEdit.html', data)

class EditView(LoginRequiredMixin,View):
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
    
class SearchView(LoginRequiredMixin,View):
    def post(self,request):
        users = User.objects.all()
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
        
        data ={'tasks':todolist,'users': users} 
        return render(request,'app/home.html',data)

class LoginView(LoginView):
    template_name = 'app/login.html'
    
    def get_success_url(self):
        return 'home'
    
    def form_invalid(self, form):
        errors = form.errors.values()
        context = self.get_context_data(form=form, errors=errors)
        return self.render_to_response(context)
    

class LogoutView(LoginRequiredMixin,LogoutView):
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
        paginator = Paginator(todolist2, 10)
        num_pages = paginator.num_pages
        page_range = list(range(1, num_pages + 1))
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data= {'page_range':page_range,'tasks': page_obj ,'users': users}
        return data

class ChatView(LoginRequiredMixin,View):
    def get(self,request, receiver_id):
        receiver = get_object_or_404(User, id=receiver_id)
        messages = Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)
        form = MessageForm(request.POST or None)
        context = {
            'receiver': receiver,
            'messages': messages,
            'form': form
        }

        return render(request, 'app/chat_view.html', context)
    def post(self, request, receiver_id):
        receiver = get_object_or_404(User, id=receiver_id)
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect('chat_view', receiver_id=receiver_id)
        context = {
            'receiver': receiver,
            'form': form
        }
        return render(request, 'app/chat_view.html', context)
    
class IndexView(LoginRequiredMixin,View): 
    def get(self, request, receiver_id): 
        users = User.objects.all()
        context = { 'receiver_id': receiver_id , 'users': users} 
        return render(request, 'app/chat.html', context)
    
class GetMessagesView(LoginRequiredMixin,View): 
    def get(self, request,receiver_id): 
        receiver = get_object_or_404(User, id=receiver_id)
        messages = Message.objects.filter(sender=request.user, receiver=receiver).order_by('-timestamp')  | Message.objects.filter(sender=receiver, receiver=request.user).order_by('-timestamp')
        response = [{'receiver_username': receiver.username,'sender':str(message.sender),'receiver': str(message.receiver),'content': message.content, 'timestamp': message.timestamp.strftime("%H:%M")} for message in messages[::-1]] 
        return JsonResponse(response, safe=False)
    
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        sender_str = request.POST.get('sender')
        receiver_str = request.POST.get('receiver')
        sender=get_object_or_404(User, username=sender_str)
        receiver=get_object_or_404(User, id=receiver_str)
        message = Message.objects.create(content=content,sender=sender,receiver=receiver)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

class GetTable(LoginRequiredMixin,View): 
    def get(self, request): 
        users = User.objects.all()
        response = [{'username': user.username,'totalSend':Message.objects.filter(sender=user).count(),'totalReceived': Message.objects.filter(receiver=user).count()} for user in users[::+1]]
        return JsonResponse(response, safe=False)
    
class GetTodolist(LoginRequiredMixin,View):
    def get(self, request): 
        users = User.objects.all()
        response = [{'username': user.username,'totalTask':toDoList.objects.filter(userId=user.id).count(),'hoanthanh': toDoList.objects.filter(userId=user.id,progress=100).count(),'quahan': toDoList.objects.filter(userId=user.id,progress__lt=100,dueDate__lt=timezone.now()).count(),'dangtienhanh': toDoList.objects.filter(userId=user.id,progress__lt=100,dueDate__gt=timezone.now()).count()} for user in users[::+1]]
        return JsonResponse(response, safe=False)
    
class StatisticsView(LoginRequiredMixin,View): 
    def get(self, request ): 
        users = User.objects.all()
        context = { 'users': users} 
        return render(request, 'app/statistics.html', context)


class message_xoa2day(LoginRequiredMixin,View):
    def get(self, request):
        Message.objects.filter(timestamp__lt=timezone.now()-timedelta(days=2)).delete()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)
    

class message_add50tin(LoginRequiredMixin,View):
    def get(self, request):
        users=User.objects.all()    
        content = "random"
        timestamp = timezone.now()-timedelta(days=3)
        for i in range(50):
            users_test = User.objects.all()
            sender = random.choice(users_test)
            users_test = users_test.exclude(pk=sender.pk)
            receiver = random.choice(users_test)
            message = Message.objects.create(sender=sender,receiver=receiver,content=content)
            message.timestamp=timezone.now()-timedelta(days=3)
            print(message)
            message.save()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)

class todolist_xoaTaskQuaHan(LoginRequiredMixin,View):
    def get(self, request):
        data=toDoList.objects.filter(progress__lt=100,dueDate__lt=timezone.now())
        for i in data:
            print(i)
            i.delete()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)

class todolist_xoaTaskHoanThanh(LoginRequiredMixin,View):
    def get(self, request):
        data=toDoList.objects.filter(progress=100)
        for i in data:
            print(i)
            i.delete()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)

class todolist_cong1day(LoginRequiredMixin,View):
    def get(self, request): 
        data=toDoList.objects.all()
        for i in data:
            i.add_one_day_to_dueDate()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)
    
class todolist_tru1day(LoginRequiredMixin,View):
    def get(self, request): 
        data=toDoList.objects.all()
        for i in data:
            i.minus_one_day_to_dueDate()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)

class todolist_cong1dayQuaHan(LoginRequiredMixin,View):
    def get(self, request):
        data=toDoList.objects.all()
        for i in data:
            if i.dueDate<=timezone.now():
                i.add_one_day_to_dueDate_out_of_date()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)


class todolist_cong50taskRandom(LoginRequiredMixin,View):
    def get(self, request):
        users=User.objects.all()    
        taskName = "random"
        for i in range(50):
            users_test = User.objects.all()
            userId = random.choice(users_test).id
            progress = random.randint(1,120)
            if progress >=100:
                progress=100
            day = random.randint(-20,20)
            dueDate = timezone.now()+timedelta(day)
            todolist=toDoList.objects.create(taskName=taskName,userId=userId,progress=progress,dueDate=dueDate)
            print(todolist)
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)
    
class todolist_xoaTaskRandom(LoginRequiredMixin,View):
    def get(self, request): 
        data=toDoList.objects.filter(taskName="random")
        for i in data:
            print(i)
            i.delete()
        users = User.objects.all()
        context = {'users': users} 
        return render(request, 'app/statistics.html', context)












        