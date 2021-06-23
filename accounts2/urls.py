from django.urls import path, reverse_lazy
from accounts2 import views
from django.contrib.auth import views as auth_views

app_name = 'accounts2'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),

    path('user_profile/', views.edit_profile, name='edit_profile'),
    path('user_password/', views.change_password, name='change_password'),

    # Reset password section

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts2/password_reset.html',
             success_url=reverse_lazy('accounts2:password_reset_done'),
             email_template_name='accounts/registration/password_reset_email.html'
         ),
         name='reset_password'),


    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts2/password_reset_sent.html',
         ),
         name='password_reset_done'),


    path('reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts2/password_reset_form.html',
             success_url=reverse_lazy('accounts2:password_reset_complete')
         ),
         name='password_reset_confirm'),


    path('rest_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts2/password_reset_done.html',
         ),
         name='password_reset_complete')
]
