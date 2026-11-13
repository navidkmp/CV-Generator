from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
import io
def dashboard(request):
    resumes = Profile.objects.all()
    return render(request,'myapp/dashboard.html',{'resumes':resumes})

def save_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        profile = Profile(name=name,email=email,phone=phone,degree=degree,school=school,university=university,summary=summary,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('myapp:dashboard')
    return render(request,'myapp/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,'myapp/resume.html',{'user_profile':user_profile})


def download_resume(request,id):
    user_profile = get_object_or_404(Profile,id=id)
    template_path = 'myapp/download_resume.html'
    context = {'user_profile':user_profile}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={user_profile.name}_CV.pdf'
    pisa_status = pisa.CreatePDF(io.BytesIO(html.encode('utf-8')), dest=response, encoding='utf-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response


from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile

def edit_resume(request, id):
    profile = get_object_or_404(Profile, id=id)
    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.degree = request.POST.get('degree')
        profile.school = request.POST.get('school')
        profile.university = request.POST.get('university')
        profile.summary = request.POST.get('summary')
        profile.previous_work = request.POST.get('previous_work')
        profile.skills = request.POST.get('skills')
        profile.save()
        return redirect('myapp:dashboard')

    return render(request, 'myapp/accept.html', {'user_profile': profile})


def delete_resume(request, id):
    profile = get_object_or_404(Profile, id=id)

    if request.method == 'POST':
        profile.delete()
        return redirect('myapp:dashboard')

    return redirect('myapp:dashboard')