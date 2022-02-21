import email
import imp
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from shorter.models import Users

# Create your views here.

def index(request):
    user = Users.objects.filter(username="bob").first()
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
            username = Users.objects.filter(pk=user_id).update(username= username)

        return JsonResponse(dict(msg = "POST Method!"))

#
def redirect(request):
    print("go redirect!!")
    return redirect("index")