# from django.urls import path
# from tasks.views import manager_dashboard, user_dashboard, test,create_task,view_task,update_task,delete_task

# urlpatterns = [
#     path('manager_dashboard/',manager_dashboard,name='manager_dashboard'),
#     path('user_dashboard/',user_dashboard),
#     path('test/', test),
#     path('create-task/',create_task,name="create_task"),
#     path('view_task/',view_task),
#     path('update_task/<int:id>/',update_task,name="update_task"),
#     path('delete_task/<int:id>/',delete_task,name="delete_task"),
# ]

from django.urls import path 
from tasks.views import manager_dashboard, user_dashboard, test, create_task, view_task, update_task, delete_task

urlpatterns = [
    path('', manager_dashboard, name='home'),  # ✅ Root path এর জন্য view
    path('manager_dashboard/', manager_dashboard, name='manager_dashboard'),
    path('user_dashboard/', user_dashboard),
    path('test/', test),
    path('create-task/', create_task, name="create_task"),
    path('view_task/', view_task),
    path('update_task/<int:id>/', update_task, name="update_task"),
    path('delete_task/<int:id>/', delete_task, name="delete_task"),
]
