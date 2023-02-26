from django.urls import path,re_path as url
from . import views
from django.contrib.auth.views import logout_then_login,LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView
urlpatterns=[
    #the default authentication check registration/template.html to load template
    #default login view
    #path("",views.process_login_form,name="login"),
    path("",LoginView.as_view(),name="login"),
    #default logout view
    path("logout",LogoutView.as_view(),{'template_name': 'registration/logout.html'},name="logout"),
    #default logout then login view
    path("logoutthenlogin",logout_then_login,name="logout_then_login"),
    #dashboard view url
    path("dashboard",views.dashboard,name="dashboard"),
    #default url to password change
    path("password-change",PasswordChangeView.as_view(),name="password_change"),
    #default view url for password change done
    path("password-change/done/",PasswordChangeDoneView.as_view(),name="password_change_done"),
    #below are the views for reset password
    path("password-reset",PasswordResetView.as_view(),name="password_reset"),
    path("password-reset/done/",PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("passoword_reset/complete/",PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    #url for registration form
    path("register",views.register,name="register"),
    path("delete",views.delete_account_user,name="delete"),
    path("delete-done",views.delete_done,name="delete_done"),
    #path to edit account information
    path("edit",views.edit,name="edit"),
    #path for settings
    path("settings",views.settings,name="settings"),
    path("change-profile",views.profile_pic_view,name="change_profile"),
    path('users/',views.user_list,name="user_list"),
    path('users/<username>',views.user_details,name="user_details"),
]
