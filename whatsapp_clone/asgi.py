"""
ASGI config for whatsapp_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from chats.consumers import PersonalChatConsumer, OnlineStatusConsumer, NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_clone.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    # AuthMiddlewareStack is use to get id of current user in chat->consumers-> PersonalChatConsumer
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/online/', OnlineStatusConsumer.as_asgi()),
            path('ws/notify/', NotificationConsumer.as_asgi())
        ])
    )
})