from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def template_mail(subject, recipient_list, template_path, context=None, sender=None):
    """
    Sends an email with a rendered Django template.

    :param subject: The subject of the email.
    :param recipient_list: A list of recipients for the email.
    :param template_path: The path to the Django template to be used for the email.
    :param context: A dictionary containing any variables to be used in the template.
    :param sender: The email address that the email should appear to come from. Defaults to the value of the DEFAULT_FROM_EMAIL setting.
    """
    if context is None:
        context = {}

    # Render the template with the provided context
    html_content = render_to_string(template_path, context)

    # Create an EmailMultiAlternatives object
    msg = EmailMultiAlternatives(subject, '', sender, recipient_list)

    # Add the rendered HTML content as an alternative content type
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()

