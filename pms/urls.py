from django.urls import path
from . import views

urlpatterns = [
    path("faculty/<int:pk>/", views.FacultyView.as_view(), name='facutly-detail'),
    path("project/<int:pk>/", views.project_detail, name='project_detail'),
    path("student/<int:pk>/", views.StudentView.as_view(), name='student-detail'),
    path("module/<int:pk>/", views.module_detail, name='module_detail'),

]