from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView, ListView
from .models import *
from django.shortcuts import get_object_or_404
from .forms import CommentForm, ModuleForm
# Create your views here.

class FacultyView(View):
    def get(self, request, pk):
        faculty = get_object_or_404(Faculty, pk=pk)
        projects = faculty.project_set.all()

        context = {
            "faculty": faculty,
            "projects": projects
        }

        return render(request, 'pms/faculty.html', context)
    
def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    modules = Module.objects.filter(project=project)
    
    if request.method == 'POST':
        module_form = ModuleForm(request.POST, request.FILES)
        if module_form.is_valid():
            new_module = module_form.save(commit=False)
            new_module.project = project
            new_module.save()
    else:
        module_form = ModuleForm()
    
    context = {
        'project': project,
        'modules': modules,
        'module_form': module_form,
    }
    return render(request, 'pms/project.html', context)

    
class StudentView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        projects = student.project_set.all()
        context = {
            "student": student,
            "projects": projects
        }
        return render(request, 'pms/student.html', context)


def module_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    module_rating = ModuleRating.objects.filter(module=module).first()
    comments = Comment.objects.filter(module=module)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.module = module
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'module': module,
        'module_rating': module_rating,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'pms/module_detail.html', context)