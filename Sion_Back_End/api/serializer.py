


from .models        import *
from rest_framework import serializers

class productos_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = productos # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB

class disponibilidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = disponibilidad
        fields = '__all__'


class estado_producto_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = estado_producto
        fields = '__all__'



class stock_productos_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = stock_productos
        fields = '__all__'


class rol_administradores_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = rol_administradores # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class admins_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = admins # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class rol_empleados_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = rol_empleados # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class empleados_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = empleados # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class usuarios_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = usuarios # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class metodo_de_pago_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = metodo_de_pago # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB

class ventas_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = ventas # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB


class productos_x_ventas_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = productos_x_ventas # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB



class rol_x_administradores_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = rol_x_administradores # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB




class rol_x_empleado_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = rol_x_empleado # Archivos exportados
        fields = '__all__' #All se refiere a todas las columnas del DB



