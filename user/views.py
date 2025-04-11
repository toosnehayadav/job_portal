from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from . import forms
from django.db.models import Q
from django.contrib import messages
from .models import UserProfile,AppliedJob
from django.utils.decorators import method_decorator
from .middleware  import checkingUserAuthentication
from adminjob.models import Job
# Create your views here.
class newUser(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth == False:
            form = forms.RegistrationForm()
            return render(request, 'user/newUser.html', {'form': form})
        else:
            return redirect('/')
    def  post(self,request):
        if request.method == 'POST':
            print(request)
            form = forms.RegistrationForm(request.POST, request.FILES)  # Including request.FILES for image upload
            if form.is_valid():
                form.save()  # Save the form data to the database
                request.session['email'] = request.POST["email"] 
                request.session['name'] = request.POST['full_name']
                return redirect('/')
            else:
                return render(request, 'user/newUser.html', {'form': form})



class login(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth == False:
            return render(request,'user/login.html')
        else:
            return redirect('/')
    
    
    def post(self,request):
        email  =  request.POST['email']
        password = request.POST["password"]

        isUser =  UserProfile.objects.filter(Q(email = email) & Q(password = password))
        
        if(len(isUser)==1):
            userinfo = UserProfile.objects.get(Q(email = email))
            request.session['email'] = email 
            request.session['name'] = userinfo.full_name
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/user/login')

        
class logout(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            del request.session['name']
            del request.session['email']
   
        
        return HttpResponseRedirect('/')
    

class UserProfiles(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            user= UserProfile.objects.get(email=request.email)
            jobs = AppliedJob.objects.filter(user = user.id)
            print(jobs,"is applid")
            return render(request,"user/userprofile.html",{"user":user,"job" :jobs})
        else:
            return HttpResponseRedirect('/')
        

class applyJob(View):
    def get(self,request,id):
        if request.isauth:
            isapplied = AppliedJob.objects.filter(job=id).exists();
            if isapplied:
                messages.info(request,'You have already applied for this job');
            else:
                users  = UserProfile.objects.get(email=request.email)
                jobs = Job.objects.get(id=id)
                AppliedJob.objects.create(user = users ,job = jobs)
                messages.info(request,'job applied successfully!!');
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


class deleteAppliedJOB(View):
    def get(self,request,id):
        isapplied = AppliedJob.objects.filter(id=id).exists()
        if isapplied:
            AppliedJob.objects.get(id=id).delete()
            return HttpResponseRedirect('/user/profile/')

        else:
            return HttpResponseRedirect('/user/profile/')
        
class jobDetail(View):
    def get(self,request,id):
        isjob = Job.objects.filter(id=id).exists()
        if isjob:
            job=Job.objects.get(id=id)
            return render(request,"user/jobdetails.html",{"job":job})

        else:
            return HttpResponseRedirect('/user/profile/')
