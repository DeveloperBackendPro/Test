from django.http import JsonResponse
from django.shortcuts import render,redirect
from home.models import Test, Category, Student
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Student.objects.get(user_id=request.user.id)
                return redirect('home')
            except:
                return redirect('login_form')
        else:
            messages.warning(request, "Ошибка входа! Логин или пароль неверны")
            return redirect('login_form')
    return render(request, 'login.html')

def logout_manager(request):
    logout(request)
    return redirect('login_form')

def home(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,'home.html',context)

def search_box(request):
    return render(request,'search_box.html')

def search_document(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        res = None
        questions = request.POST.get('questions')
        qs = Test.objects.filter(questions__icontains=questions, status='True')
        if len(qs) > 0 and len(questions) > 0:
            data = []
            for pos in qs:
                item = {
                    'id':pos.id,
                    'questions':pos.questions,
                    'answer':pos.answer,
                }
                data.append(item)
            res = data
        else:
            res = "Нет такой информации"
        return JsonResponse({'data':res})
    return JsonResponse({})
