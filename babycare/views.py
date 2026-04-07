from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime
# import pycurl
from urllib.parse import urlencode
from .models import *

def first(request):
    sel=services.objects.all()
                                                                                                                                                                                                  
    return render(request,'index.html',{'result':sel})

def index(request):
    sel=services.objects.all()
    
    return render(request,'index.html',{'result':sel})




def parentreg(request):
    return render(request,'register.html')

def addparent(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        district=request.POST.get('district')
        email=request.POST.get('email')
        password=request.POST.get('password')

        cus=parent_reg(name=name,mname=mname,lname=lname,address=address,district=district,email=email,password=password)
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})

def dcare(request):
    return render(request,'dcare.html')

def adddcare(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        district=request.POST.get('district')
        email=request.POST.get('email')
        password=request.POST.get('password')
       

        cus=dreg(name=name,address=address,district=district,email=email,password=password)
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    
def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif parent_reg.objects.filter(email=email,password=password).exists():
        userdetails=parent_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name

            request.session['uemail'] = email

            request.session['cus'] = 'cus'


            return render(request,'index.html')

    elif dreg.objects.filter(email=email,password=password).exists():
        userdetails=dreg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['did'] = userdetails.id
            request.session['dname'] = userdetails.name

            request.session['demail'] = email

            


            return render(request,'index.html')

        

    # elif wrkregg.objects.filter(email=email,password=password,status='approved').exists():
    #     userdetails=wrkregg.objects.get(email=request.POST['email'], password=password)
    #     if userdetails.password == request.POST['password']:
    #         request.session['wid'] = userdetails.id
    #         request.session['wname'] = userdetails.name

    #         request.session['wemail'] = email



    #         return render(request,'index.html')

    else:
        return render(request, 'login.html')
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def babysitterr(request):
    return render(request,'babysitter.html')

def addsitter(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')

        cus=babysitter(name=name,mname=mname,lname=lname,address=address,age=age,gender=gender,phone=phone,daycare_id=request.session['did'])
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    
def dctr(request):
    return render(request,'doctor.html')

def adddctr(request):
    if request.method=="POST":  
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        designation=request.POST.get('designation')

        cus=doctor(name=name,mname=mname,lname=lname,address=address,email=email,gender=gender,phone=phone,designation=designation,daycare_id=request.session['did'])
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    

    
def babyenv(request):
    sel=dreg.objects.all()
    return render(request,'enrollment.html',{'result':sel})

def addbaby(request):
    if request.method=="POST":
        pid=request.session['uid']
        date=request.POST.get('date')
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        description =request.POST.get('description')
        status =request.POST.get('status')
        daycare =request.POST.get('daycare')
      

        cus=baby_enroll(pid=pid,date=date,name=name,age=age,gender=gender,description=description,status=status,daycare=daycare)
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    

def viewbabies(request):
    sel=baby_enroll.objects.filter(daycare=request.session['did'])
    user= parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'viewenv.html',{'result':sel})  

def babyinfo(request,id):
    sel=baby_enroll.objects.get(id=id)
    
    return render(request,'babyinfo.html',{'result':sel})


def addbabyinfo(request):
    if request.method=="POST":
      
        bname=request.POST.get('bname')
        date=request.POST.get('date')
        description=request.POST.get('description')

        cus=baby_info(bname=bname,description=description,date=date)
        cus.save()
        return render(request,'index.html', {'message2':' successfully added'})


# def mark_attendance(request):
#     sel=baby_enroll.objects.filter(daycare=request.session['did'])
#     return render(request,'mark_attendance.html',{'result':sel})

def mark_attendance(request):
    sel=baby_enroll.objects.filter(status='accepted',daycare=request.session['did'])
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'mark_attendance.html',{'result':sel})

def mark(request,id):
    sel=baby_enroll.objects.get(id=id)
    return render(request,'attendance.html',{'result':sel})

def addattendance(request):
    if request.method=="POST":
        b_id=request.POST.get('b_id')
        p_id=request.POST.get('p_id')
        date=request.POST.get('date')
        status=request.POST.get('status')

        cus=attendance(b_id=b_id,status=status,p_id=p_id,date=date)
        cus.save()
        return render(request,'index.html', {'message2':' successfully Added'})
    


def service(request,id):
    sel=baby_enroll.objects.get(id=id)
    return render(request,'service.html',{'result':sel})


def addservice(request):
    if request.method=="POST":
        b_id=request.POST.get('b_id')
        p_id=request.POST.get('p_id')
        name=request.POST.get('name')
        typee=request.POST.get('typee')
        description=request.POST.get('description')
      

        cus=services(b_id=b_id,p_id=p_id,name=name,typee=typee,description=description,daycare_id=request.session['did'])
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})

