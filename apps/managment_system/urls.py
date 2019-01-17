from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_page',views.registerpage),
    path('register', views.register),
    path('login_page', views.loginpage),
    path('login', views.login),
    path('logout',views.logout),
    path('dashboard', views.dashboard),
    path('delete/<int:user_id>', views.delete),
    path('adduser', views.adduser),
    path('newuser', views.newuser),
    path('edit/<int:user_id>', views.edit),
    path('nameupdate/<int:user_id>', views.nameupdate),
    path('descupdate/<int:user_id>', views.descupdate),
    path('view/<int:user_id>', views.view),
    path('view/add_message',views.add_message),
    path('comment',views.comment),
    path('message/delete/<int:message_id>', views.delete_message)
]