from django import template
from info.models import University, Actors

register = template.Library()


@register.inclusion_tag('info/university_list.html')
def show_categories():
    categories = University.objects.all()
    return {'categories': categories}
