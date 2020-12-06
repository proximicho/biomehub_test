from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from bioblog.models import post, about, contact
from datetime import datetime
#https://www.w3schools.com/howto/howto_css_blog_layout.asp utilizado como base para o html e css



def index(request):
    
    latest_post_list = post.objects.order_by('-pub_date')
    contact_field = contact.objects.get(id=1).contact_text
    about_field = about.objects.get(id=1).about_text
    context = {'latest_post_list': latest_post_list,
    'contact_field':contact_field,
    'about_field':about_field


    }
    return render(request, 'bioblog/index.html',context)



def details(request,  post_type, post_name):
    
    
    
    if post_type == 'author':
        latest_post_list = post.objects.filter(author = post_name)
    elif post_type == 'organism':
        latest_post_list = post.objects.filter(organism = post_name)
    elif post_type == 'pub_date':    
        latest_post_list = post.objects.filter(pub_date__contains=post_name)
    elif post_type == 'modified_at':
        latest_post_list = post.objects.filter(modified_at__contains=post_name)
    

    contact_field = contact.objects.get(id=1).contact_text
    about_field = about.objects.get(id=1).about_text
    
    context = {'latest_post_list': latest_post_list,
    'contact_field':contact_field,
    'about_field':about_field


    }

    return render(request, 'bioblog/index.html',context)









