from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


@login_required
def logout(request):
    auth.logout(request)
    return redirect('account:login')


@login_required
def get_name(request):
    user = request.user.username
    return JsonResponse({
        "user": user
    })
