from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'web/index.html')

def jobs(req):
    return render(req,'web/jobs.html')

def contact(req):
    return render(req,'web/contact.html')

def about(req):
    return render(req,'web/about.html')

def projects(req):
    return render(req,'web/projects.html')

def cases(req,case_name="aa"):
    return render(req,'web/case.html')