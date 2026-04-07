from django.db import models

class parent_reg(models.Model):
    name=models.CharField(max_length=25)
    mname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class dreg(models.Model):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class babysitter(models.Model):
    name=models.CharField(max_length=25)
    mname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class doctor(models.Model):
    name=models.CharField(max_length=25)
    mname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class services(models.Model):
    name=models.CharField(max_length=25)
    typee=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    b_id=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class baby_enroll(models.Model):
    name=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    pid=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    status=models.CharField(max_length=25)
    daycare=models.CharField(max_length=25)

class nutritionists(models.Model):
    name=models.CharField(max_length=25)
    mname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class feedbacks(models.Model):
    pid=models.CharField(max_length=25)
    feedback=models.CharField(max_length=25)

class sitter_request(models.Model):
    name=models.CharField(max_length=25)
    bs_id=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    date_frm=models.CharField(max_length=25)
    date_to=models.CharField(max_length=25)
    message=models.CharField(max_length=25)
    status=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)
    
class doctor_request(models.Model):
    name=models.CharField(max_length=25)
    d_id=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    message=models.CharField(max_length=25)
    status=models.CharField(max_length=25)
    basicpay=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class nutrition_request(models.Model):
    name=models.CharField(max_length=25)
    n_id=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    message=models.CharField(max_length=25)
    status=models.CharField(max_length=25)
    basicpay=models.CharField(max_length=25)
    daycare_id=models.CharField(max_length=25)

class attendance(models.Model):
    b_id=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    status=models.CharField(max_length=25)

class payments(models.Model):
    s_id=models.CharField(max_length=25)
    basicpay=models.CharField(max_length=25)
    name=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    cvv=models.CharField(max_length=25)

class vacinations(models.Model):
    bname=models.CharField(max_length=25)
    vaccine=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    p_id=models.CharField(max_length=25)

class baby_info(models.Model):
    bname=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    date=models.CharField(max_length=25)

class staff(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

