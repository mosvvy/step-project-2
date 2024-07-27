from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'register.html', {'form': form})