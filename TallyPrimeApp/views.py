from django.shortcuts import render,redirect

from TallyPrimeApp.models import CreateEmployeeGrp, CreateGodown, CreateStockCateg, CreateStockGrp, UnitCrt, Price_level, cost, pancin


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
    return render(request,'stock_category(secondary).html',{'und':und})

    



def stock_items(request):
    return render(request,'stock_items.html')


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
    return render(request,'unit.html',{'unit':unit})


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
    return render(request,'employee_creation.html')

def price_levels(request):
    price=Price_level.objects.all()
    if request.method=="POST":
        number=request.POST['number']
        crt=Price_level(number=number)
        crt.save()
        return redirect('price_levels')
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
    return render(request,'pay_head.html')

def stock(request):
    return render(request,'stock.html')


def payroll(request):
    return render(request,'cost.html')

def attendance(request):
    return render(request,'attendance.html')

def attendance_seconday(request):
    return render(request,'attendance(secondary)).html')