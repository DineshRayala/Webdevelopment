from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import requests
import json

from django.http import HttpResponse,JsonResponse
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            data=request.POST.copy()
            HODID =int(form.cleaned_data.get('hod_id'))
            HODNAME=str(form.cleaned_data.get('username')) 
            DEPTNO =int(form.cleaned_data.get('department_number'))
            DESG =str(form.cleaned_data.get('designation'))
            EMAIL =str(form.cleaned_data.get('email'))
            CONTACT=str(form.cleaned_data.get('phone')) 
            ADDRESS =str(form.cleaned_data.get('address'))
            PASS =str(form.cleaned_data.get('password1'))
            data={"HODID":HODID,"HODNAME":HODNAME,"DEPTNO":DEPTNO,"DESG":DESG,"EMAIL":EMAIL,"CONTACT":CONTACT,"ADDRESS":ADDRESS,"PASS":PASS}
            resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/hod_register',data)
            messages.success(request, f'Your account has been created! You are now able to log in')
            render(request,'users/login.html')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
def home(request):
    if (request.method)=="POST":
        HODNAME=request.POST['Username']
        PASS =request.POST['pwd']
        det = { "HODNAME":HODNAME,"PASS":PASS}
        token = requests.post("https://cosc-team-14-restapi.herokuapp.com/hod_login",det)
        '''token=token.json()['access_token']
        data=requests.get("https://cosc-team-14-restapi.herokuapp.com/hod_register",headers={'Authorization':'Bearer{}'.format(token)},data={'routeId':48})
        return HttpResponse(data)'''
        global p
        p = token.json()
        #return render(request,'users/profile.html',{'users':p})
        if(len(p)!=2):
              messages.success(request,f'Invalid Credentials')
              return render(request,'users/login.html')
            #return HttpResponse(p)
        else:
            global t
            global q
            t=token.json()[" access_token "]
            q = token.json()["hodname"]
            data={"HODNAME":q}
            resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',data,headers={'Authorization':f'Bearer {t}'})
            res=resp.json()
            return render(request,'users/profile.html',{'users':t,'details':res})
        '''else:
            data=requests.get("https://cosc-team-14-restapi.herokuapp.com/hod_register",headers={'Authorization':f'Bearer{p}'})
             
            res = data.json()
            context={'data': res,}
            return redirect('home')'''
        '''elif (request.method)=="GET":
        if(p):
            if(p=="Invalid credentials"):
                print('invalid')
                context={'data':"INVALID CREDENTIALS"}
                return render(request,'login1.html',context)
            #return HttpResponse(p)
            else:'''
        



def profile(request):
    #onclick="myFunction()"
    #token=token.json()['access_token']
    #data=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',headers={'Authorization':'Bearer{}'.format(token)},data={'routeId':48})

    #print(data.json)
    #return render(request,'users/profile.html',{'data':t})
    if(t!=''):
        data={"HODNAME":q}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',data,headers={'Authorization':f'Bearer {t}'})
        res=resp.json()
        
        return render(request,'users/profile.html',{'users':t,'details':res})
    else:
        return redirect('login')
def index(request):
    data=request.GET.get('id')

    return HttpResponse(data)

