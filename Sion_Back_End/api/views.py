from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,ListAPIView

from .permissions import IsAdminUserGroup, IsEmpledoUserGroup, IsAuthenticated
from rest_framework.permissions import AllowAny


from .models import *
from .serializer import *
# Create your views here.



class productos_ListApiView(ListAPIView):
    permission_classes = [AllowAny]
    queryset           = productos.objects.all()
    serializer_class   = productos_Serializer


class productos_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsEmpledoUserGroup]
    queryset           = productos.objects.all()
    serializer_class   = productos_Serializer


class productos_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUserGroup]
    queryset           = productos.objects.all()
    serializer_class   = productos_Serializer


class disponibilidad_ListApiView(ListAPIView):
    permission_classes = [AllowAny]
    queryset           = stock_productos.objects.all()
    serializer_class   = stock_productos_Serializer


class disponibilidad_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsEmpledoUserGroup]
    queryset           = disponibilidad.objects.all()
    serializer_class   = disponibilidad_Serializer


class disponibilidad_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsEmpledoUserGroup]
    queryset           = disponibilidad.objects.all()
    serializer_class   = disponibilidad_Serializer


class estado_producto_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsEmpledoUserGroup]
    queryset           = estado_producto.objects.all()
    serializer_class   = estado_producto_Serializer


class estado_producto_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUserGroup]
    queryset           = estado_producto.objects.all()
    serializer_class   = estado_producto_Serializer


class stock_productos_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsEmpledoUserGroup]
    queryset           = stock_productos.objects.all()
    serializer_class   = stock_productos_Serializer


class stock_productos_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsEmpledoUserGroup]
    queryset           = stock_productos.objects.all()
    serializer_class   = stock_productos_Serializer


class usuarios_ListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset           = usuarios.objects.all()
    serializer_class   = usuarios_Serializer


class usuarios_CreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset           = usuarios.objects.all()
    serializer_class   = usuarios_Serializer



class usuarios_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUserGroup]
    queryset           = usuarios.objects.all()
    serializer_class   = usuarios_Serializer



class empleados_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = empleados.objects.all()
    serializer_class   = empleados_Serializer


class empleados_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = empleados.objects.all()
    serializer_class   = empleados_Serializer


class admins_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = admins.objects.all()
    serializer_class   = admins_Serializer


class admins_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = admins.objects.all()
    serializer_class   = admins_Serializer


class rol_administradores_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_administradores.objects.all()
    serializer_class   = rol_administradores_Serializer

class rol_administradores_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_administradores.objects.all()
    serializer_class   = rol_administradores_Serializer


class rol_empleados_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_empleados.objects.all()
    serializer_class   = rol_empleados_Serializer

class rol_empleados_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_empleados.objects.all()
    serializer_class   = rol_empleados_Serializer


class metodo_de_pago_ListCreateView(ListCreateAPIView):
    permission_classes = [IsEmpledoUserGroup, IsAuthenticated]
    queryset           = metodo_de_pago.objects.all()
    serializer_class   = rol_empleados_Serializer

class metodo_de_pago_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = metodo_de_pago.objects.all()
    serializer_class   = metodo_de_pago_Serializer


class ventas_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset           = ventas.objects.all()
    serializer_class   = ventas_Serializer

class ventas_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = ventas.objects.all()
    serializer_class   = ventas_Serializer



#Serializer intermedias


class productos_x_ventas_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset           = productos_x_ventas.objects.all()
    serializer_class   = productos_x_ventas_Serializer

class productos_x_ventas_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsEmpledoUserGroup, IsAuthenticated]
    queryset           = productos_x_ventas.objects.all()
    serializer_class   = productos_x_ventas_Serializer


class rol_x_administradores_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_x_administradores.objects.all()
    serializer_class   = rol_x_administradores_Serializer

class rol_x_administradores_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_x_administradores.objects.all()
    serializer_class   = rol_x_administradores_Serializer


class rol_x_empleado_ListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_x_empleado.objects.all()
    serializer_class   = rol_x_empleado_Serializer

class rol_x_empleado_DetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset           = rol_x_empleado.objects.all()
    serializer_class   = rol_x_empleado_Serializer

