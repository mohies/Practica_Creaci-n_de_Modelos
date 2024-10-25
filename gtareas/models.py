from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.TextField(unique=True)
    contraseña = models.TextField()  
    fecha_registro = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADOS = [('Pen','Pendiente'), ('Prog','Progreso'), ('Com','Completada')]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS,default="Pendiente")
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario=models.ManyToManyField(Usuario,related_name="usuario",through='AsignacionTarea')
    
    def __str__(self):
        return self.titulo


class Proyecto(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    tareas = models.ManyToManyField(Tarea, related_name='proyectos')  
    def __str__(self):
        return self.nombre
    
    
class Etiqueta(models.Model):
    nombre = models.TextField(max_length=200, unique=True)
    tareas = models.ManyToManyField(Tarea, related_name='tareas_asociadas')
    def __str__(self):
        return self.nombre
    
class AsignacionTarea(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(blank=True,null=True)
    
class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    contenido=models.TextField()
    fecha_contenido=models.DateTimeField(blank=True,null=True)
    