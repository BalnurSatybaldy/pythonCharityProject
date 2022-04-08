from django.http import HttpResponse


def profile_page_view(request):
    return HttpResponse("Volunteer Profile Page")


def donate_view(request, charity_pk):
    return HttpResponse("Donate View")


def success_donation_view(request, order_data):
    return HttpResponse("Success Donation View")


def failure_donation_view(request, order_data):
    return HttpResponse("Failure Donation View")


def to_be_volunteer_view(request, charity_pk):
    return HttpResponse("To be Volunteer View")