def babyaccept(request,id):
    sel=baby_enroll.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(viewbabies)

def babyreject(request,id):
    sel=baby_enroll.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(viewbabies)

def viewdoctors(request):
    sel=doctor.objects.filter(daycare_id=request.session['did'])
    return render(request,'viewdoctors.html',{'result':sel})
 
def deletedoctor(request,id):
	emp=doctor.objects.get(pk=id)
	emp.delete()
	return redirect(viewdoctors)

def viewservices(request):
    sel=services.objects.all()
    return render(request,'viewservices_admin.html',{'result':sel})

def deleteservice(request,id):
	emp=services.objects.get(pk=id)
	emp.delete()
	return redirect(viewservices)

def viewbabysitters(request):
    sel=babysitter.objects.filter(daycare_id=request.session['did'])
    return render(request,'viewbabysitters.html',{'result':sel})

def deletesitter(request,id):
	emp=babysitter.objects.get(pk=id)
	emp.delete()
	return redirect(viewbabysitters)


def nutritionist(request):
    return render(request,'nutritionist.html')

def addnutritionist(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')

        cus=nutritionists(name=name,mname=mname,lname=lname,address=address,age=age,gender=gender,phone=phone,daycare_id=request.session['did'])
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    
def viewnutritionist(request):
    sel=nutritionists.objects.filter(daycare_id=request.session['did'])
    return render(request,'viewnutritionist.html',{'result':sel})

def deletenutritionist(request,id):
	emp=nutritionists.objects.get(pk=id)
	emp.delete()
	return redirect(viewnutritionist)

def viewsrc(request):
    sel=services.objects.filter(p_id=request.session['uid'])
    return render(request,'viewsrvies.html',{'result':sel})

def view_doctors(request):
    sel=doctor.objects.all()
    return render(request,'view_doctors.html',{'result':sel})

def view_babysitters(request):
    sel=babysitter.objects.all()
    return render(request,'view_babysitters.html',{'result':sel})

def view_nutritionist(request):
    sel=nutritionists.objects.all()
    return render(request,'view_nutritionist.html',{'result':sel})

def feedback(request):
    return render(request,'feedback.html')

def addfeedback(request):
    if request.method=="POST":
        pid=request.session['uid']
        feedback=request.POST.get('feedback')
  
        cus=feedbacks(pid=pid,feedback=feedback)
        cus.save()
        return render(request,'index.html')
    
def v_feedback(request):
    sel=feedbacks.objects.all()
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'view_feedback.html',{'result':sel})

def reqsitter(request,id):
    sel=babysitter.objects.get(id=id)
    return render(request,'requestsitter.html',{'result':sel})

def addreqsitter(request):
    if request.method=="POST":
        p_id=request.session['uid']
        name=request.POST.get('name')
        bs_id=request.POST.get('bs_id')
        location=request.POST.get('location')
        date_frm=request.POST.get('date_frm')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        date_to=request.POST.get('date_to')
        message=request.POST.get('message')
        status=request.POST.get('status')
        daycare_id=request.POST.get('daycare_id')

        cus=sitter_request(p_id=p_id,status=status,name=name,bs_id=bs_id,location=location,date_frm=date_frm,age=age,gender=gender,date_to=date_to,message=message,daycare_id=daycare_id)
        cus.save()
        return render(request,'index.html', {'message2':' successfully Requested'})
    
def v_reqsitter(request):
    sel=sitter_request.objects.filter(daycare_id=request.session['did'])
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.p_id)==str(j.id):
                i.p_id=j.name
    return render(request,'v_requestsitter.html',{'result':sel})

def reqaccept(request,id):
    sel=sitter_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqsitter)

def reqreject(request,id):
    sel=sitter_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqsitter)

def view_reqsitter(request):
    sel=sitter_request.objects.filter(p_id=request.session['uid'])
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.p_id)==str(j.id):
                i.p_id=j.name
    return render(request,'view_requestsitter.html',{'result':sel})

def reqdoctor(request,id):
    sel=doctor.objects.get(id=id)
    return render(request,'requestdoctor.html',{'result':sel})

def addreqdoctor(request):
    if request.method=="POST":
        p_id=request.session['uid']
        d_id=request.POST.get('d_id')
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        status=request.POST.get('status')
        basicpay=request.POST.get('basicpay')
        daycare_id=request.POST.get('daycare_id')

        cus=doctor_request(p_id=p_id,d_id=d_id,status=status,name=name,location=location,date=date,age=age,gender=gender,message=message,basicpay=basicpay,daycare_id=daycare_id)
        cus.save()
        return render(request,'index.html', {'message2':' successfully Requested'})
    
