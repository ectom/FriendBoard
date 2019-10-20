from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt


def index(request):
    return render(request, 'friends/index.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.filter(alias=request.POST['alias'])
        if user.count() > 0:
            messages.error(request, "alias already taken", extra_tags="alias")
            return redirect('/')
        else:
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            create_user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'],
                                              email=request.POST['email'], birthday=request.POST['birthday'],
                                              password=hashed)
            request.session['user_id'] = create_user.id
            request.session['name'] = create_user.name
            print(user)
            return redirect('/friends')


def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users.count() > 0:
        user = users.first()
        if bcrypt.checkpw(request.POST['password'].encode(),
                          user.password.encode()) == True:  # checks for correct password
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            print(user)
            return redirect('/friends')
        else:
            messages.error(request, "Login Failed", extra_tags="email")
            return redirect('/')
    else:
        messages.error(request, "Login Failed", extra_tags="alias")
        return redirect('/')


def friends(request):
    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.all()
    others = []
    for other_user in users:
        if (other_user.id != request.session['user_id']):
            others.append(other_user)
    friends = Friend.objects.filter(users=user)
    real_friends = []
    real_others = []
    for each_friend in friends:
        real_friends.append(each_friend.friends)
    for other_user in others:
        if (other_user not in real_friends):
            real_others.append(other_user)
    data = {
        'users': real_others,
        'friends': real_friends
    }
    return render(request, 'friends/friends.html', data)


def logout(request):
    request.session.clear()
    return redirect('/')


def user(request, user_id):
    data = {
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'friends/user.html', data)


def add_friend(request, user_id):
    User.objects.adds(request.session['user_id'], user_id)
    return redirect('/friends')


def remove(request, user_id):
    User.objects.removes(request.session['user_id'], user_id)
    return redirect('/friends')
