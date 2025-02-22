from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact


def contacts(request):
    all_contacts = Contact.objects.all()
    template = loader.get_template("contacts_template.html")
    context = {"all_contacts": all_contacts}

    return HttpResponse(template.render(context, request))
