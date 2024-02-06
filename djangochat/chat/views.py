from django.shortcuts import render, redirect
from chat.models import Room, Message

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'home.html')

def room(request, room, *args, **kwargs):
    # Your view logic here
    return render(request, 'room.html', {'room_name': room})

def checkview(request, *args, **kwargs):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else: 
        new_room = Room.objects.create(name=room)
        new_room.save
        return redirect('/'+room+'/?username='+username)