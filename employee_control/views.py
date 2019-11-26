from django.shortcuts import render
from employee_control.models import Employee
from django.views import View

# Create your views here.

class HomeView(View):
    template_name = 'employee_control/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
