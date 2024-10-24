from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models import Avg,Max,Min
# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_proyectos(request):
    gtareas = Proyecto.objects.all()
    return render(request, 'gtareas/lista_proyectos.html', {'gtareas': gtareas})

def lista_tareas_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.prefetch_related('tareas').get(id=proyecto_id)
    tareas = proyecto.tareas.all().order_by('-fecha_creacion')
    return render(request, 'gtareas/lista_tareas_proyecto.html', {'tareas': tareas})

def lista_usuarios_asignados(request, tarea_id):
    asignaciones = Usuario.objects.filter(asignaciontarea__tarea=tarea_id).order_by('asignaciontarea__fecha_asignacion')
    return render(request, 'gtareas/lista_usuarios_asignados.html', { 'asignaciones': asignaciones})

def lista_tareas_por_observacion(request, texto):
    asignacion = AsignacionTarea.objects.filter(observaciones__contains=texto)
    return render(request, 'gtareas/lista_tareas_por_observacion.html', {'asignaciones': asignacion})


def dame_tareas_por_anio(request, anio_inicial, anio_final):
    tareas = Tarea.objects.filter(
        fecha_creacion__year__gte=anio_inicial,
        fecha_creacion__year__lte=anio_final,
        estado='Com'
    )
    return render(request, 'gtareas/tareas_completadas.html', {"tareas_mostrar": tareas})

def ultimo_usuario_comentario(request, tarea_id):
    ultimo_comentario = Comentario.objects.filter(tarea_id=tarea_id).order_by('-fecha_contenido').first()
    usuario = ultimo_comentario.autor 
    return render(request, 'gtareas/ultimo_comentario.html', {'usuario': usuario})
