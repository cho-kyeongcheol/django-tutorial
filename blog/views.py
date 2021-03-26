from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import users
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt

# from blog.models import users




def home(request):
    # posts = Post.objects    
    return render(request, 'index.html')

@csrf_exempt
def user_insert(request):
    print('USERINSERT@!#@#@')
    qd = request.POST
    print('qd =>', qd)
    id = request.POST['id']
    pw = request.POST['pw']
    name = request.POST['name']
    email = request.POST['email']

    print('id =>', id)
    print('pw =>', pw)
    print('name =>', name)
    print('email =>', email)

    if request.method == 'POST':
        print('post!!')
        else:
            print('else!!')

        # form = UserForm(request.POST)
        # print('11111111111')
            # if form.is_valid(self):
            #     print('222222222222')
            #     else :
            #         print('ELSESESELELESLSEL')
                # form.save()
            #     print('3333333333')
            #     return redirect('index')
            #     print('444444444444')
            # form = UserForm()
            # print('5555555555')
        
    return render(request, 'index.html',{'form': form})

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
