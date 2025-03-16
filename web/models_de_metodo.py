from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(null=True)
    contacto = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=13)
    telefono2 = models.CharField(max_length=13)
    email = models.EmailField(null=True)
    plazo_credito = models.SmallIntegerField(default=0)
    comentarios = models.TextField(null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.RESTRICT)
    sku = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    rfc = models.CharField(max_length=13)
    sexo = models.CharField(max_length=1,default="M")
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField(null=True)  # direccion fiscal
    codigo_postal = models.CharField(max_length=5,default="00000")  #cp fiscal
    ciudad = models.CharField(max_length=100, null=True)       #ciudad fiscal
    direccion_entrega = models.TextField(null=True)
    codigo_postal_entrega = models.CharField(max_length=5,default="00000")
    ciudad_entrega = models.CharField(max_length=100, null=True)
    campo_libre = models.CharField(max_length=50, null=True)
    comentarios = models.TextField(null=True)

    def __str__(self):
        return self.rfc

class Pedido(models.Model):
    
    ESTADO_CHOICES = (
        ('0','Solicitado'),
        ('1','Pagado')
    )

    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)   # ForeingKey - relacion de muchos a uno
    fecha_registro = models.DateTimeField(auto_now_add=True)
    numero_pedido = models.CharField(max_length=20,null=True)
    monto_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado = models.CharField(max_length=1,default='0',choices=ESTADO_CHOICES)   # CON Esto, solo permite 0 o 1

    def __str__(self):
        return self.numero_pedido

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(delf):
        return self.producto.nombre
