from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.contrib.auth.decorators import login_required
import requests
import json
# Create your views here.

def index(request):
    return render(request,'blog/calendar.html')
    
def info(request):
    response=requests.get('https://skillup-team-14.cxgok3weok8n.ap-south-1.rds.amazonaws.com')
    info=response.json()
    return render(request, 'blog/info.html',info)
  

def home(request):
    context={
        'posts':Post.objects.all()
    }
    #token = requests.get("https://cosc-team-14-restapi.herokuapp.com/login",data={'username':'HODID','password':'PASS'})
    #token=token.json()['access_token']
    #data=requests.get("https://cosc-team-14-restapi.herokuapp.com/hod_register",headers={'Authorization':Bearer{}'.'})
    ##response = requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register')
   # transfor the response to json objects
    ##todos = response.json()
    ##print(todos)
    ##return render(request, "blog/home.html", {"todos": todos})
    
    return render(request, 'blog/home.html',context)



def about(request):
    if(t!=''):
       return render(request, 'blog/about.html',{'title':'About'})
    else:
        return redirect('login')
    
    
def applyleave(request):
    if(t!=''):
       return render(request,'blog/applyleave.html')
    else:
        return redirect('login')
    

def table(request):
    if(t!=''):
       return render(request,'blog/table.html')
    else:
        return redirect('login')


def civil(request):
    return render(request,'blog/details/civil.html')

def mech(request):
    return render(request,'blog/details/mech.html')

def bio(request):
    return render(request,'blog/details/bio.html')
    
def ce(request):
    return render(request,'blog/details/ce.html')

def chem(request):
    return render(request,'blog/details/chem.html')

def cse(request):
    return render(request,'blog/details/cse.html')

def ece(request):
    return render(request,'blog/details/ece.html')

def eee(request):
    return render(request,'blog/details/eee.html')

def eng(request):
    return render(request,'blog/details/eng.html')

def it(request):
    return render(request,'blog/details/it.html')

def management(request):
    return render(request,'blog/details/management.html')

def math(request):
    return render(request,'blog/details/math.html')

def mca(request):
    return render(request,'blog/details/mca.html')

def phy(request):
    return render(request,'blog/details/phy.html')

def phyedu(request):
    return render(request,'blog/details/phyedu.html')


    



