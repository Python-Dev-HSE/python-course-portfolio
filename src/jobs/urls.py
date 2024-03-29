from django.urls import path
from jobs.views import IndexJobDetailView


urlpatterns = [
    path("<int:pk>/",
         IndexJobDetailView.as_view(),
         name="job"),
]