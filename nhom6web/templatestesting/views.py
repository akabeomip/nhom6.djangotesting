from django.shortcuts import render, HttpResponse

# Create your views here.
def homePage(request):
    # return render(
    #         request,
    #         'templates/home.html',
    #     )
    return HttpResponse("Hello, world. You're at the polls index.")