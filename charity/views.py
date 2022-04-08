from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect


def home_page_view(request):
    return HttpResponse("Home Page")


def donations_list_view(request):
    return HttpResponse("Donations List View")


def donation_view(request, charity_pk):
    return HttpResponse("Donation View")


def volunteering_list_view(request):
    return HttpResponse("Volunteering List View")


def volunteering_view(request, charity_pk):
    return HttpResponse("Volunteering View")


def profile_page_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "trustfund"):  # request.user.trustfund
            return redirect('/trustfund_profile/')
        return redirect('/volunteer_profile/')
    return redirect('/authorization/login/')


class SignUpView(CreateView):  # Class Based View
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # == redirect login
    template_name = "registration/signup.html"
