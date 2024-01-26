from django.urls import path

from . import views

from .views import InfoView

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.new_view, name='new-view'),

    path('cartaportes/', views.CartaporteListView.as_view(), name='cartaportes'),
    path('cartaporte/<pk>', views.CartaporteDetailView.as_view(), name='cartaporte-detail'),

    path('empresas/', views.EmpresaListView.as_view(), name='empresas'),
    path('empresa/<pk>', views.EmpresaDetailView.as_view(), name='empresa-detail'),

    path('conductors/', views.ConductorListView.as_view(), name='conductors'),
    path('conductor/<pk>', views.ConductorDetailView.as_view(), name='conductor-detail'),

    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculos'),
    path('vehiculo/<pk>', views.VehiculoDetailView.as_view(), name='vehiculo-detail'),

    path('manifiestos/', views.ManifiestoListView.as_view(), name='manifiestos'),
    path('manifiesto/<pk>', views.ManifiestoDetailView.as_view(), name='manifiesto-detail'),

    path('empresa/create/', views.EmpresaCreate.as_view(), name='empresa-create'),
    path('empresa/<pk>/update/', views.EmpresaUpdate.as_view(), name='empresa-update'),
    path('empresa/<pk>/delete/', views.EmpresaDelete.as_view(), name='empresa-delete'),

    path('vehiculo/create/', views.VehiculoCreate.as_view(), name='vehiculo-create'),
    path('vehiculo/<pk>/update/', views.VehiculoUpdate.as_view(), name='vehiculo-update'),
    path('vehiculo/<pk>/delete/', views.VehiculoDelete.as_view(), name='vehiculo-delete'),

    path('conductor/create/', views.ConductorCreate.as_view(), name='conductor-create'),
    path('conductor/<pk>/update/', views.ConductorUpdate.as_view(), name='conductor-update'),
    path('conductor/<pk>/delete/', views.ConductorDelete.as_view(), name='conductor-delete'),

    path('cartaporte/create/', views.CartaporteCreate.as_view(), name='cartaporte-create'),
    path('cartaporte/<pk>/update/', views.CartaporteUpdate.as_view(), name='cartaporte-update'),
    path('cartaporte/<pk>/delete/', views.CartaporteDelete.as_view(), name='cartaporte-delete'),

    path(' manifiesto/create/', views.ManifiestoCreate.as_view(), name='manifiesto-create'),
    path(' manifiesto/<pk>/update/', views.ManifiestoUpdate.as_view(), name='manifiesto-update'),
    path(' manifiesto/<pk>/delete/', views.ManifiestoDelete.as_view(), name='manifiesto-delete'),

    path('info/', InfoView.as_view(), name='info_view'),
]

