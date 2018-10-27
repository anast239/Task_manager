"""Определяет схемы для URL для tasks_manager."""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Домашняя страница
    url(r'^$', views.index, name='index'),

    #Вывод всех заданий
    url(r'^tasks/$', views.tasks, name='tasks'),

    #Страница для добавления нового задания
    url(r'^new_task/$', views.new_task, name='new_task'),

    #Cтраница для редактирования задания
    url(r'^edit_task/(?P<task_id>\d+)/$', views.edit_task, 
    	name='edit_task'),
]
