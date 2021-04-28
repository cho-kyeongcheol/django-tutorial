from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import users
from .models import audiofiles
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core import serializers

from django.contrib.auth import authenticate, login

import json

from django.core.serializers.json import DjangoJSONEncoder
import json as simplejson

def home(request):
    subject = "math"    

    request.session['test'] = "hahaha"
    request.session['subject'] = subject
    print('@@session.sub =>', request.session['subject'] )
    
    # if user_id :
    #     myuser_info = users.objects.get(pk=id)  #pk : primary key
    #     return HttpResponse(myuser_info.user_id)   # 로그인을 했다면, username 출력

    return render(request, 'login.html')

def upload_file(request):
    print('upload_file!!!@@###')
    if request.method == 'POST':
        print('##request.POST =>',request.POST)
        print('##request.FILES =>',request.FILES) 
        # print('$$request.FILES.file =>',request.FILES.file)
        form = UploadFileForm(request.POST, request.FILES)
        print('form =>', form)
        print('@@@@@@@')
        # test = form.is_valid()
        # print('## test =>', test)
        if form.is_valid():
            print('#####VALID')
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        else :
            print('####VALID ELSE')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
    

def index(request):

    return render(request, 'index.html')

def logout(request):

    return render(request, 'index.html')
    
def datatable(request):

    return render(request, 'datatable.html')

def userdetail(request):
    user_detail = get.objects_or_404(users, pk=user_id)
    
    return render(request, 'userdetail.html')

def usertable(request):
    userlists = users.objects.all()  
    print('## userlists =>' , userlists)
    json = serializers.serialize('json', userlists)
    
    print('## json => ', json)
    return HttpResponse(json, content_type='application/json')


def regist(request):
    
    return render(request, 'regist.html')

@csrf_exempt
def login(request):

    return render(request, 'login.html')



@csrf_exempt
def userlogin(request):
    print('LOGIN!@!@')
    response_data = {}
    if request.method == "GET" :        
        return render(request, 'login.html')
    elif request.method == "POST":     
        print('IN POST!@')
        userid = request.POST.get('id')
        userpw = request.POST.get('pw')

        #유효성 처리
        res_data ={}
        if not (userid and userpw):
            print('111111111111')
            res_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            print('22222222222')
            myuser = users.objects.get(user_id=userid) 
            # myuser = check_password(user_id=userid, password=userpw)
            print('#myuser =>', myuser)
            print('#userid =>', userid)
            print('#userpw =>', userpw)
            print('myuser.id =>', myuser.user_id)
            print('myuser.pw =>', myuser.password)

            if check_password(userpw, myuser.password):
                print('444444444')
                
                request.session['user']=myuser.id
                print('로그인성공!')
                return redirect('/')

            else:
                print('5555555')
                res_data['error'] = "비밀번호가 틀렸습니다."
                print('로그인실패!')
            


            # if(userid == myuser.user_id) :
            #     if (userpw == myuser.password) :
            #         print('로그인 성공!')
            #         request.session['user']=myuser.id
            #         data = json.dumps({'status':"success", 'msg':"로그인 성공"})                    
            #         # return redirect('/')
                    
            #     else :
            #         print('로그인 실패!')                    
            #         data = json.dumps({'status':"fail", 'msg':"비밀번호가 틀렸습니다"})                     
            # else :
            #     data = json.dumps({'status':"fail", 'msg':"아이다가 틀렸습니다"})    


                   
    # return HttpResponse(data, 'application/json')     
    return render(request,'index.html', res_data) #응답 데이터 res_data 전달
    # return render(request,'index.html', {'response_data': response_data, 'content' : content ,'contents' : contents}) 



# @csrf_exempt
# def userlogin(request):
#     print('login!!!')
#     id = request.POST['id']
#     pw = request.POST['pw']
#     print('id=>',id)
#     print('pw=>',pw)
#     return HttpResponse('bad')

# def userview(request):
# return render(request, 'userview.html')

def userlist(request):
    print('show!') 
    userlists = users.objects.all()  
    print('userlists=>', userlists)
    return render(request, 'userlist.html',{'userlists':userlists})


@csrf_exempt
def user_insert(request):
    print('USERINSERT@!#@#@')
    QueryDict = request.POST
    print('QueryDict =>', QueryDict)
    id = request.POST['id']
    pw = request.POST['pw']
    name = request.POST['name']
    email = request.POST['email']

    print('id =>', id)
    print('pw =>', pw)
    print('name =>', name)
    print('email =>', email)

    # Feedback 객체 생성
    userInsert = users(user_id = id, password= pw, name=name , email = email)
    print('userInsert =>', userInsert)
    # 새 객체 INSERT
    userInsert.save()
    print('#####')
        
    return JsonResponse({"data": "success"})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'postdetail.html', {'post':post})


def post_update(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.sava()
            return redirect('home')
        else:
            form = PostForm(instance=post)
        return render(request, 'postupdate.html', {'form':form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')
