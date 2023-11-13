from django.urls import path
from . import views

urlpatterns=[
    path("userhome",views.userhomefunc,name="userhome"),
    path("registration",views.registrationfunc,name="registration"),
    path("LoginRegister", views.loginregisterpage, name="LoginRegister"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("userhome",views.userhome,name="userhome"),
    path("viewusers",views.viewusers,name="viewusers"),
    path("adminhome",views.adminhomefunc,name="adminhome"),
    path("place_order",views.placeorder,name="place_order"),
    path("logout",views.logoutfunc,name="logout"),
    path("NonVegStarters",views.nonvegstarterspage,name="NonVegStarters"),
    path("VegStarters",views.vegstarterspage,name="VegStarters"),
    path("Soups",views.soupspage,name="Soups"),
    path("FishSeaFood",views.fishseafoodpage,name="FishSeaFood"),
    path("Payment",views.paymentpage,name="Payment"),
    path("MainCourse",views.maincoursepage,name="MainCourse"),
    path("Noodles",views.noodlespage,name="Noodles"),
    path("Salads",views.saladspage,name="Salads"),
    path("Desserts",views.dessertspage,name="Desserts"),
    path("BookRoom",views.bookroompage,name="BookRoom"),
    path("btuserhome",views.btuserhome,name="btuserhome"),
    path("changepassword",views.changepassword,name="changepassword"),
    path("updatepassword",views.updatepassword,name="updatepassword"),
    path("profile",views.profilefunc,name="profile"),
    path("updateprofile",views.updateprofile,name="updateprofile"),
    path("checkupprofile",views.checkupprofile,name="checkupprofile"),
    path('order_history/<int:user_id>/', views.order_history, name='order_history'),
    path('emailaskingpage',views.emailaskingpage,name="emailaskingpage"),
    path('emailsend',views.emailsend,name="emailsend"),
    path('otpverify/<int:otp>/',views.otpverify,name="otpverify"),




]