from django.shortcuts import render, redirect

#from .models import Contact

from django.core.mail import EmailMessage

# Create your views here.


def index(request):
    if request.method == "POST":
        contact = Contact(full_name=request.POST.get('form-name'),
                          phone_number=request.POST.get('form-phone-number'),
                          your_email=request.POST.get('form-email'),
                          subject=request.POST.get('form-subject'),
                          message=request.POST.get('form-message')
                          )
        email = EmailMessage(
            request.POST.get('form-subject'), request.POST.get('form-message'), to=['its7080.am@gmail.com'])
        email.send()

        contact.save()
        return redirect('/thankyou/')

    context = {}
    return render(request, "index.html", context)