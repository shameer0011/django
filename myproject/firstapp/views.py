from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from blog.models import Address,Event,Venue


from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from django.core import serializers as ser

from django.contrib.auth import authenticate


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile



from django.forms.models import model_to_dict
from django.http import JsonResponse


from random import randint
from PIL import Image

from django.core.files.storage import FileSystemStorage





# Create your views here.
def firstpage(request):
    ad=Student.objects.filter(firstname="sibin").first()
    
    print(ad)
    p={"data":ad}
   
    #return HttpResponse("<h2>my first page</h2>")
    return render(request,'firstapp/home.html',p)

def secondpage(request):
        obj=Address(name="sibin",place="sibinks",city="sibin@gmail.com",state="thrisur",image="kearala") 
        obj.save()
        return HttpResponse("<h2>my first page</h2>")

def studentdetails(request):
    obj=Address(name="sibin",place="sibinks",city="sibin@gmail.com",state="thrisur",image="kearala") 
    obj.save()
    print("test") 
    #to show all details of sibin include firstname,lastname,email,city,state...
    p=Student.objects.filter(firstname="sibin")
    print(p)

    bd=Student.objects.filter(firstname="sibin").first()
    print(bd)
    pas={"details":p,"data2":bd} 

    return render(request,"firstapp/profile.html",pas)
    
@csrf_exempt
def test(request):

        print("call from angular")
        x=json.loads(request.body)
        print(x)
        x["name"]="shameer"
        x["notes"]="shameer super"
        
        return JsonResponse(x)
@csrf_exempt
def post1(request):
        print("call from angular")
        x=json.loads(request.body)
        print(x)
            
        return JsonResponse(x)
   
        
    #  return HttpResponse("<h2>my first page</h2>")
#post venue form
@csrf_exempt
def venueDetails(request):
    status={"status":"1","message":"Successfully saved"}
    try:
        print("From Testing")
        z=json.loads(request.body)
        print(z)
        venue1=Venue(name=z["name"],address=z["address"],zip_code=z["zip_code"],phone=z["phone"],email_address=z["email"])
        if Venue.objects.filter(name=z["name"]) or Venue.objects.filter(email_address=z["email"]):
            print("Already Exist,Use Another Name and Email")  
            status={"status":"0","message":"Already Exist,Use Another Name and Email"} 
        else:    
            venue1.save()
            print(venue1)
    except Exception as e:
        status={"status":"0","message":"Error Occured"}
    #  return JsonResponse(z)
    return JsonResponse(status)

def savefile(file,filename,foldr='media/image'):
    fs = FileSystemStorage()
    fnam=foldr+'/'+filename
    print(fname)
    print("haiiii")
    if fs.exists(fnam):
    	fs.delete(fnam)
    filename = fs.save(fnam, file)
    fileurl = fs.url(filename)
    return fileurl

#post member form
@csrf_exempt
def memmberDetails(request):
     retstatus={"status":"1","message":"Successfully Saved"}
     try:
        picture=''
        print("From AngularMember")
        a=json.loads(request.body)
        print(a)
        print("hai")
        
        print(a["image"])
        obj=Address(name=a["name"],place=a["place"],city=a["city"],state=a["state"],image=a["image"])
       
        #savefile(file,filename)
        
        if Address.objects.filter(name=a["name"]) or Address.objects.filter(place=a["place"]):
            print("Already Exist,Use Another Name and Place")
            retstatus={"status":"0","message":"Already Exist,Use Another Name and Place"}
        else:
            obj.save()
            print(obj)
     except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
     return JsonRessponse(retstatus)


# for getting in to selectbox
@csrf_exempt
def getVenueDetails(request):
    
        print("get Data Call From Angular1 ")
        venue9 =Venue.objects.all().values('name')  # or simply .values() to get all fields
        venue_list = list(venue9)  # important: convert the QuerySet to a list objec
        return JsonResponse( venue_list, safe=False) 
       

        
#post evenform
@csrf_exempt
def eventDetails(request):
    retstatus={"status":"1","message":"Successfully Saved"}
    try: 
        print("From AngularEvent")
        s=json.loads(request.body)
        print(s)
        #must be use first()..bcz "Event.venue" must be a "Venue" instance.
        b=Venue.objects.filter(name=s["venue"]).first()
        print(b)
        if b :
           ob=Event(name=s["name"],event_date=s["event_date"],description=s["description"],venue=b)
           if Event.objects.filter(name=s["name"]):
                retstatus={"status":"0","message":"Name already Exist"}
           else: 
                ob.save()
                print(ob)
        else:
            retstatus={"status":"0","message":"No venue exist"}

    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}

    return JsonResponse( retstatus)

#to dashbord
@csrf_exempt
def getEventDetails(request):
    even=[]
    print("Get Event details to Dashboard")
    d=Event.objects.all()
    for event in d:
        #"id" is the angular form.."event.id" is the table column
        even.append({"id":event.id,"name":event.name,"event_date":event.event_date,"description":event.description,"venue":event.venue.name})
    print(event)
    return JsonResponse(even, safe=False) 
