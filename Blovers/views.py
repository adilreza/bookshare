from django.shortcuts import render
from .models import registrationList
from .models import userimage
from .models import publicallpost

from django.conf import settings
from django.conf.urls.static import static

from django.utils import timezone
import datetime
from datetime import datetime
#test here


#test here
dynamicmail=''





# Create your views here.
def home(request):
    dynamicmail=request.session.get('wow','')
    return render(request, 'index.html')

def registration(request):
	if request.method=="GET":
		return render(request, 'registration.html')
	elif request.method=="POST":
            image=request.FILES['picture']
            
            uname=request.POST.get('fullname')
            umail=request.POST.get('gmail')
            upass1=request.POST.get('pass1')
            upass2=request.POST.get('pass2')
            uvarsity=request.POST.get('varsity')
            uexpert=request.POST.get('expert')
            now = datetime.now()
            sql=userimage(usermail=umail, userimage=image, time=now)
            sql.save()
        
            
		
            sql=registrationList(username=uname,usermail=umail,pass1=upass1,pass2=upass2,varsity=uvarsity,lovebooktype=uexpert, userimage=image, time=now)
            sql.save()
		
            contextt="ok"
            makedictionary={
			'msgreg':contextt
		      }
            return render(request, 'registration.html', context=makedictionary)
	else:
		return render(request, 'index.html')



def login(request):
	if request.method=="GET":
		return render(request, 'login.html')
	elif request.method=="POST":
		ugmail=request.POST.get('loggmail')
		upass=request.POST.get('logpass')
		contexttt=registrationList.objects.filter(usermail=ugmail)
		
		if contexttt.count()==0:
			contextt="ok"
			makedictionary={
			'msgrlog2':contextt
			}
			return render(request, 'login.html',context=makedictionary)
		
		contextt="ok"
		makedictionary={
			'msgrlog':contextt
		}
		
		for i in contexttt:
			if(i.pass1==upass):
				request.session['wow']=request.POST['loggmail']
				contexttt2=publicallpost.objects.filter(usermail=ugmail).order_by('id').reverse()
				context="yes yes"
				makedictionary={
				'alluserdata':contexttt,
                'bookpostall':contexttt2
				}
				return render(request, 'userpanel.html',context=makedictionary)
			else:
				contextt="ok"
				makedictionary={
				'msgrlog2':contextt
				}
				return render(request, 'login.html',context=makedictionary)
		
				
	else:
		contextt="no"
		makedictionary={
		'msgrlog2':contextt
		}
		return render(request, 'registration',context=makedictionary)
		
		
		
def test(request):
	return render(request, 'test.html')


def mainpage(request):
    if request.method=="GET":
        dynamicmail=request.session.get('wow','')
        print(dynamicmail)
        if(dynamicmail==""):
            return render(request, 'index.html')
        else:
            allpublicpost=publicallpost.objects.all().order_by('id').reverse()
            makedictionary={
                'allpost':allpublicpost
            }
            return render(request, 'mainpage.html',context=makedictionary)

def userpanel(request):
    if request.method=="GET":
        dynamicmail=request.session.get('wow','')
        contexttt=registrationList.objects.filter(usermail=dynamicmail)
        contexttt2=publicallpost.objects.filter(usermail=dynamicmail).order_by('id').reverse()
        makedictionary={
				'alluserdata':contexttt,
                'bookpostall':contexttt2
				}
        if(dynamicmail==""):
            return render(request, 'index.html')
        else:
            return render(request, 'userpanel.html',context=makedictionary)
        
def logout(request):
    if request.method=="GET":
        request.session.pop('wow')
        return render(request, 'index.html')
        
    
    
def postabook(request):
    if request.method=="GET":
        return render(request, 'postabook.html')
    elif request.method=="POST":
        return render(request, 'userpanel.html')
    
def uploadonline(request):
    if request.method=='GET':
        return render(request, 'userpanel.html')
    if request.method=="POST":
        usermail=request.POST.get('usermail')
        booktitle=request.POST.get('booktitle')
        bookwritter=request.POST.get('bookwritter')
        userphone=request.POST.get('userphone','')
        usercomment=request.POST.get('usercomment')
        usercontactinfo=request.POST.get('usercontactinfo')
        bookprice=request.POST.get('bookprice','')
        useroption=request.POST.get('useroption')
        usertimelinecheck=request.POST.get('usertimelinecheck')
        bookimage=request.FILES['bookimage']
        bookview=0
        now = datetime.now()
        if usertimelinecheck!="":
            msg="none"
        else:
            msg="yes"
        makedictionary={
            'confirmation':msg
        }
        sql=publicallpost(usermail=usermail,booktitle=booktitle,bookwritter=bookwritter,userphone=userphone,usercomment=usercomment,usercontactinfo=usercontactinfo,bookprice=bookprice,useroption=useroption,bookimage=bookimage,bookview=bookview, time=now)
        sql.save()
        
        return render(request, 'postabook.html', context=makedictionary)

def details_selected(request):
    if request.method=='GET':
            allpublicpost=publicallpost.objects.all().order_by('id').reverse()
            makedictionary={
                'allpost':allpublicpost
            }
            return render(request, 'mainpage.html',context=makedictionary)
        
    elif request.method=='POST':
        uniqid=request.POST.get('uid')
        print(uniqid)
        
        specific_data=publicallpost.objects.filter(id=uniqid)
        oneentry=publicallpost.objects.get(id=uniqid)
        oneentry.bookview=oneentry.bookview+1
        oneentry.save()
        
        makedictionary={
            'selected_data':specific_data
        }
        return render(request, 'details_selected.html', context=makedictionary)