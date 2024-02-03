from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # URL pattern for the Django admin interface
    path("admin/", admin.site.urls),
    # URL pattern for the login view
    path("accounts/login/", LoginView.as_view(), name="login"),
    # URL pattern for the logout view
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    # URL pattern for including the URLs from the 'notes' app
    path("notes/", include("notes.urls")),
    # URL pattern for redirecting to the 'notes' app (added line)
    path("", RedirectView.as_view(url="/notes/")),
]
