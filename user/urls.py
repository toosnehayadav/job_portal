
from django.urls import path 
from . import views 


urlpatterns = [

    path('new-user/',views.newUser.as_view()),
        path('login/',views.login.as_view()),
        path('logout/',views.logout.as_view()),
        path('profile/',views.UserProfiles.as_view()),
        path('apply/<int:id>/',views.applyJob.as_view()),
        path('delete/job/<int:id>',views.deleteAppliedJOB.as_view(),name="deleteJOb"),
          path('detail/job/<int:id>',views.jobDetail.as_view(),name="jobdetail")

]
