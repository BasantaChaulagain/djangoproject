from django.shortcuts import render, get_object_or_404
from .models import Subject,Practical,Photo
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    practicals = Practical.objects.all()
    subjects = Subject.objects.all()
    query = request.GET.get("q")
    if query:
        practicals = practicals.filter(
            Q(title__icontains=query)
        ).distinct()
        subjects = Subject.objects.filter(practical=practicals)
        return render(request, 'practicals/index.html',{'practicals': practicals, 'subjects': subjects})
    else:
        return render(request, 'practicals/index.html',{'practicals': practicals, 'subjects': subjects})

def detail(request, practical_id):
    photo = Photo.objects.filter(practical=practical_id)
    practical = get_object_or_404(Practical, pk=practical_id)
    paginator= Paginator(photo,1)

    page = request.GET.get('page')
    try:
       photo = paginator.page(page)
    except PageNotAnInteger:
       photo = paginator.page(1)
    except EmptyPage:
       photo = paginator.page(paginator.num_pages)

    return render(request, 'practicals/detail.html',{'photo':photo, 'practical':practical})