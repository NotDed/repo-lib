from django.db import models

# Create your models here.
class Root(models.Model):
    idRoot = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)


class Usuario(models.Model):
    DNI = models.AutoField(primary_key=True)
    tipoUser = models.IntegerField()
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fechaDeNacimiento = models.DateField()
    lugarDeNacimiento = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)
    temasLiterarios = models.CharField(max_length=100)
    noticias = models.BooleanField()

    def getNombreCompleto(self):
        txt = '{1}, {2}'
        return txt.format(self.nombres, self.apellidos)


class TarjetaDeCredito(models.Model):
    idTarjeta = models.AutoField(primary_key=True)
    tipo = models.IntegerField()
    numeroTarjeta = models.CharField(max_length=100)
    saldo = models.FloatField()
    DNI = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def getSaldo(self):
        return self.saldo


class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    nombreAutor = models.CharField(max_length=100)


class Libro(models.Model):
    ISSN = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    numeroPaginas = models.IntegerField()
    editorial = models.CharField(max_length=100)
    idAutor = models.ForeignKey(Autor, null=False, blank=False, on_delete=models.CASCADE)


class Compra(models.Model):
    idCompra = models.AutoField(primary_key=True)
    fechaDeCompra = models.DateTimeField(auto_now_add=True)
    DNI = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)


class Reseva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaDeReserva = models.DateTimeField(auto_now_add=True)
    DNI = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)


class Ejemplar(models.Model):
    idEjemplar = models.AutoField(primary_key=True)
    estado = models.IntegerField()
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    idCompra = models.ForeignKey(Compra, null=True)
    idReserva = models.ForeignKey(Reserva, null=True)


class Noticia(models.Model):
    idNoticia = models.AutoField(primary_key=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)


class retirados(models.Model):
    idRetirado = models.AutoField(primary_key=True)
    fechaDeRetiro = models.DateTimeField(auto_now_add=True)
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
