from django.urls import path

from subscribe.views import subscribe_page

urlpatterns = [
    path('', subscribe_page, name='email')
]