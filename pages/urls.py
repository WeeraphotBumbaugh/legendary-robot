from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    MissionPageView,
    CareersPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("mission/", MissionPageView.as_view(), name="mission"),
    path("careers/", CareersPageView.as_view(), name="careers"),
]
