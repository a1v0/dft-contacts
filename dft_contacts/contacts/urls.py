from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.contacts, name="contacts"
    ),  # As soon as more than one single view is needed, this line can be deleted in favour of better routing
    path("contacts/", views.contacts, name="contacts"),
]
