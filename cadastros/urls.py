from django.urls import path
from .views import CampoCreaete, RobosCreate
from .views import CampoUpdate, RobosUpdate
from .views import CampoDelete, RobosDelete
from .views import CampoList, RobosList


urlpatterns = [
    path('cadastrar/campo', CampoCreaete.as_view(), name="cadastrar-campo"),
    path('cadastrar/robos', RobosCreate.as_view(), name="cadastrar-robos"),
    
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/robos/<int:pk>/', RobosUpdate.as_view(), name="editar-robos"),
    
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/robos/<int:pk>/', RobosDelete.as_view(), name="excluir-robos"),
    
    path('listar/campo/<int:pk>/', CampoList.as_view(), name="listar-campo"),
    path('listar/robos/<int:pk>/', RobosList.as_view(), name="listar-robos"),
]
