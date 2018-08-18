from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse

class IndexView(TemplateView):
    template_name = 'plan/index.html'

    def get(self, request):
        return render(request, self.template_name)
