import email
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from shorter.forms import RegistForm, LoginForm

from shorter.models import User

# Create your views here.

def index(request):
    user = User.objects.filter(id = request.user.id).first()
    email = user.email if user else "Anonymous User!"
    if request.user.is_authenticated is False: # 로그인 여부를 물어봄 되어있으면 True 
    # // is_anonymous -> 로그아웃 여부 // is_activate -> 로그인, 로그아웃을 넘어서 유저의 현재 활동이 가능한지 // is_superuser 도 있음
        email = "Anonymous User!"

    print(email)

    return render(request, "base.html", {"userparam": f"Hello {email}"})

@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == 'GET':
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = User.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
        
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            username = User.objects.filter(pk=user_id).update(username= username)

        return JsonResponse(dict(msg = "POST Method!"))

def register_view(request):
    if request.method == "POST":
        form = RegistForm(request.POST)
        msg = "올바르지 않는 ID와 비밀번호 입니다. 다시 입력해주세요"
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입 성공"
        return render(request, "register.html", {"form": form, "msg": msg})
    
    else :
        form = RegistForm()
        return render(request, "register.html", {"form": form})
    
def login_view(request):
    msg = None
    is_ok = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            msg = "올바른 이메일과 패스워드를 넣어주세요"
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                if user.check_password(password):
                    msg = None
                    login(request, user)
                    is_ok = True
                    request.session["remember_me"] = remember_me
    else:
        msg = None
        form = LoginForm()
        
    print(f"REMEMVER ME STATUS --> {request.session.get('remember_me')}")
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})

    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(username = username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             is_ok = True
    #     else:
    #         msg = '올바른 아이디와 비밀번호를 입력해주세요'
    # else:
    #     form = AuthenticationForm()
        
    # for visible in form.visible_fields(): 
    #     print(visible)
    #     visible.field.widget.attrs["placeholder"] = "유저ID" if visible.name =="username" else "패스워드"
    #     visible.field.widget.attrs["class"] = "form-control"
        
    # return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})        
    #     form = AuthenticationForm(request, request.POST)
    #     msg = "로그인 정보가 잘못되었습니다. 아이디와 비밀번호를 다시 입력해주세요"
    #     if form.is_valid():
    #         #form.save()
    #         username = form.cleaned_data.get("username")
    #         raw_password = form.cleaned_data.get("password")
    #         user = authenticate(username = username, password = raw_password)
    #         if user is not None:
    #             login(request, user)
    #             msg = "로그인 완료"
    #             return redirect("list")
    #     return render(request, "login.html", {"form": form, "msg": msg})
    # else:
    #     form = AuthenticationForm()
    #     return render(request, "login.html", {"form": form})
    # return render(request, "login.html",{"hello":"world"})

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required #로그인을 해야만 조회가능
def list_view(request):
    page = int(request.GET.get("p", 1)) # ex) http://localhost:8000/list_view?p=1 뒤에 p=1
    user = User.objects.all().order_by("id")
    paginator = Paginator(user, 10)
    user = paginator.get_page(page)
    
    return render(request, "board.html", {"user": user})