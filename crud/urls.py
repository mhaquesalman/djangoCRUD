from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('create_data/', views.create_data, name='create_data'),
    path('view_data/', views.view_data, name='view_data'),
    path('update_data/<int:id>/', views.update_data, name='update_data'),
    path('edit_data/<int:id>/', views.edit_data, name='edit_data'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
    
]
