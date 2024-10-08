from django.shortcuts import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

# Create your views here.
class SuccessView(TemplateView):
    template_name = "success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("success")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
        Received message below from {email}, {subject}, {message}"""

        print("Sending email...")  # Debugging statement
        print(full_message)  # Debugging statement

        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        print("Email sent successfully.")  # Debugging statement

        return super(ContactView, self).form_valid(form)
