
from bdb import effective
from decimal import Underflow
from django.db import models



# Create your models here.


    
class CreateStockGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)
    
class CreateStockCateg(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    
class CreateGodown(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
      
class CreateEmployeeGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    
class Price_level(models.Model):
    number=models.IntegerField()
    
class UnitCrt(models.Model):
    type=models.CharField(max_length=100,null=True)
    symbol=models.CharField(max_length=20,null=True)
    formal_name=models.CharField(max_length=50,null=True)
    uqc=models.CharField(max_length=50,null=True)
    decimal=models.IntegerField(null=True)
    first_unit=models.CharField(max_length=50,null=True)
    conversion=models.CharField(max_length=30,null=True)
    second_unit=models.CharField(max_length=30,null=True)
    
class pancin(models.Model):
    pan=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)
    
class cost(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    
class employee_crt(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    doj=models.CharField(max_length=30)
    salary=models.CharField(max_length=50)
    empno=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    function_name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    bld_grp=models.CharField(max_length=20)
    father_mother=models.CharField(max_length=20)
    spouse=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phn=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    bank=models.CharField(max_length=50)
    incometax=models.CharField(max_length=20)
    adhar=models.CharField(max_length=20)
    uan=models.CharField(max_length=20)
    pf=models.CharField(max_length=20)
    pr=models.CharField(max_length=20)
    esi=models.CharField(max_length=20)

class bank(models.Model):
    accno=models.CharField(max_length=50)
    ifsc_Code=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    
class bank_crt(models.Model):
    accno=models.CharField(max_length=50)
    ifsc_Code=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
             
class attendance_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=50,null=True)
    attendance=models.CharField(max_length=50,null=True)
    period=models.CharField(max_length=50,null=True)
    units=models.CharField(max_length=50,null=True)
    
class payhead_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    
class salary_crt(models.Model):
    name=models.CharField(max_length=50,null=True)
    alias=models.CharField(max_length=50,null=True)
    date=models.CharField(max_length=100,null=True)
    pay_head_name=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    pay_head_type=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    
class payroll_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    allias=models.CharField(max_length=100,null=True)
    voucher_type=models.CharField(max_length=100,null=True)
    abbreviation=models.CharField(max_length=100,null=True)
    activate_voucher=models.CharField(max_length=100,null=True)
    voucher_numbering_method=models.CharField(max_length=100,null=True)
    effective_dates=models.CharField(max_length=100,null=True)
    zero_val_transactions=models.CharField(max_length=100,null=True)
    optional_voucher=models.CharField(max_length=100,null=True)
    narration_voucher=models.CharField(max_length=100,null=True)
    ledger_narration=models.CharField(max_length=100,null=True)
    print_voucher=models.CharField(max_length=100,null=True)
    classs=models.CharField(max_length=100,null=True)
    
class stock_item_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    
class Price_level_crt(models.Model):
    number=models.CharField(max_length=100,null=True)
    
    
    
class allocate_stock(models.Model):
    allocate=models.CharField(max_length=100,null=True)
    for_allocate=models.CharField(max_length=100,null=True)
    godown=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    amount=models.CharField(max_length=100,null=True)
    
    
    