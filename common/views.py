# chat/views.py
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import UserForm, email_form
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            print("폼에 문제가 없음")
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)  # 사용자 인증
            return redirect('common:login')

        else :
            print("폼에 문제가 있음")
            get_error = form.errors                           
            return render(request,'common/signup.html',{'show_error' : get_error})
    else:
        form = UserForm()
    return render(request,'common/signup.html')

    # render의 경우 내가 가진 templates를 data를 넣어 보내고 싶을 때 이용(서브루트/페이지.html로 기입)
    # redirect는 내가 가진 templates뿐만 아니라 절대 url로 이동하고 싶을 때에도 이용('appname:name'으로 기입 가능)


@csrf_exempt
def ajax_user_id(request):
    if 'email' in request.POST:
        email_object = request.POST['email']
        print('json = ' + request.POST['email'])
        qs = User.objects.filter(email = email_object).first()
        print('object = ' + email_object)
        print(qs)
        get_id = qs.username
        # print(get_id)
        data = {'get_id' : get_id}
    
        return JsonResponse(data)

def find_user(request):
    print("고객찾기페이지 그려주기")
    return render(request, 'common/find_user.html')