#to dashbord
@csrf_exempt
def getMemberDetails(request):
    member=[]
    print("Get Member details to Dashboard")
    m=Address.objects.all()
    print(m)
    for address in m:
        member.append({"name":address.name,"place":address.place,"city":address.city,"state":address.state,"id":address})
    print(address)
    return JsonResponse(member, safe=False) 

#to dashbord
@csrf_exempt
def getVenueDetails1(request):
    venue3=[]
    print("Get Member details to Dashboard")
    v=Venue.objects.all()
    print(v)
    for venues in v:
        venue3.append({"id":venues.id,"name":venues.name,"address":venues.address,"zip_code":venues.zip_code,"phone":venues.phone,"email":venues.email_address})
    print(venues)
    return JsonResponse(venue3, safe=False) 


#its own work..    
@csrf_exempt
def post2(request):
    retstatus={"status":"1","message":"Successfully Saved"}
    try:
        print("call from angular")
        x=json.loads(request.body)
        print(x)    
           # return JsonResponse(x)
    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
    print(retstatus)
    return JsonResponse(retstatus,safe=False)

 #its own work..       
@csrf_exempt
def getVenueDetails2(request):
    print("get Data Call From Angular1 ")
    venue =Venue.objects.all().values('name')  # or simply .values() to get all fields
    print(venue)
    venue_list = list(venue)  # important: convert the QuerySet to a list objec
    print(venue_list)
    return JsonResponse( venue_list, safe=False) 

#from django to angular member form...all values in table..to show in form..
@csrf_exempt
def getMeberById(request): 
    print("member Details")
    d=request.GET["abc"]
    print(d)
    address = Address.objects.filter(id=d).values()
    print(address)
    member_list=list(address)
    return JsonResponse( member_list, safe=False)

#from django to angular event form...all values in table..to show in form..
@csrf_exempt
def getEventById(request): 
    eventsArray=[]
    print("Event Details")
    a=request.GET["id"]
    print(a)
    events = Event.objects.filter(id=a)
    print(events)
    for event in events:
        eventsArray.append({"id":event.id,"name":event.name,"event_date":event.event_date,"description":event.description,"venue":event.venue.name})
    return JsonResponse(  eventsArray, safe=False)
    
#from django to angular venue form...all values in table..to show in form..
@csrf_exempt 
def getvenueById(request): 
    print("Venue Details")
    b=request.GET["dca"]
    print(b)
    venue = Venue.objects.filter(id=b).values()
    print(venue)
    venue_list=list(venue)
    return JsonResponse( venue_list, safe=False) 

#by deleting venue by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request): 
@csrf_exempt 
def deleteVenueById(request): 
    retstatus={"status":"1","message":"Successfully Deleted"}
    try:
        print("Venue Details")
        b=request.GET["idc"]
        print(b)
        venue = Venue.objects.filter(id=b)
        print(venue)
        venue.delete()
        # venue_list=list(venue)
        #return JsonResponse( venue_list, safe=False) 
    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
        print(retstatus)
    return JsonResponse(retstatus,safe=False)


#by deleting member by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request):
@csrf_exempt 
def deleteMemberById(request): 
    retstatus={"status":"1","message":"Successfully Deleted"}
    try:
        print("Member Details")
        b=request.GET["xyz"]
        print(b)
        member = Address.objects.filter(id=b)
        print(member)
        member.delete()
        # venue_list=list(venue)
        #return JsonResponse( venue_list, safe=False) 
    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
        print(retstatus)
    return JsonResponse(retstatus,safe=False)

#by deleting event by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request):
@csrf_exempt 
def deleteEventById(request): 
    retstatus={"status":"1","message":"Successfully Deleted"}
    try:
        print("EventDetails")
        b=request.GET["abc"]
        print(b)
        event = Event.objects.filter(id=b)
        print(event)
        event.delete()
        # venue_list=list(venue)
        #return JsonResponse( venue_list, safe=False) 
    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
        print(retstatus)
    return JsonResponse(retstatus,safe=False)


#by updating venue by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request):
@csrf_exempt
def updateEventDetails(request):
    retstatus={"status":"1","message":"Successfully Saved"}
    try: 
        print("From AngularEvent")
        id=int(request.GET["id"])
        print(id)
        s=json.loads(request.body)
        print(s)
        #must be use first()..bcz "Event.venue" must be a "Venue" instance.
        #name is the table column,s[name] is  from angular.
        print("test1")
        b=Venue.objects.filter(name=s["venue"] ).first()
        print("Test2")
        print(b)
        if b :
           ob=Event(id=id,name=s["name"],event_date=s["event_date"],description=s["description"],venue=b)
           print("test3")
           filterdObject=Event.objects.filter(name=s["name"]).first()
           duplicatedStatus=False
           if filterdObject:
               if filterdObject.id!=id:
                   duplicatedStatus=True
           print("test4", filterdObject)
           if duplicatedStatus:
                retstatus={"status":"0","message":"Name already Exist"}
           else: 
                ob.save()
                print(ob)
        else:
            retstatus={"status":"0","message":"No venue exist"}

    except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}

    return JsonResponse( retstatus)


