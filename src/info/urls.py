from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('', home_page, name='home'),
    path('university/<int:university_id>/', uni_description, name='uni_description'),
    path('actor/<slug>/', ActorDescriptionView.as_view(), name='actor_description')
]
