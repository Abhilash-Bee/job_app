from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', home_page, name='home'),
    path('details/<slug:slug>', job_detail, name='job_details'),
]