from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailtView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    form_class  = StudentForm
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student-list')