from django.shortcuts import render
from django.contrib.auth import get_user_model
# The get_user_model() function returns the user model class, and
# you can use this class to perform operations related to user authentication,
#  registration, and user data.

from chats.models import ChatModel
# Create your views here.


User = get_user_model()
# This line of code assigns the user model class to a variable named User. By convention, this variable is capitalized to indicate that it represents the user model.
# Once you've assigned the user model class to User, you can use this variable to work with the user model in your code. For example, you can use it to create, update, or query user objects, as well as perform authentication-related tasks.

def index(request):
    users = User.objects.exclude(username=request.user.username)
    # taking all user except the logged in user-----
    # User.objects: This is a manager for the User model, which represents user objects in your application. You are using it to create a query to the database.
    # .exclude(username=request.user.username): This part of the query uses the exclude() method to filter the user objects. It excludes the user(s) whose username matches the request.user.username
    return render(request, 'index.html', context={'users': users})
    #  'users' is the key we have use in our index page


def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
