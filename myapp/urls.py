from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('saveprofile',views.save_profile,name='save_profile'),
    path('<int:id>/',views.resume,name='resume'),
    path('download/<int:id>/',views.download_resume,name='download_resume'),
    path('edit/<int:id>/',views.edit_resume,name='edit_resume'),
path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]