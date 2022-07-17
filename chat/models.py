
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async



class QrCode(models.Model):
   url=models.URLField()
   image=models.ImageField(upload_to='qrcode',blank=True)
   group_name=models.CharField(max_length=100)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (400,400),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

class Room(models.Model):
    room_name = models.CharField(max_length=150, unique=True)
    super_user = models.CharField(max_length=150)
    users = models.ManyToManyField(get_user_model(), related_name='rooms')

    @classmethod
    @sync_to_async
    def add(cls, room_name, user):
        if cls.objects.filter(room_name=room_name):
            room, created = cls.objects.get_or_create(room_name=room_name) # 이 메서드는 (object, created) 라는 튜플 형식으로 반환을 한다. 첫번째 인자(object)는 우리가 꺼내려고 하는 모델의 인스턴스이고, 두번째 인자(created)는 boolean flag이다.
            room.users.add(user)
            return created
        else:
            room, created = cls.objects.get_or_create(room_name=room_name, super_user=user) # 이 메서드는 (object, created) 라는 튜플 형식으로 반환을 한다. 첫번째 인자(object)는 우리가 꺼내려고 하는 모델의 인스턴스이고, 두번째 인자(created)는 boolean flag이다.
            room.users.add(user)
            return created


    @classmethod
    @sync_to_async
    def users_count(cls, room_name):
        rooms = cls.objects.filter(room_name=room_name)
        if rooms.exists():
            return rooms.first().users.count()
        return 0

    @classmethod
    @sync_to_async
    def remove(cls, room_name, user):
        #  print('클래스 : ', cls)
         room = cls.objects.filter(room_name=room_name).first()
         users = cls.objects.get(id=room.id).users
         # print(users.count())

         # if room.exists():

         print('현재유저 > ', users.count())

         if users.count() >= 2:
            room.users.remove(user)
            print(user, '가 채팅방 데이터 베이스에서 삭제되었음')
         elif users.count() == 1:
            room.delete()
         else:
            print("문제발생")

class Channel_names(models.Model):
    user_name = models.CharField(max_length=150)
    channel_name = models.CharField(max_length=150)

    @classmethod
    @sync_to_async
    def add(cls, channel_name, user):
        if cls.objects.filter(user_name=user):
            channel = cls.objects.filter(user_name=user).first()
            channel.delete()
        cls.objects.create(user_name=user, channel_name=channel_name)

    @classmethod
    @sync_to_async
    def remove_ch_list(cls, channel_name):
        channel = cls.objects.filter(channel_name=channel_name).first()
        print('삭제채널 : ', channel)
        if channel is not None:
            channel.delete()

    @classmethod
    @sync_to_async
    def get(cls, user):
        kick_user = cls.objects.filter(user_name=user).first().channel_name
        print('강퇴대상 >>>', kick_user)
        return kick_user

 