
# Proyecto Django: Clase5

Este proyecto utiliza el framework Django para implementar una aplicación web. A continuación, se documenta detalladamente la estructura del proyecto, las funcionalidades principales y los pasos para configurarlo.

---

## Estructura del Proyecto

### Raíz del Proyecto
- `manage.py`: Archivo principal para ejecutar comandos de Django.
- `db.sqlite3` y `clase5.db`: Bases de datos SQLite.

### Carpeta `clase5`
Esta carpeta contiene configuraciones globales del proyecto.
- `settings.py`: Configuración del proyecto, como bases de datos, aplicaciones instaladas y rutas estáticas.
- `urls.py`: Rutas globales.
- `asgi.py` y `wsgi.py`: Configuración para servidores.
- `static/`: Archivos estáticos como CSS y JS.

### Carpeta `mia`
Esta es una aplicación dentro del proyecto.
- **`admin.py`**: Configuración del panel de administración.
- **`apps.py`**: Configuración de la aplicación.
- **`forms.py`**: Formularios personalizados.
- **`migrations/`**: Migraciones de base de datos.
- **`models.py`**: Modelos de datos.
- **`templates/`**: Plantillas HTML.
- **`tests.py`**: Pruebas unitarias.
- **`urls.py`**: Rutas específicas de la aplicación.
- **`views.py`**: Lógica de vistas.

---

## Configuración Inicial

1. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

2. **Migrar la Base de Datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Ejecutar el Servidor**
   ```bash
   python manage.py runserver
   ```

4. **Acceder a la Aplicación**
   Visita `http://127.0.0.1:8000/` en tu navegador.

---

## Crear Formularios

Para crear formularios, utiliza el archivo `forms.py` de la aplicación `mia`. Ejemplo:

```python
from django import forms
from .models import MiModelo

class MiFormulario(forms.ModelForm):
    class Meta:
        model = MiModelo
        fields = ['campo1', 'campo2']
```

### Integración en Vistas

En el archivo `views.py`, utiliza el formulario:

```python
from django.shortcuts import render
from .forms import MiFormulario

def mi_vista(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MiFormulario()
    return render(request, 'mia/mi_template.html', {'form': form})
```

### Crear Plantillas

En `templates/mia/mi_template.html`:

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enviar</button>
</form>
```

---

## Configuración de Rutas

### Global (`clase5/urls.py`)
Incluye las rutas de la aplicación `mia`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mia.urls')),
]
```

### Específica de la Aplicación (`mia/urls.py`)
Define rutas específicas para `mia`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_vista, name='mi_vista'),
]
```

---

## Comandos Útiles

- Crear un superusuario para el panel de administración:
  ```bash
  python manage.py createsuperuser
  ```
- Ejecutar pruebas unitarias:
  ```bash
  python manage.py test
  ```
- Crear migraciones para cambios en modelos:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## Contacto

Para más información, contáctame en: [victorfernandolopez1988@gmail.com]
