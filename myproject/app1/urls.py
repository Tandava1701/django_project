from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('interier/',home2,name='home2'),
    path('sign up/',signup,name='signup'),
    path('hai/',home3,name='home3'),
    path('login/',login,name='login1'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('service/',service,name='service'),
    path('order/',order,name='order'),
    path('aboutus/',aboutus,name='aboutus'),
    path('order1/',order1,name='order1'),

     path('login/reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html "),name="reset_password"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('login/reset<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm" ),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete "),

]