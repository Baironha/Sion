from django.urls import path
from .views import *


urlpatterns =[
    path('proveedor/', proveedor_ListCreateView.as_view(), name= 'proveedor_crear_ver'),
    path('proveedor/<int:pk>/', proveedor_DetailView.as_view(), name= 'proveedor_actualizar_eliminar'),
    
    
    path('productos/ver/', productos_ListApiView.as_view(), name= 'productos_ver'),
    path('productos/crear/', productos_ListCreateView.as_view(), name= 'productos_crear_ver'),
    path('productos/<int:pk>/', productos_DetailView.as_view(), name= 'productos_actualizar_eliminar'),
    
    
    path('disponibilidad/ver/', disponibilidad_ListApiView.as_view(), name= 'disponibilidad_ver'),
    path('disponibilidad/Crear/', disponibilidad_ListCreateView.as_view(), name= 'disponibilidad_crear_ver'),
    path('disponibilidad/<int:pk>/',disponibilidad_DetailView.as_view(), name= 'disponibilidad_actualizar_eliminar'),
    
    
    path('estado_producto/', estado_producto_ListCreateView.as_view(), name= 'estado_producto_crear_ver'),
    path('estado_producto/<int:pk>/', estado_producto_DetailView.as_view(), name= 'estado_producto_eliminar'),
    
    
    path('stock_productos/', stock_productos_ListCreateView.as_view(), name= 'stock_productos_crear_ver'),
    path('stock_productos/<int:pk>/', stock_productos_DetailView.as_view(), name= 'stock_productos_eliminar'),
    
    
    path('usuarios/crear/', usuarios_CreateAPIView.as_view(), name= 'usuarios_crear'),
    path('usuarios/crear/ver/', usuarios_ListCreateView.as_view(), name= 'usuarios_crear_ver'),
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
    
    
    path('montoenvio/ver/', montoenvio_ListApiView.as_view(), name= 'montoenvio_ver'),
    path('montoenvio/crear/', montoenvio_ListCreateView.as_view(), name= 'montoenvio_crear_ver'),
    path('montoenvio/<int:pk>/', montoenvio_DetailView.as_view(), name= 'montoenvio_actualizar_eliminar'),
    
    
    path(' Descuento/ver/', Descuento_ListApiView.as_view(), name= ' Descuento_ver'),
    path(' Descuento/crear/', Descuento_ListCreateView.as_view(), name= ' Descuento_crear_ver'),
    path(' Descuento/<int:pk>/', Descuento_DetailView.as_view(), name= ' Descuento_actualizar_eliminar'),
    
    
    path('carrito/', carrito_ListCreateView.as_view(), name= 'carrito_crear'),
    path('carrito/<int:pk>/', carrito_DetailView.as_view(), name= 'carrito_actualizar_eliminar'),
    
    
    path('carritoItem/', carritoItem_ListCreateView.as_view(), name= 'carritoItem_crear'),
    path('carritoItem/<int:pk>/', carritoItem_DetailView.as_view(), name= 'carritoItem_actualizar_eliminar'),
    
    
    path('ventas/', ventas_ListCreateView.as_view(), name= 'ventas_crear'),
    path('ventas/<int:pk>/', ventas_DetailView.as_view(), name= 'ventas_actualizar_eliminar'),
    
    
    #urls intermediias
    
    path('ProveedoresXProducto/', ProveedoresXProducto_ListCreateView.as_view(), name= 'productos_x_ventas_crear'),
    path('productos_x_ventas/<int:pk>/', ProveedoresXProducto_DetailView.as_view(), name= 'ProveedoresXProducto_actualizar_eliminar'),
    
    
    path('productos_x_ventas/', productos_x_ventas_ListCreateView.as_view(), name= 'productos_x_ventas_crear'),
    path('productos_x_ventas/<int:pk>/', productos_x_ventas_DetailView.as_view(), name= 'productos_x_ventas_actualizar_eliminar'),
    
    path('rol_x_administradores/', rol_x_administradores_ListCreateView.as_view(), name= 'rol_x_administradores_crear'),
    path('rol_x_administradores/<int:pk>/', rol_x_administradores_DetailView.as_view(), name= 'rol_x_administradores_actualizar_eliminar'),
    
    path('rol_x_empleado/', rol_x_empleado_ListCreateView.as_view(), name= 'rol_x_empleado_crear'),
    path('rol_x_empleado/<int:pk>/', rol_x_empleado_DetailView.as_view(), name= 'rol_x_empleado_actualizar_eliminar'),
]
