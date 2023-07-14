from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('EMAIL DESDE DJANGO', # Asunto
              'Probando envio de email desde DJANGO, hola :D', # Contenido del mensaje
              'sjbalonzo201c@gmail.com', # Remitente
              ['jgordillome@unsa.edu.pe'], # Destinario
              fail_silently=False)
    return render(request, 'send/index.html')