def about1(request):
    global x
    x=request.GET.get("checkhistory")
    y=request.GET.get("leave_id")
    z=request.GET.get("checkhistory1")
    p=request.GET.get("approval")
    c=request.GET.get("modify")
    if(x!=None and z!=None):
        data={"EMPID":x}
        data2={"LEAVE_ID":z}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/emp_register',data,headers={'Authorization':f'Bearer {t}'})
        ro=resp.json()
        resp1=requests.get('https://cosc-team-14-restapi.herokuapp.com/leaveidinfo',data2,headers={'Authorization':f'Bearer {t}'})
        ro1=resp1.json()
        return render(request,'users/about1.html',{'values':ro,'values1':ro1,"leave_id":y})
    if(x!=None):
        data={"EMPID":x}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/emp_register',data,headers={'Authorization':f'Bearer {t}'})
        ro=resp.json()
        return render(request,'users/about1.html',{'values':ro,"leave_id":y})
    if(z!=None):
        data={"LEAVE_ID":z}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/leaveidinfo',data,headers={'Authorization':f'Bearer {t}'})
        ro1=resp.json()
        print(ro1)
        return render(request,'users/about1.html',{'values1':ro1,"leave_id":z})
    if(p!=None and c!=None):
        
        data={"LEAVE_ID":p}
        
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/leaveapproval',data,headers={'Authorization':f'Bearer {t}'})
        info=resp.json()
        print(info)
        
        if(info[0]['LEAVE_STAT']==2):

            if c=="ACCEPTED":
              data={"LEAVE_ID":p,"LEAVE_MSG":c,"LEAVE_STAT":"1"  }
            else:
                data={"LEAVE_ID":p,"LEAVE_MSG":c,"LEAVE_STAT":"0"  }
            resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/leaveapprovalupdate',data,headers={'Authorization':f'Bearer {t}'})
            info=resp.json()
            '''print(info)
            return HttpResponse(resp)'''
            messages.success(request, f'Modified leave status successfully')
            return render(request,'users/about1.html',{"info":info})
        return render(request,'users/about1.html',{"info":info})
    if (p!=None):
        data={"LEAVE_ID":p}
        
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/leaveapproval',data,headers={'Authorization':f'Bearer {t}'})
        info=resp.json()
        print(info)
        return render(request,'users/about1.html',{"info":info})

   
        
        
    else:
        return render(request, 'users/about1.html',{'title':'About'})
    '''if(p!=''):
       return render(request, 'users/about1.html',{'title':'About','users':p})
    else:
        return redirect('login')'''
    
    
def applyleave(request):
    
    if(t!=''):
       return render(request,'blog/applyleave.html',{'users':t})
    else:
        return redirect('login')
    

def table1(request):
    '''resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/deptleave',headers={'Authorization':f'Bearer {t}'})
    ro=resp.json()
    return render(request,'users/table1.html',{'values':ro})'''
    #return render(request,'users/table1.html')
    x=request.GET.get("checkhistory")

    if(x!=None):
        data={"DEPTNO":x}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/deptleave',data,headers={'Authorization':f'Bearer {t}'})
        ro=resp.json()
        return render(request,'users/table1.html',{'values':ro})

    else:
        return render(request, 'users/table1.html')
    '''if(p!=''):
       return render(request, 'users/about1.html',{'title':'About','users':p})'''
    
def home3(request): 
    LEAVE_MSG=request.GET.get("LEAVE_MSG")
    LEAVE_ID=request.GET.get("LEAVE_ID")
    LEAVE_STAT=request.GET.get("LEAVE_STAT")
    data={"LEAVE_MSG":LEAVE_MSG,"LEAVE_ID":LEAVE_ID,"LEAVE_STAT":LEAVE_STAT}
    resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/leaveapproval',data,headers={'Authorization':f'Bearer {t}'})

    messages.success(request, f'Leave status updated')
    return render(request,'users/about1.html')
    


   

def calendar1(request):
    data={"EMPID":x}
    resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/empattendence',data,headers={'Authorization':f'Bearer {t}'})
    ro3=resp.json()
    
    return render(request,'users/cal.html',{'color':ro3})

def setleaves(request):
    EMPID=request.GET.get("checkhistory2")
    NOLEAVES=request.GET.get("checkhistory3")
    data={"EMPID":EMPID,"NOLEAVES":NOLEAVES}
    resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/updatebyhod',data,headers={'Authorization':f'Bearer {t}'})
    data={"EMPID":EMPID}
    resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/emp_register',data,headers={'Authorization':f'Bearer {t}'})
    ro=resp.json()
    messages.success(request, f'Number of leaves updated successfully')
    
    return render(request,'users/about1.html',{'values':ro})
    #return render(request,'users/about1.html')
def hi(request):
    return render(request,'users/cal.html')