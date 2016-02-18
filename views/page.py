from django.views.generic import ListView , DetailView
from courses.models import Page

class PageList(ListView):
    model=Page
    template_name='page_view_1.html'

class PageDetail(DetailView):
    model=Page
    template_name='page_view_2.html'
