from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('table/',views.table,name='blog-table'),
    path('index/',views.index,name='index'),
    path('info/',views.info,name='info'),
    path('Civil_Engineering',views.civil,name='civil'),
    path('Mechanical_Engineering',views.mech,name='mech'),
    path('Electrical&amp;_Electronics_Engineering',views.eee, name='eee'),
    path('Electronics_&amp;_Communications_Engineering',views.ece,name='ece'),
    path('Computer_Sciences_&amp;_Engineering',views.cse,name='cse'),
    path('Information_Technology',views.it,name='it'),
    path('Chemical_Engineering',views.ce,name='ce'),
    path('Bio_Technology',views.bio,name='bio'),
    path('MCA',views.mca,name='mca'),
    path('CBIT-School_Management_Studies',views.management,name='management'),
    path('Physics',views.phy,name='phy'),
    path('Chemistry',views.chem,name='chem'),
    path('Mathematics',views.math,name='math'),
    path('English',views.eng,name='eng'),
    path('Physical_Education',views.phyedu,name='phyedu'),
    
    
]
