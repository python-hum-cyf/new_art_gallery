# Wymagania do projektu końcowego:

1. Podobny do niniejszego, który można wykorzystać jako wzór - tylko o innej tematyce!
2. Co najmniej dwie Django appki, każda z co najmniej jednym własnym modelem i co najmniej klucz obcy do modelu z innej appki.
4. Widoki listujące instancje modeli w poszczególnych appkach.
5. Opcjonalnie: Jedna akcja admina, może być podobna jak tu.
6. Opcjonalnie: widok pokazujący jedną konkretną instancję modelu.

# na windowsie zamiast ./manage.py:
```shell
python .\.manage.py [KOMENDA]
```
### Trzeba byc w odpowiednim folderze
## Setup
- enter venv
- pip install django (in venv)
- django-admin startproject new_project
## Apps
- ./manage.py startapp APP
- ./manage.py runserver
- add app to INSTALLED_APPS in PROJECT/settings.py
## Models
```python
# APP/models.py
class SomeModel(models.Model):
    name = models.CharField(null=False) # prevents from empty name fields
    def __str__(self):
        return self.name
```
```python
# APP/admin.py
from django.contrib import admin
from .models import SomeModel
# Register your models here.
admin.site.register(SomeModel)
```
### migrations
- ./manage.py makemigrations
- ./manage.py migrate
## Superuser
- ./manage.py createsuperuser
## Server
### Initialize
- ./manage.py runserver
### Address
localhost:8000/admin
# ORM
Pythonowska linia komend do zarządzania zawartością
- ./manage.py shell
# Views
```python
# APP/views.py
class PainterDetailView(DetailView):
    model = Painter
    template_name = 'painters_details.html'
    context_object_name = 'painter'
```

```html
<!-- należy utworzyć APP/templates/painter_details.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{painter.name}}</title>
</head>
<body>
    <h2>Period: {{painter.period}}</h2>
    <h2>Year of birth: {{painter.year_of_birth}}</h2>
    <h2>Year of death: {{painter.year_of_death}}</h2>
</body>
</html>
```
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('painters.list/', PaintersListView.as_view(), name='painters_list'),
    path('painer_details/<int:pk>', PainterDetailView.as_view(),) # <int:pk> wkłada id do URL - pk == Primary Key
]
```
