from email.policy import default
from django.db import models

# Create your models here.
class regist(models.Model):
   name=models.CharField(max_length=15,null=True)
   Pswd=models.CharField(max_length=20,null=True)

class category(models.Model):
   productcategory=models.CharField(max_length=25,null=True)
class FinancialYear(models.Model):
    financial_year = models.CharField(max_length=9, null=True)  # Format: YYYY-YYYY
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
class Basicinformation(models.Model):
   name=models.CharField(max_length=15,null=True)
   Address=models.CharField(max_length=20,null=True)
  
   Website=models.CharField(max_length=50,null=True)
   phone1=models.CharField(max_length=50,null=True)
   phone2=models.CharField(max_length=50,null=True)
   e_mail1=models.EmailField(max_length=50,null=True)
   e_mail2=models.EmailField(max_length=50,null=True)
   Logo=models.ImageField(upload_to="media",null=True)
   Gstino=models.CharField(max_length=50,null=True)
class windowblinds(models.Model):
   category=models.CharField(max_length=50,null=True)
   productcode=models.CharField(max_length=15,null=True)
   productname=models.CharField(max_length=20,null=True)
   taxpercent=models.CharField(max_length=50,null=True)
   hsncode=models.CharField(max_length=50,null=True)
   unit=models.CharField(max_length=50,null=True)
   unitprice=models.CharField(max_length=50,null=True)
class Product(models.Model):
   Category=models.CharField(max_length=15,null=True)
   Productcode=models.CharField(max_length=20,null=True)
   Productname=models.ImageField(max_length=50,null=True)
   Tax=models.CharField(max_length=50,null=True)
   Hsncode=models.CharField(max_length=50,null=True)
   Unit=models.CharField(max_length=50,null=True)
   Unitprice=models.CharField(max_length=50,null=True)
class Employeeform(models.Model):
   joiningdate=models.DateField(null=True)
   employeeid=models.CharField(max_length=20,null=True)
   firstname=models.CharField(max_length=50,null=True)
   lastname=models.CharField(max_length=50,null=True)
   dateofbirth=models.CharField(max_length=50,null=True)
   e_mail1=models.EmailField(max_length=50,null=True)
   phone1=models.CharField(max_length=20,null=True)
   phone2=models.CharField(max_length=20,null=True)
   address=models.CharField(max_length=60,null=True)
   designation=models.CharField(max_length=20,null=True)
   idcardtype=models.CharField(max_length=20,null=True)
   idcardnumber=models.CharField(max_length=20,null=True)
   photo=models.ImageField(upload_to='media',null=True)
   doc1=models.ImageField(upload_to='media',null=True)
   doc2=models.ImageField(upload_to='media',null=True)
class staff(models.Model):
    name = models.CharField(max_length=100, null= False)

class Lead(models.Model):
   inquiry_id = models.CharField(max_length=20, null=True, blank=True)
   inquiry_date = models.DateField(null=True, blank=True)  # Use DateField for dates
   cust_name = models.CharField(max_length=100, null=True, blank=True)  # Increased max_length
   mobile = models.CharField(max_length=20, null=True, blank=True)
   alternate_no = models.CharField(max_length=20, null=True, blank=True)
   email = models.EmailField(max_length=50, null=True, blank=True)
   address = models.CharField(max_length=255, null=True, blank=True)  # Increased max_length
   remark = models.CharField(max_length=255, null=True, blank=True)
   source = models.CharField(max_length=50, null=True)
   status = models.CharField(
        max_length=20,
        choices=[
            ('lead_approved', 'Lead Approved'),
            ('order_taken', 'Order Taken'),
        ],
        default='lead_approved'
    )
   assigned_staff = models.ForeignKey(staff,on_delete=models.CASCADE,default=1)
class windowblindtable(models.Model):
   
   sqft=models.CharField(max_length=20,null=True)
   ratepermeter=models.CharField(max_length=20,null=True)
   unit=models.CharField(max_length=20,null=True)
   name=models.ForeignKey(Lead,on_delete=models.CASCADE,default=1)
   productname=models.ForeignKey(windowblinds,on_delete=models.CASCADE,null=True)
   qty=models.CharField(max_length=20,null=True)
   totalsqft=models.CharField(max_length=20,null=True)
   price=models.CharField(max_length=20,null=True)
class windowblindtable1(models.Model):
   quatationnumber=models.CharField(max_length=20,null=True)
   dateofreceipt=models.CharField(max_length=20,null=True)
   
   totalamount=models.CharField(max_length=20,null=True)
   pastingcharge=models.CharField(max_length=20,null=True)
   #totalqty=models.CharField(max_length=20,null=True)
   gsttotal=models.CharField(max_length=20,null=True)
   discount=models.CharField(max_length=20,null=True)
   others=models.CharField(max_length=20,null=True)
   netamount=models.CharField(max_length=20,null=True)


class Curtain(models.Model):
   Category=models.CharField(max_length=15,null=True)
   Productcode=models.CharField(max_length=20,null=True)
   Productname=models.ImageField(max_length=50,null=True)
   Tax=models.CharField(max_length=50,null=True)
   Hsncode=models.CharField(max_length=50,null=True)
   Unit=models.CharField(max_length=50,null=True)
   Unitprice=models.CharField(max_length=50,null=True)

class Sofa(models.Model):
   Category=models.CharField(max_length=15,null=True)
   Productcode=models.CharField(max_length=20,null=True)
   Productname=models.ImageField(max_length=50,null=True)
   Tax=models.CharField(max_length=50,null=True)
   Hsncode=models.CharField(max_length=50,null=True)
   Unit=models.CharField(max_length=50,null=True)
   Unitprice=models.CharField(max_length=50,null=True)


class Mosquito(models.Model):
   Category=models.CharField(max_length=15,null=True)
   Productcode=models.CharField(max_length=20,null=True)
   Productname=models.ImageField(max_length=50,null=True)
   Tax=models.CharField(max_length=50,null=True)
   Hsncode=models.CharField(max_length=50,null=True)
   Unit=models.CharField(max_length=50,null=True)
   Unitprice=models.CharField(max_length=50,null=True)



