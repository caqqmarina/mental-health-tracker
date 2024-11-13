from django.urls import path
from authentication.views import login, register  # add "register" to this line

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]