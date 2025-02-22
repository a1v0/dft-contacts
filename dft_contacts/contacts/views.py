from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact
from contacts.forms import ContactForm


def handle_form_submit(request, form):
    if "save" in request.POST:
        form = ContactForm(request.POST)
        form.save()
        return

    if "delete" in request.POST:
        id = request.POST.get("delete")
        contact = Contact.objects.get(id=id)
        contact.delete()
        return

    if "edit" in request.POST:
        pass
        return

    raise ValueError("No valid CRUD operator found in POST request.")


def contacts(request):
    all_contacts = Contact.objects.all()
    template = loader.get_template("contacts_template.html")
    form = ContactForm()

    if request.method == "POST":
        handle_form_submit(request, form)

    context = {}
    context["all_contacts"] = all_contacts
    context["form"] = form

    return HttpResponse(template.render(context, request))
