from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import users
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404

# from blog.models import users




def home(request):
    return render(request, 'index.html')


def regist(request):
    return render(request, 'regist.html')

def login(request):
    return render(request, 'login.html')

def userlist(request):
    print('show!') 
    userlists = users.objects.all()  
    print('userlists=>', userlists)
    return render(request, 'userlist.html',{'userlists':userlists})

def show(request):     
    print('userlists=>', userlists)
    return render(request,"userlist.html")  

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

def post_create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            form = PostForm()
        return render(request, 'postcreate.html', {'form': form})


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
