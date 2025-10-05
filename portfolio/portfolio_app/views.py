from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Technology, Skill, Project, SocialLink
from .forms import ContactForm

def home(request):
    # Get technologies grouped by category
    technologies_using = Technology.objects.filter(is_interested=False)
    technologies_interested = Technology.objects.filter(is_interested=True)

    # Get skills
    skills = Skill.objects.all()

    # Get projects (featured first)
    projects = Project.objects.all()

    # Get social links
    social_links = SocialLink.objects.filter(is_active=True)

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact.subject}",
                    message=f"From: {contact.name} ({contact.email})\n\n{contact.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            except Exception as e:
                messages.warning(request, 'Your message was saved, but email notification failed.')

            return redirect('portfolio_app:home')
    else:
        form = ContactForm()

    context = {
        'technologies_using': technologies_using,
        'technologies_interested': technologies_interested,
        'skills': skills,
        'projects': projects,
        'social_links': social_links,
        'contact_form': form,
    }

    return render(request, 'portfolio_app/home.html', context)