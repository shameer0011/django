from django.shortcuts import render
from django.http import HttpResponse
from .models import Address,Event,Venue

# Create your views here.
def home(request):
    adresslist=Address.objects.all()
    print(adresslist)
    print("home") 
    a={"Name":"shameer","age":4,"addr":adresslist} 
    print(a)
    return render(request,"blog/home.html",a) 
def about(request):
    ad=Address.objects.filter(name="jisnu").first()
    adlist=Address.objects.filter(name="jisnu")
    q=Event.objects.all()
    print(ad)
    p={"data":ad,"fulldata":adlist,"event":q}
    
    return render(request,"blog/about.html",p) 

def addresstest(request):
    obj=Address(name="shameer",place="thrithallure",city="malappuram",state="kerala")
    obj.save()
    obj2=Address(name="smr",place="thrithallure",city="malappuram",state="kerala")
    obj2.save()
    obj3=Address(name="shami",place="chavakkad",city="thrissur",state="kerala")
    obj3.save()

    venue1=Venue(name="Northh stadiume",address="South st",zip_code="123456",phone="999955776")
    venue1.save()
    
    event1=Event(name="Test3 event",event_date="2018-12-5",venue=venue1)
    event1.save()
    event1.attendees.add(obj)
    event1.attendees.add(obj2)
    event1.attendees.add(obj3)
    
    print("inside save")

    return render(request,"blog/about.html")

