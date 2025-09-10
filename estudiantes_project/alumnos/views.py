from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    
    # Paginación
    paginator = Paginator(alumnos, 10)  # 10 alumnos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_alumnos': alumnos.count()
    }
    return render(request, 'alumnos/lista.html', context)

def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Alumno registrado exitosamente!')
            return redirect('lista_alumnos')
        else:
            messages.error(request, 'Error en el formulario. Revise los datos.')
    else:
        form = AlumnoForm()
    
    return render(request, 'alumnos/registro.html', {'form': form})

def inicio(request):
    total_alumnos = Alumno.objects.count()
    ultimos_alumnos = Alumno.objects.all()[:5]
    
    context = {
        'total_alumnos': total_alumnos,
        'ultimos_alumnos': ultimos_alumnos
    }
    return render(request, 'alumnos/inicio.html', context)