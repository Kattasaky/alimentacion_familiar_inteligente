from django.db import models

#las clases representan las tablas de la base de datos, 
# cada clase es una tabla y cada atributo es una columna.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    condicion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    TIPO_CHOICES = [
        ('proteina', 'Proteína'),
        ('carbohidrato', 'Carbohidrato'),
        ('grasa', 'Grasa'),
        ('verdura', 'Verdura'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre


class Preferencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    acepta = models.BooleanField()

    def __str__(self):
        return f"{self.persona} - {self.alimento} - {self.acepta}"


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=50)  # ejemplo: "1 taza"

    def __str__(self):
        return f"{self.plato} - {self.alimento}"


class MenuSemanal(models.Model):
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"Semana de {self.fecha_inicio}"


class DiaMenu(models.Model):
    menu = models.ForeignKey(MenuSemanal, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10)  # lunes, martes...
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia} - {self.plato}"