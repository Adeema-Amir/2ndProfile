import json
from django.shortcuts import render
from app.models import house
from django.template.loader import get_template

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
                  
# def index(request):
#    if request.method == "POST":
#     name = request.POST.get("name")
#     room = request.POST.get("room")
#     kitchen = request.POST.get("kitchen")
#     bathroom = request.POST.get("bathroom")
#     drawing_room = request.POST.get("drawing_room")
#     data=house(
#         name=name,
#         room=room,
#         kitchen=kitchen,
#         bathroom=bathroom,
#         drawing_room=drawing_room
#     )
#     data.save()
    
#     b='your data has been sent sir you can go and check'
#     return render(request,'index.html',{'b':b})
       
       
                  
def about(request):
    return render(request,'about.html')

def index(request):
  if request.method == "POST":
    name = request.POST.get("name")
    room = request.POST.get("room")
    kitchen = request.POST.get("kitchen")
    bathroom = request.POST.get("bathroom")
    drawing_room = request.POST.get("drawing_room")
    data=house(
        name=name,
        room=room,
        kitchen=kitchen,
        bathroom=bathroom,
        drawing_room=drawing_room
    )
    data.save()
    b='your data has been sent sir you can go and check'
    return render(request,'index.html',{'b':b})