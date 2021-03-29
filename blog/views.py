from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import users
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404


def home(request):
    print('request =>',request)
    print('request.session=>',request.session)
    print('request.session.session_key=>',request.session.session_key)
    return render(request, 'index.html')

def regist(request):
    return render(request, 'regist.html')

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def userlogin(request):
    print('login!!!')
    id = request.POST['id']
    pw = request.POST['pw']
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
