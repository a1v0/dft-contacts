"""
To seed the contacts database with dummy data, do the following:

Run `py manage.py shell` in the CLI.

This will open Python in your terminal. Then paste the contents
of this file into the CLI. This will generate several records.
"""

from contacts.models import Contact


# UNCOMMENT THIS LOOP TO DELETE EXISTING DATA IN THE DATABASE BEFORE SEEDING
# for existing_contact in Contact.objects.all():
#     existing_contact.delete()


contact0 = Contact(
    first_name="Albert",
    last_name="Ross",
    email="albert@example.com",
    mobile="07111 111 111",
    type="3",
)
contact1 = Contact(
    first_name="Barbara",
    last_name="Seville",
    email="seville@example.com",
    mobile="07111 111 111",
    type="2",
)
contact2 = Contact(
    first_name="Camilla",
    last_name="Highwater",
    email="camilla@example.com",
    mobile="07111 111 111",
    type="5",
)
contact3 = Contact(
    first_name="N. G.",
    last_name="Near",
    email="ngnear@example.com",
    mobile="07111 111 111",
    type="4",
)
contact4 = Contact(
    first_name="Sean",
    last_name="Delier",
    email="sean@example.com",
    mobile="07111 111 111",
    type="2",
)
contact5 = Contact(
    first_name="Barb",
    last_name="Dwyer",
    email="barb@example.com",
    mobile="07111 111 111",
    type="3",
)
contact6 = Contact(
    first_name="Horace",
    last_name="Cope",
    email="horace@cope.com",
    mobile="07111 111 111",
    type="1",
)
contact7 = Contact(
    first_name="I. C. Theresa",
    last_name="Green",
    email="theresa@example.com",
    mobile="07111 111 111",
    type="1",
)

contacts_list = [
    contact0,
    contact1,
    contact2,
    contact3,
    contact4,
    contact5,
    contact6,
    contact7,
]

for contact in contacts_list:
    contact.save()
