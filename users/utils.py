
from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginateProfiles(request, profiles, results):

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:

        profiles = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    return custom_range, profiles



def searchProfiles(request):
    search_content = ''

    if request.GET.get('search_content'):
        search_content = request.GET.get('search_content')

    skills = Skill.objects.filter(name__icontains=search_content)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_content) | Q(short_intro__icontains=search_content) | Q(skill__in =skills))



    return profiles, search_content