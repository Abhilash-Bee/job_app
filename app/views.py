from django.shortcuts import render
from app.models import JobPost

# Create your views here.
def home_page(request):
    jobs = JobPost.objects.all()
    context = {
        "jobs" : jobs,
    }
    return render(request, "app/home.html", context=context)


def job_detail(request, slug):
    data = JobPost.objects.get(slug=slug)
    context = {
        "data" : data
    }
    return render(request, 'app/details.html', context=context)

    