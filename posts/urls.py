from django.urls import path
from . import views

# This will use to identify if multiple apps are availabel.
app_name="post"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<slug:slug>", views.post_page, name="page"),
]
