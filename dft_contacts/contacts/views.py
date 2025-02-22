from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact
from contacts.forms import ContactForm


def contacts(request):
    all_contacts = Contact.objects.all()
    template = loader.get_template("contacts_template.html")
    form = ContactForm()

    context = {}
    context["all_contacts"] = all_contacts
    context["form"] = form

    return HttpResponse(template.render(context, request))
