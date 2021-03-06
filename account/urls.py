from django.urls import path

from api import views


urlpatterns = [
    path('create/',views.CreateUserView.as_view(),name='create-user'),
    path('login/',views.LoginUserView.as_view(),name='login-user'),
    path('profile-pic/',views.UpdateProfilePictureView.as_view(),name='profile-pic'),
    path('get-token/',views.TokenGetView.as_view(),name='token-get'),
    path('get-user/',views.get_user_data,name='get-user'),
    path('reset-password-email/',views.GetResetPasswordURLView.as_view(),name='reset-password-email'),

    path('reset-password/<uidb64>/<token>/',views.ResetPassword.as_view(),name='reset-password'),
    path('reset-complete',views.reset_complete,name='reset-complete')


]