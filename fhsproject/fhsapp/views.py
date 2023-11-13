from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from .forms import RegistrationForm
from .models import Registration,Order
import random
def userhomefunc(request):
    return render(request,"userhome.html")

def loginregisterpage(request):
    return render(request,"LoginRegister.html")

def registrationfunc(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Registration Successful"
            return render(request,"registration.html",{"form":form,"msg":msg})
        else:
            msg="Email or contact no. already exists"
            return render(request,"registration.html",{"form":form,"msg":msg})

    return render(request, "registration.html", {"form": form})

def checkuserlogin(request):
    emaild = request.POST["emailid"]
    pwd = request.POST["password"]

    flag = Registration.objects.filter(Q(email=emaild) & Q(password=pwd))
    print(flag)

    if flag:
        user = Registration.objects.get(email=emaild)
        print(user)
        print(user.id, user.fullname, user.username)  # other fields also
        request.session["uname"] = user.username
        request.session["uemail"]=user.email
        request.session["uphone"]=user.contact
        request.session["uid"]=user.id
        return render(request, "userhome.html",{"uname":user.username,"uid":user.id})
    else:
        msg = "Login Failed"
        return render(request, "LoginRegister.html", {"msg": msg})

def userhome(request):
    username = request.session["uname"]
    print(username)
    return render(request, "userhome.html", {"uname": username})

def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    email = request.POST["emailid"]
    pwd = request.POST["password"]

    if email == "koushiklakkuru@gmail.com" and pwd == "lvk":
        return render(request,"adminhome.html")
    elif email == "modembhanuprakash@gmail.com" and pwd == "mbp":
        return render(request,"adminhome.html")
    elif email == "saivenkateitakota@gmail.com" and pwd == "esv":
        return render(request,"adminhome.html")
    else:
        msg="Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})

def adminhomefunc(request):
    return render(request,"adminhome.html")

def viewusers(request):
    userdata=Registration.objects.all()
    usercount=Registration.objects.count()
    return render(request,"viewusers.html",{"users":userdata,"count":usercount})

def placeorder(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        userid=request.session['uid']
        user=Registration.objects.get(id=userid)
        order = Order(user=user,item_name=item_name, quantity=quantity)
        order.save()
        orderdata=Order.objects.all()
        username = request.session["uname"]
        userid=request.session["uid"]
        return render(request,"userhome.html",{"orderdata":orderdata,"uname": username,"uid":userid})

def logoutfunc(request):
    #Order.objects.all().delete()
    return render(request,"home.html")

def nonvegstarterspage(request):
    username = request.session["uname"]
    return render(request,"NonVegStarters.html", {"uname": username})


def vegstarterspage(request):
    username = request.session["uname"]
    return render(request,"VegStarters.html", {"uname": username})


def soupspage(request):
    username = request.session["uname"]
    return render(request,"Soups.html", {"uname": username})


def fishseafoodpage(request):
    username = request.session["uname"]
    return render(request,"FishSeaFood.html", {"uname": username})


def paymentpage(request):
    username = request.session["uname"]
    return render(request,"Payment.html", {"uname": username})

def maincoursepage(request):
    username = request.session["uname"]
    return render(request,"MainCourse.html", {"uname": username})

def noodlespage(request):
    username = request.session["uname"]
    return render(request,"Noodles.html", {"uname": username})

def saladspage(request):
    return render(request,"Salads.html")

def dessertspage(request):
    return render(request,"Desserts.html")

def bookroompage(request):
    return render(request,"BookRoom.html")

def btuserhome(request):
    username = request.session["uname"]
    userid=request.session['uid']
    return render(request, "userhome.html", {"uname": username,"uid":userid})

def changepassword(request):
    emaild=request.session["uemail"]
    return render(request,"changepassword.html",{"emaild":emaild})

def updatepassword(request):
    emaild=request.session["uemail"]
    opwd=request.POST["op"]
    npwd=request.POST["np"]
    flag = Registration.objects.filter(Q(email=emaild) & Q(password=opwd))
    if flag:
        Registration.objects.filter(email=emaild).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "changepassword.html", {"emaild":emaild,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "changepassword.html", {"emaild":emaild,"msg":msg})

def profilefunc(request):
    emaild=request.session["uemail"]
    flag=Registration.objects.filter(email=emaild).get()

    return render(request,"profile.html",{"userdet":flag})

def updateprofile(request):
    emaild = request.session["uemail"]
    flag = Registration.objects.filter(email=emaild).get()
    return render(request,"updateprofile.html",{"userdet":flag})

def checkupprofile(request):
    emaild = request.session["uemail"]
    mobile=request.session["uphone"]
    newfullname=request.POST['newfullname']
    newphonenum=request.POST['newphonenum']
    newdateofbirth=request.POST['newdateofbirth']
    newlocation=request.POST['newlocation']
    newusername=request.POST['newusername']
    flag = Registration.objects.filter(email=emaild).get()
    if newphonenum in Registration.objects.filter(contact=mobile):
        msg="Phone Number already exists"
        return render(request,"updateprofile.html",{"userdet":flag,"msg":msg})
    Registration.objects.filter(email=emaild).update(fullname=newfullname)
    Registration.objects.filter(email=emaild).update(contact=newphonenum)
    Registration.objects.filter(email=emaild).update(dateofbirth=newdateofbirth)
    Registration.objects.filter(email=emaild).update(location=newlocation)
    Registration.objects.filter(email=emaild).update(username=newusername)

    return render(request,"profile.html",{"userdet":flag})

def order_history(request, user_id):
    user = Registration.objects.get(id=user_id)
    user_orders = Order.objects.filter(user_id=user_id)
    """context = {
        'user': user,
        'user_orders': user_orders,
    }"""
    return render(request, 'order_history.html',{'user':user,'user_orders':user_orders})

def emailaskingpage(request):
    return render(request,"emailaskingpage.html")
def emailsend(request):
    otp = random.randint(100000, 999999)
    if request.method=='POST':
        emailadd=request.POST['emailadd']
        send_mail(
            'Enter the otp',
            'This is your otp'+str(otp),
            'koushiklakkuru@gmail.com',
            [emailadd],
            fail_silently=False,
        )
        return render(request,"otpaskingpage.html",{"emailadd":emailadd,"otp":otp})
def otpverify(request,otp):
    if request.method=='POST':
        givenotp=request.POST['givenotp']
        if int(otp)==int(givenotp):
            return render(request,"userhome.html")
        else:
            return HttpResponse("Otp is Incorrect")



