from django.shortcuts import render
from django.http import HttpResponse


# Main page
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Group posts
def group_posts(request, slug):
    return HttpResponse('Group posts')