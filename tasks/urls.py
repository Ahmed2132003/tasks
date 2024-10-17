from django.urls import path
from . import views
from .views import login_register_view


urlpatterns = [
    path('', views.Task_list , name= 'Task_list'),
    path('tasks/<int:task_id>/', views.Task_detail , name= 'Task_detail'),
    path('tasks/create/', views.Task_create , name= 'Task_create'),
    path('tasks/<int:task_id>/edit/', views.Task_update , name= 'Task_update'),
    path('tasks/<int:task_id>/delete/', views.Task_delete , name= 'Task_delete'),
    path('tasks/filter/',views.filter_task ,name='tasks-filter'),
    path('tasks/filter_date/',views.filter_by_date ,name='tasks-filter-by-date'),
    path('login/', login_register_view, name='login_register'),
]