from django.urls import path

from .views import MechanicDetailView, MechanicListCreateView

urlpatterns = [
    path(
        "mechanics/",
        MechanicListCreateView.as_view(),
        name="mechanic-list-create",
    ),
    path(
        "mechanics/<int:pk>/",
        MechanicDetailView.as_view(),
        name="mechanic-detail",
    ),
]
