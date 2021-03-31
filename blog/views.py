from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import users
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib import auth
from django.contrib.auth.hashers import check_password


def home(request):
    request.session['test'] = "hahaha"
    
    # if user_id :
    #     myuser_info = users.objects.get(pk=id)  #pk : primary key
    #     return HttpResponse(myuser_info.user_id)   # 로그인을 했다면, username 출력

    return render(request, 'index.html')

def regist(request):
    print(request.session.session_key)

    session_id = request.session.session_key
    test = request.session['test']
    alal = request.session.get('test')

    contents = {
        'session_id' : session_id,
        'test': test
    }
    print('test =>', test)
    print('alal=>', alal)

    
    return render(request, 'regist.html', contents)

@csrf_exempt
def login(request):
    print('LOGIN!@!@')
    response_data = {}
    if request.method == "GET" :
        print('IN GET!@!@')
        return render(request, 'login.html')

    elif request.method == "POST":                
        print('IN POST!@')
        userid = request.POST.get('userid', None)
        userpw = request.POST.get('userpw', None)
        print('userid =>', userid)
        print('userpw =>', userpw)

        if not (userid and userpw):
            print('#####')
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            print('%%%%')
            myuser = users.objects.get(user_id=userid) 
            print('myuser=>' , myuser)
            print('userpw =>', userpw)
            print('myuser.password=>' , myuser.password)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(userpw, myuser.password):
                print(' IN CHECK_PASSWORD!!')
                print('myuser.password22=>' , myuser.password)
                request.session['user'] = myuser.id 
                print('2222')
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                print('#IN CHECKrequest =>',request)
                print('#IN CHECKrequest.session=>',request.session)
                print('#IN CHECKrequest.session.@session_key=>',request.session.session_key)
                user_id = request.session.get('user')
                print('#IN CHECKuser_id =>', user_id)
                return redirect('/')
            else:
                print('ELSE CHECKPASSWORD')
                response_data['error'] = "비밀번호를 틀렸습니다."

    print('#request =>',request)
    print('#request.session=>',request.session)
    print('#request.session.@session_key=>',request.session.session_key)
    user_id = request.session.get('user')
    print('#user_id =>', user_id)

    return render(request, 'index.html', response_data)

@csrf_exempt
def userlogin(request):
    print('login!!!')
    id = request.POST['id']
    pw = request.POST['pw']
    print('id=>',id)
    print('pw=>',pw)
    return HttpResponse('bad')

# def userview(request):
# return render(request, 'userview.html')

def userlist(request):
    print('request =>',request)
    print('request.session=>',request.session)
    print('request.session.session_key=>',request.session.session_key)    
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
