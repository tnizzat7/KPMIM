from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name="index"),
    path("course/",views.course,name="course"),
    path("mentor/",views.mentor,name="mentor"),
    path("searchC/", views.Search,name="search"),
    path("searchM/", views.SearchM,name="searchM"),
    path("course/update_course/<str:code>", views.update_course,name="update_course"),
    path('course/update_course/save_update_course/<str:code>', views.save_update_course, name='save_update_course'),
    path('course/delete_course/<str:code>', views.delete_course, name='delete_course')
    
]