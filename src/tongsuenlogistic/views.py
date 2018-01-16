from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.urls import reverse

def home_page(request):
    
    if request.session.get("lang")== 'TH':
        context = {
        "lang":"TH"
        }
    elif request.session.get("lang") == 'EN':
        context = {
        "lang":"EN"
        }
    elif request.session.get("lang") == 'CN':
        context = {
        "lang":"CN"
        }
    else:
        context = {
        "lang":"TH"
        }
    return render(request,"index.html",context)

def about_page(request):
    return render(request,"index.html",{})

def contact_page(request): 
    return render(request,"index.html",{})

def change_lang_to_thai(request):
    request.session['lang'] = 'TH'
    context = {
        "lang":"TH"
        }
    return render(request,"index.html",context)
    
def change_lang_to_eng(request):
    request.session['lang'] = 'EN'
    context = {
        "lang":"EN"
        }
    return render(request,"index.html",context)

def change_lang_to_cn(request):
    request.session['lang'] = 'CN'
    context = {
        "lang":"CN"
        }
    return render(request,"index.html",context)

def email(request): #contact@tongsuenlogistics.co.th
    rendered = render_to_string('email.html', { 'foo': 'bar' })
    msg = EmailMessage('subject', rendered, 'tongsuenDev@gmail.com', ['atp12112@gmail.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return render(request,"index.html",{})
