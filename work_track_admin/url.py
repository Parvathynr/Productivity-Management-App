from django.urls import path
from .import views
urlpatterns = [
    path('add_tasks',views.Add_Tasks,name='Add_tasks'),
    path('update_tasks/<int:id>',views.Update_Tasks,name='Update_Task'),
    path('delete_tasks/<int:id>',views.Delete_Task,name='Delete_Tasks'),
    path('view_tasks',views.View_Tasks,name='View_Tasks'),
    #projects
    path('add_projects',views.Add_Projects,name='Add_projects'),
    path('view_projects',views.View_Projects,name='View_Projects'),
    path('update_projects/<int:id>',views.update_projects,name='Updated_projects'),
    path('delete_projects/<int:id>',views.Delete_Projects,name='Delete_projects')



]
