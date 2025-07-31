from django.urls import path
from .views import *


urlpatterns =[

    path('productos/', productos_ListApiView.as_view(), name= 'productos_ver'),
    path('productos/', productos_ListCreateView.as_view(), name= 'productos_crear_ver'),
    path('productos/<int:pk>/', productos_DetailView.as_view(), name= 'productos_actualizar_eliminar'),
    
    
    path('usuarios/', usuarios_CreateAPIView.as_view(), name= 'usuarios_crear'),
    path('usuarios/<int:pk>/', usuarios_DetailView.as_view(), name= 'usuarios_actualizar_eliminar'),

    path('empleados/', empleados_ListCreateView.as_view(), name= 'empleados_crear'),
    path('empleados/<int:pk>/', empleados_DetailView.as_view(), name= 'empleados_actualizar_eliminar'),

    path('admins/', admins_ListCreateView.as_view(), name= 'admins_crear'),
    path('admins/<int:pk>/', admins_DetailView.as_view(), name= 'admins_actualizar_eliminar'),
    
    path('rol_admins/', rol_administradores_ListCreateView.as_view(), name= 'rol_admins_crear'),
    path('rol_admins/<int:pk>/', rol_administradores_DetailView.as_view(), name= 'rol_admins_actualizar_eliminar'),
    
    path('rol_empleados/', rol_empleados_ListCreateView.as_view(), name= 'rol_empleados_crear'),
    path('rol_empleados/<int:pk>/', rol_empleados_DetailView.as_view(), name= 'rol_empleados_actualizar_eliminar'),
    
    path('metodos_pago/', metodo_de_pago_ListCreateView.as_view(), name= 'metodos_pago_crear'),
    path('metodos_pago/<int:pk>/', metodo_de_pago_DetailView.as_view(), name= 'metodos_pago_actualizar_eliminar'),
    
    path('rol_empleados/', rol_empleados_ListCreateView.as_view(), name= 'rol_empleados_crear'),
    path('rol_empleados/<int:pk>/', rol_empleados_DetailView.as_view(), name= 'rol_empleados_actualizar_eliminar'),
    
    path('ventas/', ventas_ListCreateView.as_view(), name= 'ventas_crear'),
    path('ventas/<int:pk>/', ventas_DetailView.as_view(), name= 'ventas_actualizar_eliminar'),
    
    
    #urls intermediias
    path('usuarios_x_ventas/', usuarios_x_ventas_ListCreateView.as_view(), name= 'usuarios_x_ventas_crear'),
    path('usuarios_x_ventas/<int:pk>/', usuarios_x_ventas_DetailView.as_view(), name= 'usuarios_x_ventas_actualizar_eliminar'),
    
    path('productos_x_ventas/', productos_x_ventas_ListCreateView.as_view(), name= 'productos_x_ventas_crear'),
    path('productos_x_ventas/<int:pk>/', productos_x_ventas_DetailView.as_view(), name= 'productos_x_ventas_actualizar_eliminar'),
    
    path('rol_x_administradores/', rol_x_administradores_ListCreateView.as_view(), name= 'rol_x_administradores_crear'),
    path('rol_x_administradores/<int:pk>/', rol_x_administradores_DetailView.as_view(), name= 'rol_x_administradores_actualizar_eliminar'),
    
    path('rol_x_empleado/', rol_x_empleado_ListCreateView.as_view(), name= 'rol_x_empleado_crear'),
    path('rol_x_empleado/<int:pk>/', rol_x_empleado_DetailView.as_view(), name= 'rol_x_empleado_actualizar_eliminar'),
]
