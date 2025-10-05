from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime

from .models import ContactSubmission
from services.models import Service
import threading

def send_emails_async(submission, name, email):
    """Send business + user emails in background"""
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import render_to_string
    from django.conf import settings
    from datetime import datetime

    try:
        # Business email
        subject_business = f'New Contact Form Submission from {name}'
        html_content_business = render_to_string(
            'contacts/email/business_notification.html',
            {'submission': submission}
        )
        text_content_business = f"New contact from {name}\nEmail: {email}\nMessage:\n{submission.message}"

        msg_business = EmailMultiAlternatives(
            subject=subject_business,
            body=text_content_business,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
        )
        msg_business.attach_alternative(html_content_business, "text/html")
        msg_business.send()

        # User email
        subject_user = 'Thank you for contacting Lumo Software Solutions'
        context_user = {'name': name, 'year': datetime.now().year}
        html_content_user = render_to_string('contacts/email/user_confirmation.html', context_user)
        text_content_user = f"Hi {name},\n\nThank you for reaching out to Lumo Software Solutions."

        msg_user = EmailMultiAlternatives(
            subject=subject_user,
            body=text_content_user,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        msg_user.attach_alternative(html_content_user, "text/html")
        msg_user.send()

    except Exception as e:
        print(f"[Email Error] {e}")


def contact_view(request):
    """Handle contact form submissions"""
    services = Service.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company', '')
        service_id = request.POST.get('service_of_interest')
        message = request.POST.get('message')
        
        # Get service instance if provided
        service = None
        if service_id:
            try:
                service = Service.objects.get(id=service_id)
            except Service.DoesNotExist:
                pass
        
        # Create contact submission
        submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            company=company,
            service_of_interest=service,
            message=message
        )
        
        threading.Thread(target=send_emails_async, args=(submission, name, email)).start()

        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contacts:contact_success')
    
    context = {
        'services': services,
    }
    return render(request, 'contacts/contact.html', context)

def contact_success(request):
    """Success page after contact form submission"""
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'contacts/contact_success.html', context)


