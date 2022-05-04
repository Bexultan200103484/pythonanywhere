from django.shortcuts import render, redirect
from .models import*
from .forms import CreateUser
# Create your views here.
def createuser(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('create_user')
            except:
                form.add_error(None, 'Failed attempt to create user')
    else:
        form = CreateUser()
    return render(request, 'posts/registration.html', {'form': form})