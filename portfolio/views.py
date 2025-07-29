from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project, WorkExperience, Certificate
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    experiences = WorkExperience.objects.all()
    certificates = Certificate.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            email_message = f"You have received a message from {name} ({email_from}):\n\n{message}"
            
            # Send email
            send_mail(
                subject,
                email_message,
                'your-website@example.com',
                ['nupurdharpure01@gmail.com'], 
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio:home')
    else:
        form = ContactForm()
    
    context = {
        'projects': projects,
        'experiences': experiences,
        'certificates': certificates,
        'form': form,
    }
    
    return render(request, 'portfolio/home.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def certificate_detail(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    return render(request, 'portfolio/certificate_detail.html', {'certificate': certificate})