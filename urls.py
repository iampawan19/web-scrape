from django.urls import path, include
from .views import HomeView, JobDetailView

app_name = 'scraper'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job/<int:job_id>/', JobDetailView.as_view(), name='job_detail')
]
