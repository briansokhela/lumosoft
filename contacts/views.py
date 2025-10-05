from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail  

from .models import ContactSubmission
from services.models import Service
import threading

def send_emails_async(submission, name, email):
    """Send business and user emails asynchronously using SendGrid API"""
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        # Business email
        subject_business = f'New Contact Form Submission from {name}'
        html_content_business = render_to_string(
            'contacts/email/business_notification.html',
            {'submission': submission}
        )

        msg_business = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=settings.CONTACT_EMAIL,
            subject=subject_business,
            plain_text_content=f"New contact from {name}\nEmail: {email}\nMessage:\n{submission.message}",
            html_content=html_content_business
        )
        sg.send(msg_business)
        print('sent business_notification')

        # User confirmation email
        subject_user = 'Thank you for contacting Lumo Software Solutions'
        html_content_user = render_to_string(
            'contacts/email/user_confirmation.html',
            {'name': name, 'year': datetime.now().year}
        )

        msg_user = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=email,
            subject=subject_user,
            plain_text_content=f"Hi {name},\n\nThank you for reaching out to Lumo Software Solutions.",
            html_content=html_content_user
        )
        sg.send(msg_user)
        print('sent user_confirmation')
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