#by deleting venue by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request):

@csrf_exempt
def updateMemberDetails(request):
     retstatus={"status":"1","message":"Successfully Saved"}
     try:
        print("From AngularMember")
        #passing id.. in variable in id from angular ..
        b=int(request.GET["abc"])
        print(b)
        a=json.loads(request.body)
        print(a)
        #leftside tablename='a["name"]' is from angularname..id already intialize above..so not a[id]..
        obj=Address(id=b,name=a["name"],place=a["place"],city=a["city"],state=a["state"])
       # if Address.objects.filter(name=a["name"]) or Address.objects.filter(place=a["place"]):
        print(obj)
        print("Test Members")

        duplicatedStatus=False
        #.first() must be entered.. if not entered first(),otherwise not show any error both(A,D)
        filtername=Address.objects.filter(name=a["name"]).first()
        print(filtername) 
        if filtername:
             if filtername.id!=id:
                print("test9")
                duplicatedStatus=True
        print("test10",filtername)
        if duplicatedStatus:
            print("Already Exist,Use Another Name ")  
            retstatus={"status":"0","message":"Already Exist,Use Another Name"} 
        else:    
            obj.save()
            print(obj)
     except Exception as e:
         print(e)
         retstatus={"status":"0","message":"Error Occured"}

     return JsonResponse(retstatus)

#by deleting venue by id...after values in form(above),def getEventById(request):,def getMeberById(request):,def getEventById(request):
@csrf_exempt
def updateVenueDetails(request):
     retstatus={"status":"1","message":"Successfully Saved"}
     try:
        print("From AngularMember")
        #passing id.. in variable in id from angular ..
        id=int(request.GET["bcd"])
        print(id)
        a=json.loads(request.body)
        print(a)
        #leftside tablename='a["name"]' is from angularname..id already intialize above..so not a[id]..
        venue1=Venue(id=id,name=a["name"],address=a["address"],zip_code=a["zip_code"],phone=a["phone"],email_address=a["email"])
        #if Venue.objects.filter(name=z["name"]) or Venue.objects.filter(email_address=z["email"]):
        #section for validation for updation....
        duplicatedStatus=False
        #.first() must be entered.. if not entered first(),otherwise not show any error both(A,D)
        filtername=Venue.objects.filter(name=a["name"]).first()
        print(filtername) 
        if filtername:
             if filtername.id!=id:
                print("test9")
                duplicatedStatus=True
        print("test10",filtername)
        if duplicatedStatus:
            print("Already Exist,Use Another Name ")  
            retstatus={"status":"0","message":"Already Exist,Use Another Name"} 
        else:    
            venue1.save()
            print(venue1)
     except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
    #  return JsonResponse(z)
     return JsonResponse(retstatus)
     
@csrf_exempt
def loginDetails(request):
     retstatus={"status":"1","message":"Successfully Saved"}
     try:
        a=json.loads(request.body)
        print(a)
        username=a["email"]
        password=a["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("User authenticated")
            retstatus={"status":"1","message":"User authenticated"}
        else:
            print("User not authenticated")
            retstatus={"status":"1","message":"User not authenticated"}
     except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}
     return JsonResponse(retstatus)

def datafilter(request):
    print("inside....Filter")
    print(request.GET["name"])
    address=Address.objects.filter(name=request.GET["name"]).values()
    addressList = list(address)
    return JsonResponse(addressList, safe=False)



@csrf_exempt
def reactMemmberDetails(request):
     retstatus={"status":"1","message":"Successfully Saved"}
     try:
        print("From AngularMember")
        a=json.loads(request.body)
        print(a)
        print("hai")
        obj=Address(name=a["name1"],place=a["place1"],city=a["city1"],image=a["image"])
      
        print(obj)
        if Address.objects.filter(name=a["name1"]):
            retstatus={"status":"0","message":"Name Already Exist"}
        else:
            obj.save()
            print(obj)
     except Exception as e:
        print(e)
        retstatus={"status":"0","message":"Error Occured"}

     return JsonResponse(retstatus)



#post venue form
@csrf_exempt
def reactVenue(request):
    status={"status":"1","message":"Successfully saved"}
    try:
        print("From Testing")
        z=json.loads(request.body)
        print(z)
        venue1=Venue(name=z["venue_name"],address=z["venue_address"],zip_code=z["venue_zipcode"],phone=z["venue_phone"],email_address=z["venue_email"])
        if Venue.objects.filter(name=z["venue_name"]) or Venue.objects.filter(email_address=z["venue_email"]):
            print("Already Exist,Use Another Name and Email")  
            status={"status":"0","message":"Already Exist,Use Another Name and Email"} 
        else:    
            venue1.save()
            print(venue1)
    except Exception as e:
        print(e)
        status={"status":"0","message":"Error Occured"}
    #  return JsonResponse(z)
    return JsonResponse(status)

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Address.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)








