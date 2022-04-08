"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from charity import views as charity_views
from trustfund import views as trustfund_views
from volunteer import views as volunteer_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', charity_views.home_page_view),

    path('donations_list/', charity_views.donations_list_view),
    path('donations_list/<int:charity_pk>/', charity_views.donation_view),
    path('volunteering_list/', charity_views.volunteering_list_view),
    path('volunteering_list/<int:charity_pk>/', charity_views.volunteering_view),

    path('donations_list/<int:charity_pk>/donate/', volunteer_views.donate_view),
    path('success_donation/<str:order_data>/', volunteer_views.success_donation_view),
    path('failure_donation/<str:order_data>/', volunteer_views.failure_donation_view),
    path('volunteering_list/<int:charity_pk>/to_be_volunteer/', volunteer_views.to_be_volunteer_view),

    path('authorization/', include('django.contrib.auth.urls')),
    path('authorization/sign-up/', charity_views.SignUpView.as_view(), name="sign-up"),
    path('profile/', charity_views.profile_page_view),

    path('trustfund_profile/', trustfund_views.profile_page_view),
    path('trustfund_profile/charity/<int:charity_pk>/', trustfund_views.charity_view),
    path('trustfund_profile/add_charity/', trustfund_views.add_charity_view),
    path('trustfund_profile/charity/<int:charity_pk>/remove_charity/', trustfund_views.remove_charity_view),
    path('trustfund_profile/charity/<int:charity_pk>/edit_charity/', trustfund_views.edit_charity_view),

    path('volunteer_profile/', volunteer_views.profile_page_view)
]
