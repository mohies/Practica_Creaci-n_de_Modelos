from django.shortcuts import render
from .models import *
from django.db.models import Q,Count,Prefetch
from django.db.models import Avg,Max,Min
# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_proyectos(request):
    gtareas = Proyecto.objects.select_related("usuario").prefetch_related("colaboradores", Prefetch("proyecto_tareas")).all() #esta es la adecuada
    
    return render(request, 'gtareas/lista_proyectos.html', {'gtareas': gtareas})

def lista_tareas_proyecto(request, proyecto_id):
    tareas = Tarea.objects.filter(proyecto__id=proyecto_id).order_by('-fecha_creacion') 
    return render(request, 'gtareas/lista_tareas_proyecto.html', {'tareas': tareas})

def lista_usuarios_asignados(request, tarea_id):
    asignaciones = Usuario.objects.filter(asignaciontarea__tarea__id=tarea_id).order_by('asignaciontarea__fecha_asignacion')
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

def ultimo_usuario_comentario(request, proyecto_id):
    ultimo_comentario = Usuario.objects.filter(comentario__tarea__proyecto=proyecto_id).order_by('-comentario__fecha_contenido')[:1].get()
    return render(request, 'gtareas/ultimo_comentario.html', {'usuario': ultimo_comentario})

def obtener_comentarios(request, palabra, anio,tarea_id):
    comentarios = Comentario.objects.filter(
        tarea=tarea_id,
        contenido__startswith=palabra,   
        fecha_contenido__year=anio)
    return render(request, 'gtareas/lista_comentarios.html', {'comentarios': comentarios})
def obtener_etiquetas_proyecto(request, proyecto_id): #el selected related se suele poner para optimizar y tambien por si quiero acceder a todas las tareas por ejemplo que esten relaciondas
    etiqueta = Etiqueta.objects.filter(tareas__proyecto__id=proyecto_id) #porque esta en la tabla de tareas y lo otro porque esta fuera  y al no poner get se puedee usra for y luego esta el .all() y el get()
    return render(request, 'gtareas/lista_etiquetas_proyecto.html', {'etiquetas': etiqueta})
def usuarios_sin_tareas(request):
    #usuarios_libres = Usuario.objects.annotate(tareas_count=Count('tarea')).filter(tareas_count=0) #annotate lo que hace es añadir un campo nuevo
    usuarios_libres = Usuario.objects.filter(tarea=None)
    return render(request, 'gtareas/usuarios_libres.html', {'usuarios': usuarios_libres})

def mi_error_404(request, exception=None):
    return render(request, 'gtareas/errores/404.html', None,None,404)
def mi_error_400(request, exception=None):
    return render(request, 'gtareas/errores/400.html', None,None,400)
def mi_error_403(request, exception=None):
    return render(request, 'gtareas/errores/403.html', None,None,403)
def mi_error_500(request, exception=None):
    return render(request, 'gtareas/errores/403.html', None,None,500)