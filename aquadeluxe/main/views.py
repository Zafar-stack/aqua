from django.shortcuts import render
from main.models import *


# Create your views here.


def indexHandler(request):
    if not request.session.session_key:
        request.session.create()

    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'checkout':
            zayavki = Podpischiki.objects.filter(session_id=request.session.session_key).filter(status=0)
            if zayavki:
                new_z = zayavki[0]
                new_z.city = request.POST.get('user_city', '')
                new_z.person = request.POST.get('user_name', '')
                new_z.phone = request.POST.get('user_phone', '')

                new_z.save()


    return render(request, 'index.html', {})


def thanksHandler(request):

    return render(request, 'thank-you.html', {})
