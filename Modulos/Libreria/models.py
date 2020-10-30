from django.db import models

# Create your models here.
class Root(models.Model):
    idRoot = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)


class Usuario(models.Model):
    DNI = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fechaDeNacimiento = models.DateField()
    lugarDeNacimiento = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)
    temasLiterarios = models.CharField(max_length=100)
    adm = models.BooleanField(default=False)
    noticias = models.BooleanField(default=False)

    def __str__(self):
        tipo = 'Admin' if self.adm else 'Cliente'
        noticias = 'Subscrito' if self.noticias else 'No subscrito'
        txt = '{}: ({}) {}, {}'
        return txt.format(tipo, self.DNI, self.correoElectronico, noticias)


class TarjetaDeCredito(models.Model):
    idTarjeta = models.AutoField(primary_key=True)
    debito = models.BooleanField(default=False)
    numeroTarjeta = models.CharField(max_length=100)
    saldo = models.FloatField(default=0)
    DNI = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        tipo = 'Debito' if self.debito else 'Credito'
        txt = '{} - {}: No: {} de {} ({})  con ${} '
        return txt.format(self.idTarjeta, tipo, self.numeroTarjeta, self.DNI.nombres, self.DNI.DNI, self.saldo)


class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    nombreAutor = models.CharField(max_length=100)

    def __str__(self):
        txt = '{} - {}'
        return txt.format(self.idAutor, self.nombreAutor)


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


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaDeReserva = models.DateTimeField(auto_now_add=True)
    DNI = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)


class Ejemplar(models.Model):
    idEjemplar = models.AutoField(primary_key=True)
    estado = models.IntegerField()
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    idCompra = models.ForeignKey(Compra, null=True, on_delete=models.SET_NULL)
    idReserva = models.ForeignKey(Reserva, null=True, on_delete=models.SET_NULL)


class Noticia(models.Model):
    idNoticia = models.AutoField(primary_key=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)


class Retirado(models.Model):
    idRetirado = models.AutoField(primary_key=True)
    fechaDeRetiro = models.DateTimeField(auto_now_add=True)
    ISSN = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
