from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Actors, University, Info_about_university, GlobalInformation


def home_page(request):
    return render(request, 'info/home.html')


class ActorDescriptionView(DetailView):
    model = Actors
    template_name = 'info/actor_description.html'
    context_object_name = 'qs'


def uni_description(request, university_id):
    qs = Info_about_university.objects.filter(university_id=university_id)
    actors = Actors.objects.filter(university_id=university_id)
    global_info = GlobalInformation.objects.filter(university_id=university_id)
    category = University.objects.get(pk=university_id)
    context = {'qs': qs, 'category': category, 'actors': actors, 'global_info': global_info}
    return render(request, 'info/uni_description.html', context)
