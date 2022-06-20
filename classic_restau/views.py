from restau.models import Restau
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy


# Create your views here.

class ClassicRestauListView(ListView):
    model = Restau
    template_name = 'restau_list.html'


class ClassicRestauDetailView(DetailView):
    model = Restau
    template_name = 'restau_detail.html'


class ClassicRestauUpdateView(UpdateView):
    model = Restau
    fields = '__all__'
    template_name = 'restau_update.html'


class ClassicRestauDeleteView(DeleteView):
    model = Restau
    template_name = 'restau_delete.html'
    success_url = reverse_lazy('restau_list')


class ClassicRestauCreateView(CreateView):
    model = Restau
    template_name = 'restau_create.html'
    fields = '__all__'
    success_url = reverse_lazy('restau_list')
