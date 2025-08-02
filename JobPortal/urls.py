"""
URL configuration for JobPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_login',user_login,name="user_login"),
    path('recruiter_login',recruiter_login,name="recruiter_login"),
    path('recruiter_signup',recruiter_signup,name="recruiter_signup"),
    path('user_signup',user_signup,name="user_signup"),
    path('user_home',user_home,name="user_home"),
    path('recruiter_home',recruiter_home,name="recruiter_home"),
    path('admin_home',admin_home,name="admin_home"),
    path('Logout',Logout,name="Logout"),
    path('view_users',view_users,name="view_users"),
    path('delete_user/<int:uid>',delete_user,name="delete_user"),
    path('delete_recruiter/<int:uid>',delete_recruiter,name="delete_recruiter"),
    path('change_status/<int:uid>',change_status,name="change_status"),
    path('recruiter_pending',recruiter_pending,name="recruiter_pending"),
    path('recruiter_accepted',recruiter_accepted,name="recruiter_accepted"),
    path('recruiter_rejected',recruiter_rejected,name="recruiter_rejected"),
    path('recruiter_all',recruiter_all,name="recruiter_all"),
    path('change_password_admin',change_password_admin,name="change_password_admin"),
    path('change_password_user',change_password_user,name="change_password_user"),
    path('change_password_recruiter',change_password_recruiter,name="change_password_recruiter"),
    path('change_company_logo/<int:uid>',change_company_logo,name="change_company_logo"),
    path('add_job',add_job,name="add_job"),
    path('latest_jobs',latest_jobs,name="latest_jobs"),
    path('job_list',job_list,name="job_list"),
    path('user_latest_jobs',user_latest_jobs,name="user_latest_jobs"),
    path('edit_job_details/<int:uid>',edit_job_details,name="edit_job_details"),
    path('job_details/<int:uid>',job_details,name="job_details"),
    path('apply_for_job/<int:uid>',apply_for_job,name="apply_for_job"),
    path('applied_candidates',applied_candidates,name="applied_candidates"),
    path('contact',contact,name="contact"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
