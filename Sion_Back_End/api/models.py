from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class productos(models.Model):
    nombre              = models.CharField(max_length=100, null=False )
    precio              = models.DecimalField(max_digits=10, null=False)
    marca               = models.CharField(max_length=100,null=False)
    cantidad            = models.IntegerField(max_length=100, null=False)
    Descripcion_product = models.CharField(max_length=500, blank=True)


class rol_administradores (models.Model):
    nombre_rol      = models.CharField( max_length=50, null=False)


class admins(models.Model):
    rol      = models.CharField(max_length=10, null=False)
    nombre   = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(max_length=15, null=False)
    correo   = models.CharField(max_length=60, null=False)
    rol      = models.CharField(max_length=10, null=False)


class rol_empleados (models.Model):
    nombre_rol      = models.CharField( max_length=50, null=False)


class empleados(models.Model):
    nombre    = models.CharField(max_length=100, null=False)
    correo    = models.CharField(max_length=60, null=False)
    rol       = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=500, null=False)


class usuarios(models.Model):
    Nombre     = models.CharField(max_length=100,  null=False)
    edad       = models.IntegerField(null=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
    direccion  = models.CharField(max_length=100, null=False)
    correo     = models.EmailField(max_length=300,null=False)
    telefono   = models.IntegerField(max_length=30,null=False)


class metodo_de_pago(models.Model):
    tipo_de_pago = models.CharField(max_length=100, null=False)


class ventas(models.Model):
    usuario            = models.ForeignKey(usuarios, on_delete = models.CASCADE, related_name='ventas')
    producto           = models.ForeignKey(productos, on_delete = models.CASCADE, related_name='ventas')
    fecha_registro     = models.DateField(null=False)
    usuario            = models.ForeignKey(usuarios, on_delete = models.CASCADE, related_name='ventas')
    metodo_de_pago     = models.ForeignKey(metodo_de_pago, on_delete = models.CASCADE, related_name='ventas')




#Tablas intermedias

class usuarios_x_ventas(models.Model):
    id_usuario    = models.ForeignKey(usuarios, on_delete = models.CASCADE, related_name='usuarios_x_ventas')
    id_ventas     = models.ForeignKey(ventas, on_delete = models.CASCADE, related_name='usuarios_x_ventas')

class productos_x_ventas(models.Model):
    id_producto    = models.ForeignKey(productos, on_delete = models.CASCADE, related_name='productos_x_ventas')
    id_ventas     = models.ForeignKey(ventas, on_delete = models.CASCADE, related_name='productos_x_ventas')


class rol_x_administradores (models.Model):
    id_administradores      = models.ForeignKey(rol_administradores, on_delete = models.CASCADE, related_name='rol_x_administradores')
    id_rol_administradores  = models.ForeignKey(admins, on_delete = models.CASCADE, related_name='rol_x_administradores')


class rol_x_empleado(models.Model):
    id_Rol      = models.ForeignKey(rol_empleados, on_delete = models.CASCADE, related_name='rol_x_empleado')
    id_Empleado = models.ForeignKey(empleados, on_delete = models.CASCADE, related_name='rol_x_empleado')