from django.shortcuts import render
from user.middleware import checkingUserAuthentication
from django.utils.decorators import method_decorator
from django.views import View
from adminjob.models import Job

class index(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            jobs = Job.objects.all()
            print(jobs,"jobs")
            return render(request,"homepage.html",{"jobs":jobs})
        else:

            return render(request,"index.html")

    