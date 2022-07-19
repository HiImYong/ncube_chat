# mysite/asgi.py
import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_project.settings")
# AppRegistry를 보장하기 위해 Django ASGI 애플리케이션을 일찍 초기화합니다.
# ORM 모델을 가져올 수 있는 코드를 가져오기 전에 채워집니다.
django.setup()
django_asgi_app = get_asgi_application()



import chat.routing

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})