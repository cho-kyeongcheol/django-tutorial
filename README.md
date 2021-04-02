# Django Project START!

### Project Setting
```
$ python -m venv 'myvenv' #가상환경 생성
$ source myvenv/scripts/activate # 가상환경 실행
(myvenv) # 가상환경 켜짐
$ pip install django # django 설치
$ django-admin startproject <project name> #프로젝트 생성
# 이때 manage.py가 위치한 프로젝트 안(BASE_DIR)으로 들어간다. 
$ python manage.py startapp <app name> # app 생성
$ python manage.py runserver # http://127.0.0.1:8000/

```
### session 관리
```
session_id = request.session.session_key

# 넣기
request.session['test'] = "hahaha" 

# 빼기
test = request.session['test']
test = request.session.get('test') 

# 담기
contents = {
    'session_id' : session_id,
    'test': test
}

# template로 전달
return render(request, 'regist.html', contents)
```


```
Forbidden (CSRF token missing or incorrect.): /userlogin

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
```



### DataTable
##### ajax
``` js
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" language="javascript" class="init">
    
    $(document).ready(function() {
        console.log('## working ##')
         $('#deviceTable').dataTable( {
             "processing": true,
             "ajax": {
                 "processing": true,
                 "url": "{% url 'usertable' %}",
                 "dataSrc": ""
             },

             "columns": [
                     { "data": "fields.user_id" },
                     { "data": "fields.name" },
                     { "data": "fields.email" },
                 ]
         } );
     } );

</script>

```
#### views.py
``` python
    
def usertable(request):
    userlists = users.objects.all()  
    print('## userlists =>' , userlists)
    json = serializers.serialize('json', userlists)
    
    print('## json => ', json)
    return HttpResponse(json, content_type='application/json')

```



#### 에러 모음
```
https://velog.io/@ash3767/django-%EC%97%90%EB%9F%AC-%EB%AA%A8%EC%9D%8C
```
