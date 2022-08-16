
from configparser import LegacyInterpolation
from unicodedata import name
from django.shortcuts import render,redirect,HttpResponseRedirect

from TallyPrimeApp.models import CreateEmployeeGrp, CreateGodown, CreateStockCateg, CreateStockGrp, Price_level_crt, UnitCrt, Price_level, allocate_stock, attendance_crt, bank_crt,  employee_crt, pancin, payhead_crt, payroll_crt, salary_crt, stock_item_crt


# Create your views here.

def base(request):
    return render(request,'base.html')

def company(request):
    return render(request,'inventory_masters.html')

def stock_group(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_group')
    return render(request,'stock_group.html',{'und':und})

def stock_group_secondary(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_group')
    return render(request,'stock_group(secondary).html',{'und':und})
    
    

def stock_category_creation(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
    return render(request,'stock_category_creation.html',{'und':und})

def stock_category_secondary(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
        return redirect('stock_category_creation')
    return render(request,'stock_category(secondary).html',{'und':und})

    

def stock_items(request):
    cat=CreateStockCateg.objects.all()
    grp=CreateStockGrp.objects.all()
    unt=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        category=request.POST['category']
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=stock_item_crt(name=name,alias=alias,under=under,category=category,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional)
        crt.save()
    return render(request,'stock_items1.html',{'cat':cat,'grp':grp,'unt':unt})


def unit_creation(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        type=request.POST['type']
        symbol=request.POST['symbol']
        formal_name=request.POST['formal_name']
        uqc=request.POST['uqc']
        decimal=request.POST['decimal']
        first_unit=request.POST['first_unit']
        conversion=request.POST['conversion']
        second_unit=request.POST['second_unit']
        crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        crt.save()
    return render(request,'unit1.html',{'unit':unit})


def uqc(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')

def unit_creation_secondary(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        type=request.POST['type']
        symbol=request.POST['symbol']
        formal_name=request.POST['formal_name']
        uqc=request.POST['uqc']
        decimal=request.POST['decimal']
        first_unit=request.POST['first_unit']
        conversion=request.POST['conversion']
        second_unit=request.POST['second_unit']
        crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        crt.save()
    return render(request,'unit_creation(secondary).html',{'unit':unit})

def uqc_secondary(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')



def godown_alteration(request):
    gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
        gdcrt.save()
    return render(request,'godown_alteration.html',{'gd':gd})

def godown_secondary(request):
    gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
        gdcrt.save()
        return redirect('godown_alteration')
    return render(request,'godown(secondary).html',{'gd':gd})
    

def employee_group_creation(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group_creation.html',{'emp':emp})

def emloyee_group_secondary(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group(secondary).html',{'emp':emp})
    

def employee_creation(request):
    grp=CreateEmployeeGrp.objects.all()
    emp=employee_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        doj=request.POST['doj']
        salary=request.POST['salary']
        empno=request.POST['empno']
        designation=request.POST['designation']
        function_name=request.POST['function_name']
        location=request.POST['location']
        gender=request.POST['gender']
        dob=request.POST['dob']
        bld_grp=request.POST['bld_grp']
        father_mother=request.POST['father_mother']
        spouse=request.POST['spouse']
        address=request.POST['address']
        phn=request.POST['phn']
        email=request.POST['email']
        bank=request.POST['bank']
        incometax=request.POST['incometax']
        adhar=request.POST['adhar']
        uan=request.POST['uan']
        pf=request.POST['pf']
        pr=request.POST['pr']
        esi=request.POST['esi']
        crt=employee_crt(name=name,alias=alias,under_name=under_name,doj=doj,salary=salary,empno=empno,designation=designation,
                         function_name=function_name,location=location,gender=gender,dob=dob,bld_grp=bld_grp,father_mother=father_mother,
                         spouse=spouse,address=address,phn=phn,email=email,bank=bank,incometax=incometax,adhar=adhar,uan=uan,pf=pf,pr=pr,esi=esi)
        crt.save()
        request.session["name"]=name            
    return render(request,'employee_creation.html',{'emp':emp,'grp':grp})
    
def price_levels(request):
    if request.method=="POST":
        number=request.POST['number']
        crt=Price_level_crt(number=number)
        crt.save()
        return redirect('price_levels')
    price=Price_level_crt.objects.all()
    return render(request,'price_levels.html',{"price":price})

def pan_cin(request):
    pc=pancin.objects.all()
    if request.method=='POST':
        pan=request.POST['pan']
        cin=request.POST['cin']
        crt=pancin(pan=pan,cin=cin)
        crt.save()
    return render(request,'pan_cin.html')


# def show_emp(request):
#     show=EmplGrpCrt.objects.all()
#     return render(request,'show_details.html',{"show":show})

# def edit_emp(request,pk):
#     ed=EmplGrpCrt.objects.get(id=pk)
#     if request.method=='POST':
#         ed.name=request.POST['name']
#         ed.alias=request.POST['alias']
#         ed.under=request.POST['under']
#         ed.save()
#         return redirect('show_emp')
#     return render(request,'edit_emp.html',{'ed':ed})

# def delete(request,pk):
#     ed=EmplGrpCrt.objects.get(id=pk)
#     ed.delete()
#     return redirect('show_emp')

def pay_head(request):
    att=attendance_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        payhead_type=request.POST['payhead_type']
        under_name=request.POST['under_name']
        net_salary=request.POST['net_salary']
        pay_slip_name1=request.POST['pay_slip_name']
        currency_ledger=request.POST['currency_ledger']
        calculation_type=request.POST['calculation_type']
        crt=payhead_crt(name=name,alias=alias,payhead_type=payhead_type,under_name=under_name,net_salary=net_salary,pay_slip_name=pay_slip_name1,currency_ledger=currency_ledger,calculation_type=calculation_type)
        crt.save()
    return render(request,'pay_head.html',{'att':att})

def load(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})



def load_calculation(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

def bank(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        accno=request.POST['accno']
        ifsc_Code=request.POST['ifsc_Code']
        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        crt=bank_crt(accno=accno,ifsc_Code=ifsc_Code,bank_name=bank_name,branch=branch)
        crt.save
        return redirect('employee_creation')
    return render(request,'bank_details.html',{'emp':emp})


def payroll(request):
    if request.method=='POST':
        name=request.POST['name']
        allias=request.POST['allias']
        voucher_type=request.POST['voucher_type']
        abbreviation=request.POST['abbreviation']
        activate_voucher=request.POST['activate_voucher']
        voucher_numbering_method=request.POST['voucher_numbering_method']
        effective_dates=request.POST['effective_dates']
        narration_voucher=request.POST['narration_voucher']
        print_voucher=request.POST['print_voucher']
        classs=request.POST['classs']
        crt=payroll_crt(name=name,allias=allias,voucher_type=voucher_type,abbreviation=abbreviation,activate_voucher=activate_voucher,
                        voucher_numbering_method=voucher_numbering_method,effective_dates=effective_dates,
                        narration_voucher=narration_voucher,
                        print_voucher=print_voucher,classs=classs)
        crt.save()
        
        
    return render(request,'payroll_voucher_type.html')

def attendance(request):
    att=attendance_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units)
        crt.save()
    return render(request,'attendance.html',{'att':att})


def attendance_seconday(request):
    att=attendance_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units)
        crt.save()
    return render(request,'attendance(secondary).html',{'att':att})

def salary_details(request):
    pay=payhead_crt.objects.all()
    sal=salary_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        date=request.POST['date']
        pay_head_name=request.POST['pay_head_name']
        rate=request.POST['rate']
        pay_head_type=request.POST['pay_head_type']
        calculation_type=request.POST['calculation_type']
        crt=salary_crt(name=name,alias=alias,date=date,pay_head_name=pay_head_name,pay_head_type=pay_head_type,rate=rate,calculation_type=calculation_type)
        crt.save()
    return render(request,'salary_details.html',{'pay':pay,'sal':sal})

def stock_item_allocations(request):
    gd=CreateGodown.objects.all()
    if request.method=="POST":
        allocate=request.POST['allocate']
        for_allocate=request.POST['for_allocate']
        godown=request.POST['godown']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        amount=request.POST['amount']
        crt=allocate_stock(allocate=allocate,for_allocate=for_allocate,godown=godown,
                           quantity=quantity,rate=rate,per=per,amount=amount)
        crt.save()
        return redirect("stock_items")
    return render(request,'allocation_stock_item.html',{'gd':gd})
    

