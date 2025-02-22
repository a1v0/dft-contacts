from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def contacts(request):
    template = loader.get_template("contacts_template.html")
    return HttpResponse(template.render())
