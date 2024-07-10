
from datetime import timezone
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def Login(request):
    return render(request,'login.html')


def changepassword(request):

    return render(request,'changepassword.html')

def  checklogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            return redirect("/")

    
def reset_password(request):
    username = request.POST.get("username")
    new_password = request.POST.get("password")
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return redirect("/dashboard")

def design(request):
    return render(request,'design.html')

def product_category(request):
    categories = category.objects.all()
    context = {
        'prod' : categories
    }
    return render(request,'product_category.html',context)





def financialyear(request):
    financial_years = FinancialYear.objects.all()  # Fetch all financial years
    context = {
        'financial_years': financial_years
    }
    return render(request, 'financialyear.html', context)

def financialyearadd(request):
    return render (request,"financialyearadd.html")

def financialyearedit(request):
    id = request.POST.get("id")
    financial_year = get_object_or_404(FinancialYear, pk=id)  # Retrieve the financial year object
    context = {
        'financial_year': financial_year
    }
    return render(request, "financialyearedit.html", context)

def financialyearadd_tbl(request):
    obj=FinancialYear()
    obj.financial_year=request.POST.get("financialYear")
    obj.start_date = request.POST.get("startDate")
    obj.end_date= request.POST.get("endDate")
    obj.save()
    return redirect('/financialyear/')



def financialyear_delete(request, id):
    financial_year = get_object_or_404(FinancialYear, id=id)
    financial_year.delete()
    messages.success(request, 'Financial year deleted successfully.')
    return redirect('financialyear_list')  # Make sure 'financialyear_list' is the name of your list view URL pattern

def savefinancialyear(request):
    if request.method == 'POST':
        # Extracting data from the POST request

        id = request.POST.get('id')
        financial_year = request.POST.get('financial_year')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(id)
        print(financial_year)

        # Getting the FinancialYear instance or returning a 404 error if not found
        financial_year_instance = get_object_or_404(FinancialYear, id=id)

        # Updating the instance with new data
        financial_year_instance.financial_year = financial_year
        financial_year_instance.start_date = start_date
        financial_year_instance.end_date = end_date

        # Saving the updated instance to the database
        financial_year_instance.save()

        # Redirecting to a success page or another relevant page
        return redirect('/financialyear/')  # Change this to the appropriate URL



def delete_row(request, id):
        try:
            obj = get_object_or_404(FinancialYear, pk=id)
            obj.delete()
            return redirect('/financialyear/')
        except Exception as e:
            return redirect('/financialyear/')
        
def basicinformation(request):
    obj = Basicinformation.objects.all()
    context = {
        'direct' : obj
    }
    return render(request,'basicinformation.html',context)






def dir_add(request):
    direct=Basicinformation()
    direct.name = request.POST.get('name')
    direct.Address = request.POST.get('address')    
    Logo= request.FILES['Logo']
    fs=FileSystemStorage()
    file=fs.save(Logo.name,Logo)
    url=fs.url(file)
    direct.logo=url
    
    direct.Website = request.POST.get('website')
   
    direct.e_mail1 = request.POST.get('e_mail1')
    direct.e_mail2 = request.POST.get('e_mail2')
    direct.phone1 = request.POST.get('phonenumber1')
    direct.phone2 = request.POST.get('phonenumber2')
   
    direct.Gstino = request.POST.get('Gstino')
    
    direct.save()
    return redirect('/basicinformation/')


def addinformation(request):
    return render (request,'addinfo.html')
    

