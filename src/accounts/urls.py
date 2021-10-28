from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='registration'),
    path('<pk>/', user_info_view, name='information'),
    path('<pk>/change_info/', change_info_view, name='change_information')
]
