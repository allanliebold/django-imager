# from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def home_view(request):
    # """."""
    # # template = loader.get_template('template/imagersite/base.html')
    # # response_body = template.render()
    # return render(request, 'imager_profile/base.html')

# def home_view(request):
    # """Home view callable, for the home page."""
    # return HttpResponse("Hello World!")


def home_view(request):
    return render(request, 'imagersite/base.html')
