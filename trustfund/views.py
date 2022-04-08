from django.http import HttpResponse


def profile_page_view(request):
    return HttpResponse("TrustFund Profile Page")


def charity_view(request, charity_pk):
    return HttpResponse("Charity View")


def add_charity_view(request):
    return HttpResponse("Add Charity View")


def remove_charity_view(request, charity_pk):
    return HttpResponse("Remove Charity View")


def edit_charity_view(request, charity_pk):
    return HttpResponse("Edit Charity View")
