from django.shortcuts import render,redirect

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

def cases(req):
    return render(req,'web/case.html')

def casesdetail(req,case_name):
    if(req.method == 'GET'):
        if case_name =='1':
            return render(req,'web/casedetail/case_ljfg.html')
        elif case_name =='2':
            return render(req,'web/casedetail/case_ghls.html')
        elif case_name =='3':
            return render(req,'web/casedetail/case_dhfs.html')
        elif case_name =='4':
            return render(req,'web/casedetail/case_djw.html')
        else:
            return redirect('/')

def projectsdetail(req,project_name):
    if(req.method == 'GET'):
        if project_name =='1':
            return render(req,'web/projects/projects_gd.html')
        elif project_name =='2':
            return render(req,'web/projects/projects_st.html')
        elif project_name =='3':
            return render(req,'web/projects/projects_wx.html')
        else:
            return redirect('/')
