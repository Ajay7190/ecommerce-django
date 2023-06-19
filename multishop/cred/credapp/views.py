from django.shortcuts import render,redirect
from credapp.models import categoryDB,poductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webApp.models import contactDB
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req,'index.html')
def categorypage(req):
    return render(req,'addcategory.html')
def categorydata(req):
    if req.method == "POST":
        cname=req.POST.get('c-name')
        cimg=req.FILES['c-image']
        cdes=req.POST.get('c-description')
        obj = categoryDB(category_name=cname,category_image=cimg, category_description=cdes)
        obj.save()
        messages.success(req,"Category Saved Successfuly....")
        return redirect(categorypage)



def displaycategory(req):
    data = categoryDB.objects.all()
    return render(req,"displaycategorytable.html", {'data':data})

def updatecategorydata(req,dataid):
    data = categoryDB.objects.get(id=dataid)
    return render(req, "updatecategorydata.html", {'data':data})

def editcategorydata(req,dataid):
    if req.method == "POST":
        cname=req.POST.get('c-name')
        cdes=req.POST.get('c-description')
        try:
            img=req.FILES['c-image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categoryDB.objects.get(id = dataid).category_image
        categoryDB.objects.filter(id=dataid).update(category_name=cname,category_image=file, category_description=cdes)
        messages.success(req,"Category Edited Successfuly....")
        return redirect(displaycategory)
    
def deleteCategoryData(req,dataid):
    data = categoryDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Category Deleted Successfuly....")
    return redirect(displaycategory)


def poductpage(req):
    data = categoryDB.objects.all()
    return render(req,'addProduct.html',{'data':data})

def getproductdata(req):
    if req.method == "POST":
        pcategory=req.POST.get('Product-category')
        pname=req.POST.get('Product-name')
        price=req.POST.get('Product-price')
        pdes=req.POST.get('Product-description')
        pbrand=req.POST.get('Product-brand')
        pimg=req.FILES['Product-image']       
        obj = poductDB(product_category=pcategory,product_name=pname,product_price=price,product_description=pdes,product_brand=pbrand,product_image=pimg)
        obj.save()
        messages.success(req,"Product Saved Successfuly....")
        return redirect(poductpage)
    
def displayproduct(req):
    data = poductDB.objects.all()
    return render(req,"displayProduct.html", {'data':data})

def updateproductdata(req,dataid):
    cate=categoryDB.objects.all()
    data = poductDB.objects.get(id=dataid)
    return render(req, "updateproduct.html", {'cate':cate,'data':data})

def editproductdata(req,dataid):
    if req.method == "POST":
        pcategory=req.POST.get('Product-category')
        pname=req.POST.get('Product-name')
        price=req.POST.get('Product-price')
        pdes=req.POST.get('Product-description')
        pbrand=req.POST.get('Product-brand')
        try:
            pimg=req.FILES['Product-image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name,pimg)
        except MultiValueDictKeyError:
            file = poductDB.objects.get(id = dataid).product_image
        poductDB.objects.filter(id=dataid).update(product_category=pcategory,product_name=pname,product_price=price,product_description=pdes,product_brand=pbrand,product_image=file)
        messages.success(req,"Product Edited Successfuly....")
        return redirect(displayproduct)
    

    
def deleteproductData(req,dataid):
    data = poductDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Product Deleted Successfuly....")
    return redirect(displayproduct)

def loginpage(req):
    return render(req,"loginpage.html")

def admin_login(req):
    if req.method=="POST":
        uname=req.POST.get('username')
        pwd=req.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(req,user)
                req.session['username'] = uname
                req.session['password'] = pwd
                messages.success(req,"Login Successfuly....")
                return redirect(indexpage)
            
            else:
                messages.error(req,"Invalid User Name or Password")
                return redirect(loginpage)
        else:
            return redirect(loginpage)
        
def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage) 

def displayConatct(req):
    data = contactDB.objects.all()
    return render(req,"displayContactdetals.html", {'data':data})

def deletecontactdata(req,dataid):
    data = contactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayConatct)








