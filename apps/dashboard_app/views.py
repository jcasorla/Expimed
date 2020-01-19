from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages

from time import gmtime, strftime
from datetime import datetime
import random
from . models import *



def bad_request(request):
    if('id' in request.session):
        return redirect('/dash/show')
    
    else:
        return redirect('/')

# def calendar(request):

#     # return render(request, "login_app/show.html")
#     return render(request, "dashboard_app/calendar.html")


########################### Patient ###########################################
def show(request):
    if('id' in request.session):
        context={
        "all_pats": Patient.objects.all()
        }
        return render(request, "dashboard_app/patient_grid.html",context)
    
    else:
        return redirect('/')



def new_patient(request):
    if('id' in request.session):
      
        return render(request, "dashboard_app/new_patient.html")
    
    else:
        return redirect('/')

    


def insert_patient(request):

    if('id' in request.session):
        if request.method=="POST":
    
            errors=Patient.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                    return redirect('/dash/new_patient')
            
            else:
                
                Patient.objects.create(
                    first_name=request.POST['first_name'],\
                    last_name=request.POST['last_name'],\
                    email=request.POST['email'], \
                    address=request.POST['address'],\
                    middle_name=request.POST['middle_name'],\
                    city=request.POST['city'],\
                    state=request.POST['state'],\
                    zip_code=request.POST['zip_code'],\
                    phone1=request.POST['p_number'],\
                    creator_id=request.session['id'],
                )
                return redirect('/dash/show')
    
    else:
        return redirect('/')
        
    
def patient_view(request,my_val):
    if('id' in request.session):
          # this_pat=Patient.objects.get(id=my_val)
        # my_meds=this_pat.presc_meds.all().filter(id=my_val).values()
        my_meds=Med.objects.all().filter(presc__id__contains=my_val).values()
        # not_mine=this_pat.presc_meds.all().exclude(id=my_val).values()
        not_mine=Med.objects.all().exclude(presc__id__contains=my_val).values()

        # presc_meds = Med.objects.all().filter(presc_meds__contains=my_val)      
        # not_meds = Med.objects.all().exclude(presc_meds__id__contains=my_val)
        # my_meds=Med.objects.first().presc_med.all()

        context={
            "pat": Patient.objects.get(id=my_val),
            "all_meds": not_mine,
            "my_meds": my_meds
            
        }
    
        return render(request, "dashboard_app/view_patient2.html",context)
    else:
        return redirect('/')

   

def patient_edit(request,my_val):
    if('id' in request.session):
        context={
        "pat": Patient.objects.get(id=my_val)
        }
        
        return render(request, "dashboard_app/edit_patient.html",context)
        
    else:
        return redirect('/')
    

def patient_update(request,my_val):
    if('id' in request.session):
      
        if request.method=="POST":
    
            errors=Patient.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                return redirect(f"/dash/patient/{my_val}/edit")

            else:
                p1=Patient.objects.get(id=my_val)
                p1.first_name=request.POST["first_name"]
                p1.last_name=request.POST["last_name"]
                p1.email=request.POST["email"]
                p1.address=request.POST["address"]
                p1.city=request.POST["city"]
                p1.state=request.POST["state"]
                p1.zip_code=request.POST["zip_code"]
                p1.phone1=request.POST["p_number"]
                p1.save()
                
                return redirect(f"/dash/patient/{my_val}")
    
    else:
        return redirect('/')
    
    


def patient_del(request,my_val):

    if('id' in request.session):
      
        p1=Patient.objects.get(id=my_val)
        p1.delete()

        return redirect('/dash/show')
    
    else:
        return redirect('/')
    

def presc_med(request,user_id,med_id):
    if('id' in request.session):
      
        this_med = Med.objects.get(id=med_id)
        this_pat = Patient.objects.get(id = user_id)
        this_med.presc.add(this_pat)
        #print("this book's likes",this_book.likes.all().values())
        # whopresc = this_med.presc.filter(id = user_id)
        # print(whopresc.values())
        # print("who liked it?",whopresc.values()[0]['id'])

        return redirect(f"/dash/patient/{user_id}")

    
    else:
        return redirect('/')
    

def unpresc_med(request,user_id,med_id):
    if('id' in request.session):
      
        this_med = Med.objects.get(id=med_id)
        this_pat = Patient.objects.get(id = user_id)
        this_med.presc.remove(this_pat)

        return redirect(f"/dash/patient/{user_id}")
    
    else:
        return redirect('/')
    
    

def unpresc_med2(request,user_id,med_id):
    if('id' in request.session):
      
        this_med = Med.objects.get(id=med_id)
        this_pat = Patient.objects.get(id = user_id)
        this_med.presc.remove(this_pat)
        return redirect(f"/dash/med/{med_id}")
        
    else:
        return redirect('/')
    
   

