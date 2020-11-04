from django.shortcuts import render

def all_blogs(request):
    return render(request, template_name='blog/all_blogs.html')
