from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("notes/", include("notes.urls")),
    path("", RedirectView.as_view(url="/notes/")),  # Adaugă această linie
]