########################### Medication ###########################################
def meds_grid(request):
    if('id' in request.session):
      
        context={
        "all_meds": Med.objects.all()

        }        

        return render(request, "dashboard_app/medication_grid.html", context)
    
    else:
        return redirect('/')

    

def new_med(request):
    if('id' in request.session):
        context={
            "all_cats": Category.objects.all()
        }        
      
        return render(request, "dashboard_app/new_medication.html", context)
    
    else:
        return redirect('/')

def insert_med(request):
    if('id' in request.session):
      
        if request.method=="POST":
    
            errors=Med.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                    return redirect('/dash/new_med')
            
            else:
                print(request.POST['category'])
                this_cat = Category.objects.get(id = request.POST['category'])
                print(this_cat.name)
                Med.objects.create(
                    name=request.POST['name'],\
                    category2=this_cat, \
                    description=request.POST['description'],\
                    creator_id=request.session['id'],
                )
                # this_med = Med.objects.get(id=med_id)
                # this_pat = Patient.objects.get(id = user_id)
                # this_med.presc.add(this_pat)
                return redirect('/dash/meds_grid')
    
    else:
        return redirect('/')

    

def med_view(request,my_val):
    if('id' in request.session):
      
        my_pats=Med.objects.first().presc.all()

        context={
            "med": Med.objects.get(id=my_val),
            "my_pats": my_pats
        }
        
        return render(request, "dashboard_app/view_med.html",context)
    
    else:
        return redirect('/')    

def med_edit(request,my_val):
    if('id' in request.session):
          
        context={
            "med": Med.objects.get(id=my_val),
            "all_cats": Category.objects.all()
        }
        
        return render(request, "dashboard_app/edit_med.html",context)
    
    else:
        return redirect('/')

   

def med_update(request,my_val):
    if('id' in request.session):
      
        if request.method=="POST":
    
            errors=Med.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                return redirect(f"/dash/med/{my_val}/edit")

            else:
                m1=Med.objects.get(id=my_val)
                m1.name=request.POST["name"]
                m1.description=request.POST["description"]
                m1.category=request.POST["category"]
                m1.save()
                
                return redirect(f"/dash/med/{my_val}")
    
    else:
        return redirect('/')

    

def med_del(request,my_val):
    if('id' in request.session):
      
        m1=Med.objects.get(id=my_val)
        m1.delete()

        return redirect('/dash/meds_grid')
        
    else:
        return redirect('/')

    
########################### Patient ###########################################
def cat_grid(request):
    if('id' in request.session):
      
        context={
        "all_cats": Category.objects.all()

        }        

        return render(request, "dashboard_app/category_grid.html", context)
    
    else:
        return redirect('/')

    

def new_cat(request):
    if('id' in request.session):
      
        return render(request, "dashboard_app/new_category.html")
    
    else:
        return redirect('/')

def insert_cat(request):
    if('id' in request.session):
      
        if request.method=="POST":
    
            errors=Category.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                    return redirect('/dash/new_cat')
            
            else:
                
                Category.objects.create(
                    name=request.POST['name'],\
                    description=request.POST['description'],\
                    creator_id=request.session['id'],
                )
                return redirect('/dash/cat_grid')
    
    else:
        return redirect('/')

    

def cat_view(request,my_val):
    if('id' in request.session):
      
        my_meds=Category.objects.first().meds.all()

        context={
            "cat": Category.objects.get(id=my_val),
            "my_meds": my_meds
        }
        
        return render(request, "dashboard_app/view_cat.html",context)
    
    else:
        return redirect('/')    

def cat_edit(request,my_val):
    if('id' in request.session):
      
        context={
        "cat": Category.objects.get(id=my_val)
        }
        
        return render(request, "dashboard_app/edit_category.html",context)
    
    else:
        return redirect('/')

   

def cat_update(request,my_val):
    if('id' in request.session):
      
        if request.method=="POST":
    
            errors=Category.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    print(key, value + '\n')
                    messages.add_message(request, messages.INFO,  value)
                return redirect(f"/dash/cat/{my_val}/edit")

            else:
                c1=Category.objects.get(id=my_val)
                c1.name=request.POST["name"]
                c1.description=request.POST["description"]
                c1.save()
                
                return redirect(f"/dash/cat/{my_val}")
    
    else:
        return redirect('/')

    

def cat_del(request,my_val):
    if('id' in request.session):
      
        c1=Category.objects.get(id=my_val)
        c1.delete()

        return redirect('/dash/cat_grid')
        
    else:
        return redirect('/')





 