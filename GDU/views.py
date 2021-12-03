from django.shortcuts import render

def autorizacion(request): 
    return render(request,'autorizacion.html')

def denuncias(request):
    return render(request,'denuncias.html')