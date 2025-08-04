from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator


class proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100, null=False)
    contacto       = models.CharField(max_length=100, null=False)
    telefono       = models.CharField(max_length=20, null=False)
    correo         = models.EmailField(max_length=100, null=False)
    direccion      = models.CharField(max_length=200, null=True, blank=True)
    pais           = models.CharField(max_length=50, null=True, blank=True)
    descripcion    = models.TextField(null=True, blank=True)  
    activo         = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_empresa} - {self.contacto}"


class productos(models.Model):
    nombre              = models.CharField(max_length=100, null=False)
    codigo_producto     = models.CharField(max_length=100, blank=True)
    precio              = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    marca               = models.CharField(max_length=100, null=False)
    Descripcion_product = models.CharField(max_length=300, blank=True)
    peso                = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    proveedores         = models.ManyToManyField( 'Proveedor', through='ProveedoresXProducto', related_name='productos' )
    def __str__(self):
        return self.nombre


class disponibilidad(models.Model):
    id_producto    = models.ForeignKey(productos, on_delete = models.CASCADE, related_name='disponibilidad_producto')
    disponible = [
        ('Disponible', 'Disponible'),
        ('Agotado', 'Agotado'),
    ]
    disponibilidad = models.CharField(max_length=10, choices=disponible, default='Disponible', null=False)
    cantidad       = models.IntegerField(null=False)


class estado_producto (models.Model):
    estado_producto = [
        ('Bueno', 'Bueno'),
        ('Dañado', 'Dañado'),
    ]
    estado      = models.CharField(max_length=10,choices=estado_producto,default='Bueno',)
    def __str__(self):
        return self.estado
    descripcion = models.CharField(max_length=300, null=False)


class stock_productos(models.Model):
    id_producto        = models.ForeignKey(productos, on_delete = models.CASCADE, related_name='stock_productos')
    id_disponibilidad  = models.ForeignKey(disponibilidad, on_delete = models.CASCADE, related_name='stock_disponibilidad')
    id_estado_producto = models.ForeignKey(estado_producto, on_delete = models.CASCADE, related_name='stock_estado')


class rol_administradores (models.Model):
    nombre_rol      = models.CharField( max_length=50, null=False)


class admins(models.Model):
    rol      = models.CharField(max_length=10, null=False)
    nombre   = models.CharField(max_length=50, null=False)
    correo   = models.EmailField(max_length=60, null=False)
    telefono = models.CharField(max_length=20,null=False,validators=[RegexValidator(regex=r'^\+?[\d\s\-\(\)]+$', message='Solo se permiten números, espacios, y los símbolos + - ( )')])



class rol_empleados (models.Model):
    nombre_rol = models.CharField( max_length=50, null=False)


class empleados(models.Model):
    nombre    = models.CharField(max_length=100, null=False)
    correo    = models.EmailField(max_length=60, null=False)
    rol       = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=500, null=False)


class usuarios(models.Model):
    Nombre     = models.CharField(max_length=100,  null=False)
    edad       = models.IntegerField(null=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
    direccion  = models.CharField(max_length=100, null=False)
    correo     = models.EmailField(max_length=300,null=False)
    telefono   = models.CharField(max_length=20,null=False,validators=[RegexValidator(regex=r'^\+?[\d\s\-\(\)]+$', message='Solo se permiten números, espacios, y los símbolos + - ( )')])



class metodo_de_pago(models.Model):
    tipo_de_pago = models.CharField(max_length=100, null=False)


class montoenvio(models.Model):
    REGION_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Latinoamérica', 'Latinoamérica'),
        ('Internacional', 'Internacional'),
    ]

    region          = models.CharField(max_length=20, choices=REGION_CHOICES, null=False)
    costo_por_libra = models.DecimalField(max_digits=10, decimal_places=2, null=False)  # ₡ o $

    def __str__(self):
        return f"{self.region} - ₡/{'$'}{self.costo_por_libra} por libra"