def reqnutri(request,id):
    sel=nutritionists.objects.get(id=id)
    return render(request,'requestnutri.html',{'result':sel})

def addreqnutri(request):
    if request.method=="POST":
        p_id=request.session['uid']
        n_id=request.POST.get('n_id')
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        status=request.POST.get('status')
        basicpay=request.POST.get('basicpay')
        daycare_id=request.POST.get('daycare_id')

        cus=nutrition_request(p_id=p_id,n_id=n_id,status=status,name=name,location=location,date=date,age=age,gender=gender,message=message,basicpay=basicpay,daycare_id=daycare_id)
        cus.save()
    return render(request,'index.html', {'message2':' successfully Requested'})
    
def v_reqdoctor(request):
    sel=doctor_request.objects.filter(daycare_id=request.session['did'])
    user=doctor.objects.all()
    for i in sel:
        for j in user:
            if str(i.d_id)==str(j.id):
                i.d_id=j.name
    return render(request,'v_requestdoctor.html',{'result':sel})

def d_reqaccept(request,id):
    sel=doctor_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqdoctor)

def d_reqreject(request,id):
    sel=doctor_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqdoctor)

def v_reqnutritionist(request):
    sel=nutrition_request.objects.filter(daycare_id=request.session['did'])
    user=nutritionists.objects.all()
    for i in sel:
        for j in user:
            if str(i.n_id)==str(j.id):
                i.n_id=j.name
    return render(request,'v_requestnutritionist.html',{'result':sel})

def n_reqaccept(request,id):
    sel=nutrition_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqnutritionist)

def n_reqreject(request,id):
    sel=nutrition_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqnutritionist)

def mark_attendance(request):
    sel=baby_enroll.objects.filter(status='accepted')
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'mark_attendance.html',{'result':sel})

def mark(request,id):
    sel=baby_enroll.objects.get(id=id)
    return render(request,'attendance.html',{'result':sel})

def addattendance(request):
    if request.method=="POST":
        b_id=request.POST.get('b_id')
        p_id=request.POST.get('p_id')
        date=request.POST.get('date')
        status=request.POST.get('status')

        cus=attendance(b_id=b_id,status=status,p_id=p_id,date=date)
        cus.save()
        return render(request,'index.html', {'message2':' successfully Added'})
    
def view_requests(request):
    user=request.session['uid']
    sel=doctor_request.objects.filter(id=user)
    sel1=nutrition_request.objects.filter(id=user)
    return render(request,'view_requests.html',{'result':sel,'result1':sel1})

"""from django.shortcuts import render, get_object_or_404
from .models import doctor_request, nutrition_request, payments

def payment(request):
    user = request.session.get('uid')
    sel = doctor_request.objects.filter(status='accepted', p_id=user)
    sel1 = nutrition_request.objects.filter(status='accepted', p_id=user)
    return render(request, 'payments.html', {'result': sel, 'result1': sel1})

def dpay(request, id):
    sel = get_object_or_404(doctor_request, id=id)
    return render(request, 'pay.html', {'result': sel})

def addpay(request):
    if request.method == "POST":
        s_id = request.POST.get('s_id')
        basicpay = request.POST.get('basicpay')
        name = request.POST.get('name')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')

        cus = payments(s_id=s_id, basicpay=basicpay, name=name, date=date, cvv=cvv)
        cus.save()
        return render(request, 'index.html', {'message2': 'Successfully Paid'})

def pay(request, id):
    sel = get_object_or_404(nutrition_request, id=id)
    return render(request, 'pay.html', {'result': sel})"""



from django.shortcuts import render, get_object_or_404, redirect
from .models import doctor_request, nutrition_request, payments

def payment(request):
    user = request.session.get('uid')
    sel = doctor_request.objects.filter(status='accepted', p_id=user)
    sel1 = nutrition_request.objects.filter(status='accepted', p_id=user)
    return render(request, 'payments.html', {'result': sel, 'result1': sel1})

def dpay(request, id):
    sel = get_object_or_404(doctor_request, id=id)
    return render(request, 'pay.html', {'result': sel})

def addpay(request):
    if request.method == "POST":
        s_id = request.POST.get('s_id')
        basicpay = request.POST.get('basicpay')
        name = request.POST.get('name')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')

        cus = payments(s_id=s_id, basicpay=basicpay, name=name, date=date, cvv=cvv)
        cus.save()
        return render(request, 'index.html', {'message2': 'Successfully Paid'})
    else:
        return redirect('payment')

