from django.shortcuts import render

# Create your views here.
def services(request):
    context={'service':'active'}
    return render(request,'services/service.html',context)