class Descuento(models.Model):
    producto   = models.ForeignKey(productos, on_delete=models.CASCADE)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.producto.nombre} - {self.porcentaje}%"


class carrito(models.Model):
    usuario        = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='carrito')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    monto_envio    = models.ForeignKey(montoenvio, on_delete=models.SET_NULL, null=True, blank=True, related_name='carritos')

    def peso_total(self):
        return sum([item.get_peso_total() for item in self.items.all()])

    def subtotal(self):
        return sum([item.subtotal() for item in self.items.all()])

    def descuento_total(self):
        return sum([(item.producto.precio * item.cantidad) - item.subtotal() for item in self.items.all()])

    def impuestos(self, porcentaje=13):  # Por defecto 13%
        return self.subtotal() * (porcentaje / 100)

    def costo_envio(self):
        if self.monto_envio:
            return self.peso_total() * self.monto_envio.costo_por_libra
        return 0

    def monto_total(self):
        return self.subtotal() - self.descuento_total() + self.impuestos() + self.costo_envio()

    def __str__(self):
        return f"Carrito de {self.usuario.nombre}"


class carritoItem(models.Model):
    carrito  = models.ForeignKey(carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(productos, on_delete=models.CASCADE, related_name='productos')
    cantidad = models.PositiveIntegerField(default=1)

    def get_descuento(self):
        try:
            descuento = Descuento.objects.get(producto=self.producto)
            return descuento.porcentaje
        except Descuento.DoesNotExist:
            return 0

    def get_precio_unitario_con_descuento(self):
        descuento = self.get_descuento()
        return self.producto.precio * (1 - (descuento / 100))

    def subtotal(self):
        return self.get_precio_unitario_con_descuento() * self.cantidad

    def get_peso_total(self):
        return self.producto.peso * self.cantidad  # Asegúrate de que el modelo `productos` tenga el campo `peso`

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"



class ventas(models.Model):
    usuario         = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='ventas_usuario')
    productos       = models.ManyToManyField(productos, through='productos_x_ventas', related_name='ventas_productos')
    fecha_registro  = models.DateField(null=False)
    empleado        = models.ForeignKey(empleados, on_delete=models.CASCADE, related_name='ventas_empleados')
    metodo_de_pago  = models.ForeignKey(metodo_de_pago, on_delete=models.CASCADE, related_name='ventas_metodo_pago')
    subtotal        = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    descuento_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    impuestos       = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    monto_envio     = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # <- nuevo campo
    monto_total     = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_registro}"




#Tablas intermedias

class ProveedoresXProducto(models.Model):
    producto       = models.ForeignKey(productos, on_delete=models.CASCADE, related_name='proveedores_producto')
    proveedor      = models.ForeignKey(proveedor, on_delete=models.CASCADE, related_name='productos_proveedor')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.proveedor.nombre_empresa} -> {self.producto.nombre}"



class productos_x_ventas(models.Model):
    id_producto = models.ForeignKey(productos, on_delete = models.CASCADE, related_name='productos_x_ventas')
    id_ventas   = models.ForeignKey(ventas, on_delete = models.CASCADE, related_name='productos_x_ventas')
    cantidad    = models.PositiveIntegerField(null=False, default=1)
    def __str__(self):
        return f"{self.id_producto.nombre} x{self.cantidad}"


class rol_x_administradores (models.Model):
    id_administradores      = models.ForeignKey(rol_administradores, on_delete = models.CASCADE, related_name='rol_x_administradores')
    id_rol_administradores  = models.ForeignKey(admins, on_delete = models.CASCADE, related_name='rol_x_administradores')


class rol_x_empleado(models.Model):
    id_Rol      = models.ForeignKey(rol_empleados, on_delete = models.CASCADE, related_name='rol_x_empleado')
    id_Empleado = models.ForeignKey(empleados, on_delete = models.CASCADE, related_name='rol_x_empleado')