def dir_del(request, id):
    try:
        obj = get_object_or_404(Basicinformation, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/basicinformation/')


def dir_edit(request,id):
    obj = get_object_or_404(Basicinformation, pk=id)
    context = {
        'company' : obj
    }
    return render(request,'edit.html',context)


def save_dir_add(request):
    id = request.POST.get("id")
    direct=get_object_or_404(Basicinformation, pk=id)
    direct.name = request.POST.get('name')
    direct.Address = request.POST.get('address')
  
    direct.Website = request.POST.get('website')
   
    direct.e_mail1 = request.POST.get('e_mail1')
    direct.e_mail2 = request.POST.get('e_mail2')
    direct.phone1 = request.POST.get('phonenumber1')
    direct.phone2 = request.POST.get('phonenumber2')
    direct.Gstino = request.POST.get('Gstino')
    try:
        Logo = request.FILES['Logo']
        fs=FileSystemStorage()
        file=fs.save(Logo.name,Logo)
        url=fs.url(file)
        direct.Logo=url
        direct.save()
    except:
        direct.save()
    return redirect('/basicinformation/')
    


def windowblind(request):
    obj = windowblinds.objects.all()
    context = {
        'di' : obj
    }
    return render(request,'windowblind.html',context)


def windowaddinfo(request):
    di=windowblinds()
    di.category = request.POST.get('category')
    di.productcode = request.POST.get('code')
    di.productname = request.POST.get('p_name')
    di.taxpercent = request.POST.get('tax%')
    di.hsncode = request.POST.get('hsncode')
    di.unit = request.POST.get('unit')
    di.unitprice = request.POST.get('unitprice')
    di.save()
    return redirect('/windowblind/')

def windowadd(request):
    return render (request,'windowadd.html')

def windowblindedit(request,id):
    obj = get_object_or_404(windowblinds, pk=id)
    context = {
        'comp' : obj
    }
    return render(request,'windowblindedit.html',context)

def windowblinddelete(request, id):
    try:
        obj = get_object_or_404(windowblinds, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/windowblind/')

def windowsaveinfo(request):
    id = request.POST.get("id")
    di=get_object_or_404(windowblinds, pk=id)
    di.category = request.POST.get('category')
    di.productcode = request.POST.get('code')
    di.productname = request.POST.get('p_name')
    di.taxpercent = request.POST.get('tax%')
    di.hsncode = request.POST.get('hsncode')
    di.unit = request.POST.get('unit')
    di.unitprice = request.POST.get('unitprice')
    di.save()
    return redirect('/windowblind/')


def Products(request):
    obj = Product.objects.all()
    context = {
        'direct' : obj
    }
    return render(request,'Product.html',context)


def addnewproduct(request):
    return render(request,'addnewproduct.html')


def add_prod_tbl(request):
    direct=Product()
    direct.Category = request.POST.get('Category')
    direct.Productcode = request.POST.get('Productcode')
     
  
    direct.Productname = request.POST.get('Productname')
   
    direct.Tax = request.POST.get('Tax')
    direct.Hsncode = request.POST.get('Hsncode')
    direct.Unit = request.POST.get('Unit')
    direct.Unitprice = request.POST.get('Unitprice')
   
    
    
    direct.save()
    return redirect('/Product/')



def dir_del_prod(request, id):
    try:
        obj = get_object_or_404(Product, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/Product/')


def edit_prod_tbl(request,id):
    obj = get_object_or_404(Product, pk=id)
    context = {
        'direct' : obj
    }
    return render(request,'editproduct.html',context)


def save_edit_prod(request):
    id = request.POST.get("id")
    direct=get_object_or_404(Product, pk=id)
    direct.Category=request.POST.get('Category')
    direct.Productcode=request.POST.get('Productcode')
    direct.Productname=request.POST.get('Productname')
    direct.Tax=request.POST.get('Tax')
    direct.Hsncode=request.POST.get('Hsncode')
    direct.Unit=request.POST.get('Unit')
    direct.Unitprice=request.POST.get('Unitprice')
  
    direct.save()
    return redirect('/Product/')
def employeeform(request):
    
    return render(request,'employeeform.html')

def saveemployeeform(request):
   
    if request.method == 'POST':
        # Create a new instance of the Employee model
        employee = Employeeform()
        
        # Assign values to the model fields from the POST data
        employee.joiningdate = request.POST.get('joining-date')
        employee.employeeid = request.POST.get('employee-id')
        employee.firstname = request.POST.get('first-name')
        employee.lastname = request.POST.get('last-name')
        employee.dateofbirth = request.POST.get('dob')
        employee.e_mail1 = request.POST.get('email')
        employee.phone1 = request.POST.get('phone1')
        employee.phone2 = request.POST.get('phone2')
        employee.address = request.POST.get('address')
        employee.designation = request.POST.get('designation')
        employee.idcardtype = request.POST.get('idcard-type')
        employee.idcardnumber = request.POST.get('idcard-number')
        #employee.photo=request.FILES['upload-photo']
    
        photo = request.FILES['upload-photo']
        fs=FileSystemStorage()
        file=fs.save(photo.name,photo)
        url=fs.url(file)
        employee.photo=url
        doc1 = request.FILES['upload-id-proof']
        fs=FileSystemStorage()
        file=fs.save(doc1.name,doc1)
        url=fs.url(file)
        employee.doc1=url
        doc2 = request.FILES['upload-other-document']
        fs=FileSystemStorage()
        file=fs.save(doc2.name,doc1)
        url=fs.url(file)
        employee.doc2=url
        
        
    
        employee.save()
    return redirect('/dashboard/')
        
        
     





def displayemployee(request):
    obj = Employeeform.objects.all()
    context = {
        'gd' : obj
    }
    return render(request,'displayemployee.html',context)



def tablepage(request):
    obj = windowblinds.objects.all()
    obj1 = Lead.objects.all()
    
    try:
        # Get the record with the largest bill_no
        largest_billno_record = windowblindtable1.objects.order_by('-quatationnumber').first()
        if largest_billno_record is not None:
            largest_billno = largest_billno_record.quatationnumber
            # Increment the numeric part of the bill_no
            prefix = largest_billno[:-4]
            numeric_part = largest_billno[-4:]
            next_numeric_part = str(int(numeric_part) + 1).zfill(4)
            next_bill_no = prefix + next_numeric_part
            print(next_bill_no)
        else:
            next_bill_no = "KPAC0001"
    except Exception as e:
        print(f"Unexpected error: {e}")
        next_bill_no = "KPAC0001"

    context = {
        'le': obj1,
        'win': obj,
        'bill_no': next_bill_no
    }
    return render(request, 'table.html', context)



def ajax_view_for_products(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        obj = get_object_or_404(windowblinds, pk=selected_option)
        
        pc=obj. productcode
        
        
       
        

        response_data = {
            'message': f'Selected option is {selected_option}',
           
            'pc' : pc,
            
            


            
        }

        print(response_data)
        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'},status=400)



# lead
def lead(request):
    obj = Lead.objects.all()
    context = {
        'leads' : obj
    }
    return render(request,'lead.html',context)



def leadadd(request):
    staffs = staff.objects.all()
    context = {
        'staff' : staffs
    }
    return render(request,'leadadd.html',context)



def leadedit(request,id):
    obj = get_object_or_404(Lead, pk=id)
    staffs = staff.objects.all()
    context = {
        'lead' : obj,
        'staff' : staffs
    }
    return render(request,'leadedit.html',context)



def savelead(request):
    if request.method == 'POST':
        inquiry_id = request.POST.get('inquiryId')
        inquiry_date = request.POST.get('inquiryDate')
        customer_name = request.POST.get('customerName')
        mobile_no = request.POST.get('mobileNo')
        alternate_no = request.POST.get('alternateNo')
        email_id = request.POST.get('emailId')
        address = request.POST.get('address')
        lead_source = request.POST.get('leadSource')
        inquiry_staff_id = request.POST.get('inquiryStaff')
        customer_remark = request.POST.get('customerRemark')

        assigned_staff = get_object_or_404(staff, pk=inquiry_staff_id)

        Lead.objects.create(
            inquiry_id=inquiry_id,
            inquiry_date=inquiry_date,
            cust_name=customer_name,
            mobile=mobile_no,
            alternate_no=alternate_no,
            email=email_id,
            address=address,
            source=lead_source,
            assigned_staff=assigned_staff,
            remark=customer_remark
        )

        return redirect('/lead/')

    return render(request, 'lead.html', {'staff': staff.objects.all()})



def save_edited_lead(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        inquiry_id = request.POST.get('inquiryId')
        inquiry_date = request.POST.get('inquiryDate')
        customer_name = request.POST.get('customerName')
        mobile_no = request.POST.get('mobileNo')
        alternate_no = request.POST.get('alternateNo')
        email_id = request.POST.get('emailId')
        address = request.POST.get('address')
        lead_source = request.POST.get('leadSource')
        inquiry_staff_id = request.POST.get('inquiryStaff')
        customer_remark = request.POST.get('customerRemark')

        try:
            assigned_staff = get_object_or_404(staff, pk=inquiry_staff_id)
        except staff.DoesNotExist:
            return render(request, 'error_page.html', {'error_message': 'Assigned staff does not exist.'})

        try:
            lead_obj = get_object_or_404(Lead, pk=id)
        except Lead.DoesNotExist:
            return render(request, 'error_page.html', {'error_message': 'Lead does not exist.'})

        # Update lead object with new data
        lead_obj.inquiry_id = inquiry_id
        lead_obj.inquiry_date = inquiry_date
        lead_obj.cust_name = customer_name
        lead_obj.mobile = mobile_no
        lead_obj.alternate_no = alternate_no
        lead_obj.email = email_id
        lead_obj.address = address
        lead_obj.source = lead_source
        lead_obj.assigned_staff = assigned_staff
        lead_obj.remark = customer_remark
        lead_obj.save()

        return redirect('/lead/')

    else:
        id = request.GET.get("id")
        if id is None:
            return render(request, 'error_page.html', {'error_message': 'Lead ID parameter is missing.'})

        try:
            lead = get_object_or_404(Lead, pk=id)
        except Lead.DoesNotExist:
            return render(request, 'error_page.html', {'error_message': 'Lead does not exist.'})

        context = {
            'lead': lead,
            'staff': staff.objects.all()
        }
        return render(request, 'lead_edit.html', context)
    


def delete_lead(request, id):
    try:
        lead = get_object_or_404(Lead, pk=id)
        lead.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/lead/')


# staff
def  addstaff(request):
    names=['vishnu', 'raju', 'Rajeev']
    for n in names:
        obj = staff.objects.create(name=n)
        obj.save()
    return redirect('/lead/')
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        obj = get_object_or_404(Lead, pk=selected_option)
        add = obj.address
        

        response_data = {
            'message': f'Selected option is {selected_option}',
            'address': add
           
        }

        print(response_data)
        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'},status=400)


def salesform_save(request):
     if request.method == 'POST':
         
        obj2=windowblindtable1()
        obj2.quatationnumber=request.POST.get("bill_number")
        obj2.dateofreceipt=request.POST.get("reciept_date")
        obj2.totalamount=request.POST.get("total_amount")
        obj2.pastingcharge=request.POST.get("pasting_charge")
        obj2.totalqty=request.POST.get("total_qty")
        obj2.gsttotal=request.POST.get("gst_total")
        obj2.discount=request.POST.get("discount")
        obj2.others=request.POST.get("others")
        obj2.netamount=request.POST.get("net_amount")
        obj2.dateofreceipt=request.POST.get("reciept_date")
        obj2.save()

        serialnumber=request.POST.getlist("serial_number[]")
        product_name=request.POST.getlist("product_drop[]")

        sqft=request.POST.getlist("sqft[]")
        print(sqft)
        ratepermeter=request.POST.getlist("ratepermeter[]")
        print(ratepermeter)
        unit=request.POST.getlist("unit[]")
        qty=request.POST.getlist("QTY[]")
        totalsqft=request.POST.getlist("TOTALSQFT[]")
        price=request.POST.getlist("price[]")
        name=request.POST.get("cust_name")
        name=Lead.objects.get(id=name)
        

        for i in range(len(serialnumber)):
            try:
                # Retrieve the single windowblinds instance
                product_instance = windowblinds.objects.get(id=product_name[i])
            except windowblinds.DoesNotExist:
                # Handle the case where the product does not exist
                # Log the error or inform the user
                return HttpResponse(f"Product '{product_name[i]}' does not exist", status=404)

           # product_name = get_object_or_404(windowblinds, productname=productname[i])
           # print(product_name)
            # product_name = windowblinds.objects.filter(productname=productname[i])
            obj = windowblindtable()
            obj.productname = product_instance
            obj.sqft=sqft[i]
            obj.ratepermeter=ratepermeter[i]
            obj.unit=unit[i]
            obj.qty=qty[i]
            obj.totalsqft=totalsqft[i]
            obj.price=price[i]
            obj.name=name
            obj.save()
        return redirect('/table/')
     return HttpResponse("Invalid request method", status=405)

def quotationreport(request):
     obj = windowblindtable1.objects.all()
     obj2=windowblindtable.objects.all()
     combined_list=zip(obj,obj2)
     context = {
        'combined_list': combined_list,
    }
     return render(request,'quotation_report.html',context)


def curtain(request):
    obj = Curtain.objects.all()
    context = {
        'direct' : obj
    }
    return render(request,'curtain.html',context)

def addnewcurtain(request):
    return render(request,'addnewcurtain.html')


def add_curtain_tbl(request):
    direct=Curtain()
    direct.Category = request.POST.get('Category')
    direct.Productcode = request.POST.get('Productcode')
     
  
    direct.Productname = request.POST.get('Productname')
   
    direct.Tax = request.POST.get('Tax')
    direct.Hsncode = request.POST.get('Hsncode')
    direct.Unit = request.POST.get('Unit')
    direct.Unitprice = request.POST.get('Unitprice')
   
    
    
    direct.save()
    return redirect('/curtain/')



def dir_del_curtain(request, id):
    try:
        obj = get_object_or_404(Curtain, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/curtain/')


def edit_curtain_tbl(request,id):
    obj = get_object_or_404(Curtain, pk=id)
    context = {
        'direct' : obj
    }
    return render(request,'editcurtain.html',context)


def save_edit_curtain(request):
    id = request.POST.get("id")
    direct=get_object_or_404(Curtain, pk=id)
    direct.Category=request.POST.get('Category')
    direct.Productcode=request.POST.get('Productcode')
    direct.Productname=request.POST.get('Productname')
    direct.Tax=request.POST.get('Tax')
    direct.Hsncode=request.POST.get('Hsncode')
    direct.Unit=request.POST.get('Unit')
    direct.Unitprice=request.POST.get('Unitprice')
  
    direct.save()
    return redirect('/curtain/')

# sofa
def sofa(request):
    obj = Sofa.objects.all()
    context = {
        'direct' : obj
    }
    return render(request,'sofa.html',context)

def addnewsofa(request):
    return render(request,'addnewsofa.html')


def add_sofa_tbl(request):
    direct=Sofa()
    direct.Category = request.POST.get('Category')
    direct.Productcode = request.POST.get('Productcode')
     
  
    direct.Productname = request.POST.get('Productname')
   
    direct.Tax = request.POST.get('Tax')
    direct.Hsncode = request.POST.get('Hsncode')
    direct.Unit = request.POST.get('Unit')
    direct.Unitprice = request.POST.get('Unitprice')
   
    direct.save()
    return redirect('/sofa/')



def dir_del_sofa(request, id):
    try:
        obj = get_object_or_404(Sofa, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/sofa/')


def edit_sofa_tbl(request,id):
    obj = get_object_or_404(Sofa, pk=id)
    context = {
        'direct' : obj
    }
    return render(request,'editsofa.html',context)


def save_edit_sofa(request):
    id = request.POST.get("id")
    direct=get_object_or_404(Sofa, pk=id)
    direct.Category=request.POST.get('Category')
    direct.Productcode=request.POST.get('Productcode')
    direct.Productname=request.POST.get('Productname')
    direct.Tax=request.POST.get('Tax')
    direct.Hsncode=request.POST.get('Hsncode')
    direct.Unit=request.POST.get('Unit')
    direct.Unitprice=request.POST.get('Unitprice')
  
    direct.save()
    return redirect('/sofa/')

def leadreport(request):
    obj = Lead.objects.all()
    context = {
        'leads' : obj
    }
    return render(request,'leadreport.html',context)

def mosquito(request):
    obj = Mosquito.objects.all()
    context = {
        'direct' : obj
    }
    return render(request,'mosquito.html',context)






def addmosquito(request):
    return render(request,'addmosquito.html')


def add_mosq_tbl(request):
    direct=Mosquito()
    direct.Category = request.POST.get('Category')
    direct.Productcode = request.POST.get('Productcode')
     
  
    direct.Productname = request.POST.get('Productname')
   
    direct.Tax = request.POST.get('Tax')
    direct.Hsncode = request.POST.get('Hsncode')
    direct.Unit = request.POST.get('Unit')
    direct.Unitprice = request.POST.get('Unitprice')
   
    direct.save()
    return redirect('/mosquito/')



def dir_del_mosq(request, id):
    try:
        obj = get_object_or_404(Mosquito, pk=id)
        obj.delete()
        messages.success(request, "Information deleted successfully")
    except Exception as e:
        messages.error(request, "Error deleting information")
    return redirect('/mosquito/')


def edit_mosq_tbl(request,id):
    obj = get_object_or_404(Mosquito, pk=id)
    context = {
        'direct' : obj
    }
    return render(request,'editmosq.html',context)


def save_edit_mosq(request):
    id = request.POST.get("id")
    direct=get_object_or_404(Mosquito, pk=id)
    direct.Category=request.POST.get('Category')
    direct.Productcode=request.POST.get('Productcode')
    direct.Productname=request.POST.get('Productname')
    direct.Tax=request.POST.get('Tax')
    direct.Hsncode=request.POST.get('Hsncode')
    direct.Unit=request.POST.get('Unit')
    direct.Unitprice=request.POST.get('Unitprice')
  
    direct.save()
    return redirect('/mosquito/')


