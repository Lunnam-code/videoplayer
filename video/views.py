from django.shortcuts import render
from . models import Video

def index(request):
  if request.method == "GET":
    di = Video.objects.all()
    context = {
      'di':di,
    }
    return render(request,'index.html',context)

