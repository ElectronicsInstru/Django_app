from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = 'member_home'), # HOMEPAGE de todos los miembros 
    path('<int:id>/', views.member, name='member_info') # Pagina de miembro individual
]
