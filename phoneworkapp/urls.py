from django.urls import path
from.import views
urlpatterns=[
    path('',views.home),
    path('phonework/',views.addphone, name='addphone'),
    path('display/',views.display, name='display'),
    path('delete/', views.delete, name='delete'),  
    path('update/', views.update, name='update'),
    
]