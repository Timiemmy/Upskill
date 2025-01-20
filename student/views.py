from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import CourseEnrollForm
from course.models import Course


class StudentRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'student/student/registration.html'
    success_url = reverse_lazy('student_course_list')


    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        user = authenticate(username=cleaned_data['username'], password=cleaned_data['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.student.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'student/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(student__in=[self.request.user])


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'student/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(student__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
    # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
    # get first module
            context['module'] = course.modules.all()[0]
        return context