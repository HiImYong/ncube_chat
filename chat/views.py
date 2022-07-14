# chat/views.py
from django.shortcuts import redirect, render

from .models import QrCode, Room
from django.contrib.auth.models import User

from django.db.models import Count




def index(request):
    room_objects = Room.objects.all()
    return render(request, 'chat/index.html',{'room_objects' : room_objects})

def room(request, room_name):
    if Room.objects.all():
        room_objects = Room.objects.get(room_name=room_name)
        super_user_object = room_objects.super_user
        user_objects = room_objects.users.all()
        user_str_objects = map(str, user_objects)

    else:
        user_objects = {request.user.username}
        user_str_objects = {request.user.username}
        super_user_object = {request.user.username}
        
    

    QrCode.objects.create(url='http://localhost:8000'+request.path_info, group_name='chatgroup_'+room_name)

    qr_code=QrCode.objects.filter(group_name='chatgroup_'+room_name).first()


    return render(request, 'chat/room.html', {   
        'user_objects': user_objects,
        'user_str_objects': user_str_objects,
        'super_user_object' : super_user_object,
        'room_name': room_name,
        'qr_code':qr_code
    })

# def qrcode(request):
#    if request.method=="POST":
#       Url=request.POST['url']
#       QrCode.objects.create(url=Url)

#    qr_code=QrCode.objects.last()
#    return render(request,"chat/room.html",{'qr_code':qr_code})



# def kick_user(request, room_name):
#     room_objects = Room.objects.get(room_name=room_name)
#     user_objects = room_objects.users.all()
#     print('컨슈머.py >> : ', request.POST['kick'])
#     kicked_user = request.POST['kick']
#     Room.remove(Room, room_name, kicked_user)
#     return redirect('/chat/dd/')
