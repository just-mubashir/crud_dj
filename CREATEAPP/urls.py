from django.urls import path
from . import views

urlpatterns = [
    path ('', views.add_show, name = 'addanddisplay'),
    path ('delete/<int:id>', views.delete_entry, name = 'delete_entry'),
    path ('<int:id>', views.update, name = 'update')
]
