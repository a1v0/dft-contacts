from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact
from contacts.forms import ContactForm


def handle_form_submit(request, form):
    if "save" in request.POST:
        id = request.POST.get("save")
        if not id:
            form = ContactForm(request.POST)
        else:
            contact = Contact.objects.get(id=id)
            form = ContactForm(request.POST, instance=contact)

        form.save()

        form = ContactForm()  # Reset form before returning
        return form

    if "delete" in request.POST:
        id = request.POST.get("delete")
        contact = Contact.objects.get(id=id)
        contact.delete()
        return form

    if "edit" in request.POST:
        id = request.POST.get("edit")
        contact = Contact.objects.get(id=id)
        form = ContactForm(instance=contact)
        return form

    raise ValueError("No valid CRUD operator found in POST request.")


def contacts(request):
    all_contacts = Contact.objects.all()
    template = loader.get_template("contacts_template.html")
    form = ContactForm()

    if request.method == "POST":
        form = handle_form_submit(request, form)

    context = {}
    context["all_contacts"] = all_contacts
    context["form"] = form

    return HttpResponse(template.render(context, request))
