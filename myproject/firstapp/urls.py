from django.urls import path,include
from . import views
urlpatterns = [
   
    path('', views.firstpage,name='firstapp-home'),
    path('secondpage', views.secondpage,name='firstapp-about'),
    path('profile', views.studentdetails,name='firstapp-profile'),
    path('test/', views.test,name='testapp'),
    path('post', views.post1,name='postapp'),
    path('venue/',views.venueDetails,name='postvenue'),
    path('member/',views.memmberDetails,name='postmember'),
    path('getVenueName/',views.getVenueDetails,name='getvenuename'),
    path('event/',views.eventDetails,name='postevent'),
    #get from django to angular(dashbord)
    path('getallevent/',views.getEventDetails,name='getallevent'),
    path('getallmember/',views.getMemberDetails,name='getallemember'),
    path('getallvenue/',views.getVenueDetails1,name='getallvenue'),
    

    path('getallvenue2/',views.getVenueDetails2,name='getallvenue2'),
    path('post2/', views.post2,name='postapp2'),
    #update
    path('editmember/', views.getMeberById,name='editmember'),
    path('editevent/', views.getEventById,name='editevent'),
    path('editvenue/', views.getvenueById,name='editvenue'),
    #delete
    path('deletevenue/', views.deleteVenueById,name='deletevenue'),
    path('deletmember/', views.deleteMemberById,name='deletevenue'),
    path('deleteevent/', views.deleteEventById,name='deleteevent'),

    #updation
    path('updateevent/', views.updateEventDetails,name='updateevent'),
    path('updatemember/', views.updateMemberDetails,name='updatemember'),
    path('updatevenue/', views.updateVenueDetails,name='updatevenue'),

    path('login/', views.loginDetails,name='login'),
    #React
    path('filter/', views.datafilter,name='filter'),
    path('reactmember/', views.reactMemmberDetails,name='reactmember'),
    path('reactvenue/', views.reactVenue,name='reactvenue'),
    

    

    


    
    
                    
        
]