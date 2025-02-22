from django.db import models


class Contact(models.Model):
    CONTACT_TYPES = [
        ("1", "Family"),
        ("2", "Friends"),
        ("3", "Work"),
        ("4", "Trade"),
        ("5", "Other"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    contact_type = models.CharField(
        max_length=2,
        choices=CONTACT_TYPES,
    )

    def type_verbose(self):
        # This method exists because I couldn't get get_contact_type_display to work in the template
        return dict(Contact.CONTACT_TYPES)[self.contact_type]
