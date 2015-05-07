from django.template import loader, Context
from django.core.mail import send_mail
from django.conf import settings


def send_tpl_email(template_name, email, context, from_email=None, **kwds):
    t = loader.get_template(template_name)
    c = Context(context)
    subject, txt = t.render(c).split("\n", 1)
    from_email = from_email if from_email else settings.DEFAULT_FROM_EMAIL
    send_mail(subject=subject, message=txt, from_email=from_email, recipient_list=[email], **kwds)