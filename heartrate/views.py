from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

from heartrate.forms import HeartRateForm
from heartrate.models import HeartRate, User


# Create your views here.
@login_required(login_url="login/")
def index(request: HttpRequest) -> HttpResponse:

    context = {'form': HeartRateForm()}
    return render(request, 'index.html', context)


def add_rate(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = HeartRateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            systolic = int(data['systolic'])
            diastolic = int(data['diastolic'])
            pulse = int(data['pulse'])
            obj = HeartRate(
                systolic=systolic,
                diastolic=diastolic,
                pulse=pulse,
                measured_in=timezone.now(),
                user=User.objects.get(username=request.user)
            )
            obj.save()
            context = {'heartrate': obj, 'form': HeartRateForm()}
            return render(request, 'heartrate/heartrate.html', context)
        else:
            context = {
                'form': form,
            }
        return render(request, 'heartrate/form.html', context)


def get_list(request: HttpRequest) -> HttpResponse:
    heartrates = HeartRate.objects.filter(user=request.user)
    print(heartrates)
    context = {
        'heartrates': heartrates
    }
    return render(request, template_name="heartrate/list.html", context=context)
