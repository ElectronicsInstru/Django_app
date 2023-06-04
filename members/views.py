from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    return render(request, 'members/members.html')

def member(request, id):

    # Obtenemos la instancia del perfil utilizando el id recibido en la URL
    member_info = get_object_or_404(Profile, id=id)
    print(member_info.descripcion)
    print(member_info.nombre)

    return render(request, 'members/member_info.html', {'member_info': member_info})