def pay(request, id):
    sel = get_object_or_404(nutrition_request, id=id)
    return render(request, 'pay.html', {'result': sel})



# from django.shortcuts import render, get_object_or_404
# from .models import doctor_request, nutrition_request, payments

# def payment(request):
#     user = request.session['uid']
#     sel = doctor_request.objects.filter(status='accepted', p_id=user)
#     sel1 = nutrition_request.objects.filter(status='accepted', p_id=user)
#     return render(request, 'payments.html', {'result': sel, 'result1': sel1})

# def dpay(request, id):
#     sel = get_object_or_404(doctor_request, id=id)
#     return render(request, 'pay.html', {'result': sel})

# def addpay(request):
#     if request.method == "POST":
#         s_id = request.POST.get('s_id')
#         basicpay = request.POST.get('basicpay')
#         name = request.POST.get('name')
#         date = request.POST.get('date')
#         cvv = request.POST.get('cvv')

#         cus = payments(s_id=s_id, basicpay=basicpay, name=name, date=date, cvv=cvv)
#         cus.save()
#         return render(request, 'index.html', {'message2': 'Successfully Paid'})

# def pay(request, id):
#     sel = get_object_or_404(nutrition_request, id=id)
#     return render(request, 'pay.html', {'result': sel})


# def payment(request):
#     user=request.session['uid']
#     sel=doctor_request.objects.filter(status='accepted',id=user)
#     sel1=nutrition_request.objects.filter(status='accepted',id=user)
#     return render(request,'payments.html',{'result':sel,'result1':sel1})

# def dpay(request,id):
#     sel=doctor_request.objects.get(id=id)
#     return render(request,'pay.html',{'result':sel})

# def pay(request,id):
#     sel=nutrition_request.objects.get(id=id)
#     return render(request,'pay.html',{'result':sel})

# def addpay(request):
#     if request.method=="POST":
#         s_id=request.POST.get('s_id')
#         basicpay=request.POST.get('basicpay')
#         name=request.POST.get('name')
#         date=request.POST.get('date')
#         cvv=request.POST.get('cvv')

#         cus=payments(s_id=s_id,basicpay=basicpay,name=name,date=date,cvv=cvv)
#         cus.save()
#         return render(request,'index.html', {'message2':' successfully Paid'})
    
def vac(request):
    return render(request,'vaccine.html')

def addvac(request):
    if request.method=="POST":
        p_id=request.session['uid']
        bname=request.POST.get('bname')
        vaccine=request.POST.get('vaccine')
        date=request.POST.get('date')
        description=request.POST.get('description')

        cus=vacinations(p_id=p_id,bname=bname,vaccine=vaccine,description=description,date=date)
        cus.save()
        return render(request,'index.html', {'message2':' successfully added'})
    
    
def viewvac(request):
    sel=vacinations.objects.all()
    return render(request,'view_vaccine.html',{'result':sel})


    
def view_babyinfo(request):
    sel=baby_info.objects.all()
    user=baby_enroll.objects.all()
    for i in sel:
        for j in user:
            if str(i.bname)==str(j.id):
                i.bname=j.name
    return render(request,'view_babyinfo.html',{'result':sel})

def view_attendence(request):
    user1=request.session['uid']
    sel=attendance.objects.filter(p_id=user1)
    user=baby_enroll.objects.all()
    for i in sel:
        for j in user:
            if str(i.b_id)==str(j.id):
                i.b_id=j.name
    return render(request,'view_attendance.html',{'result':sel})

def profile(request):
    a=baby_enroll.objects.get(id=request.session['user_id'])
    return render(request,'profile.html',{'res':a})

def markattendance(request):
    sel=baby_enroll.objects.filter(status='accepted')
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'markattendance.html',{'result':sel})

def staff(request):
    return render(request,'staff.html')

def addstaff(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        cus=staff(name=name,email=email,password=password,phone=phone)
        cus.save()
    return render(request,'staff.html', {'message1':' successfully Registered'})

def feed(request):
    return render(request,'feed.html')

def addfeed(request):
    if request.method=="POST":
        pid=request.session['uid']
        feedback=request.POST.get('feedback')
  
        cus=feedbacks(pid=pid,feedback=feedback)
        cus.save()
        return render(request,'index.html')

def viewdcare(request):
    sel=dreg.objects.all()
    return render(request,'viewdcare.html',{'result':sel})

def deletedcare(request,id):
	emp=dreg.objects.get(pk=id)
	emp.delete()
	return redirect(viewdcare)

def viewuser(request):
    sel=parent_reg.objects.all()
    return render(request,'viewuser.html',{'result':sel})


