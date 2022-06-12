from django.urls import path
from . import views

urlpatterns = [
    #-------------------------------users api urls ---------------------------------
    path('users/', views.getUsers, name='users'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register' , views.registerUser , name='register user'),
    path('users/profile/update', views.updateUserProfile, name='user_profile'),
    path('users/profile', views.getUserProfile, name='user_profile'),
   #--------------------------------PFE urls ---------------------------------------
   path('PFE/getAll' , views.getPfes , name='all_pfes'),
   path('PFE/add' , views.ADD_PFE , name='new_pfe'),
   path('PFE/Delete/<int:pk>' , views.delete_pfe , name='delete'),
   path('PFE/unique_PFE/student/<str:pk>' , views.GET_SINGLE_PFE_by_student , name='PFE_UNIQUE'),
   path('PFE/unique_PFE/institue/<str:pk>', views.GET_SINGLE_PFE_by_institue, name='PFE_UNIQUE'),
    path('PFE/unique_PFE/year/<int:pk>', views.GET_SINGLE_PFE_by_year, name='PFE_UNIQUE')
]
 
