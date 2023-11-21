from django.shortcuts import render

# Create your views here.

def boy(request):
    return render(request,'boy.html')

def girlfriend(request):
    return render(request,'girlfriend.html')


# def girlbesti(request):
#     return render(request,'girlbesti.html')
