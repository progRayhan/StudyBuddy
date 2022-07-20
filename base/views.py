from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Mohammad Rayhan'},
#     {'id':2, 'name':'Ahmed Hridoy'},
#     {'id':3, 'name':'Mahfuz Alam'},
# ]

# Create your views here.
def home(request):
    # return HttpResponse("Home Page")
    # rooms = Room.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains = q)
    topics = Topic.objects.all()
    context = {'room':rooms, 'topics':topics}
    return render(request, 'base/home.html', context)

def room(request,pk):
    # return HttpResponse("Room Page")
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})


