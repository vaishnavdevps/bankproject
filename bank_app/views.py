from django.shortcuts import render

# Create your views here.
from django import template
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


@csrf_exempt


def index(request):
    register = template.Library()

    @register.simple_tag
    def split_token(token):
        bits = token.split_contents()
        return bits

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        first_name = request.form['fname']
        last_name = request.form['name']
        email = request.form['email']
        message = request.form['message']
    return render(request, 'index.html')





