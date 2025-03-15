from django.urls import path
from heartrate import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", view=views.index, name="index"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path('list/', view=views.get_list, name='list'),
    path('add/', view=views.add_rate, name='add-rate'),
]
