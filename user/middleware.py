from .models import UserProfile as users
from django.db.models import Q

class checkingUserAuthentication:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        if 'email' in request.session:
            if 'name' in request.session:
                isExist = users.objects.filter(Q(email=request.session['email'])& Q(full_name=request.session['name']))
                if len(isExist) == 1:
                    request.name = request.session['name']
                    request.email = request.session['email']
                    request.isauth = True
                else:
                    request.isauth = False
                    
            else:
                    request.isauth = False
        else:
                request.isauth = False

        
        response = self.get_response(request)

        return response