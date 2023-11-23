from django.shortcuts import render

# Create your views here.
def forloop(request):

    d={'name':{'bhuvi','venkey*2','pavan'}}

    return render(request,'forloop.html',d)
