# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SpliceTray, Coupler
from .forms import SpliceTrayForm, CouplerForm



class SpliceTrayListView(ListView):
    model = SpliceTray
    template_name = 'netbox_access_lists/splice_tray_list.html'


class SpliceTrayCreateView(CreateView):
    model = SpliceTray
    form_class = SpliceTrayForm
    template_name = 'generic/form.html'


class SpliceTrayUpdateView(UpdateView):
    model = SpliceTray
    form_class = SpliceTrayForm
    template_name = 'generic/form.html'


class SpliceTrayDeleteView(DeleteView):
    model = SpliceTray
    success_url = reverse_lazy('plugins:netbox_access_lists:splicetray_list')
    template_name = 'generic/delete_confirm.html'


class CouplerListView(ListView):
    model = Coupler
    template_name = 'netbox_access_lists/Coupler.html'


class CouplerCreateView(CreateView):
    model = Coupler
    form_class = CouplerForm
    template_name = 'generic/form.html'


class CouplerUpdateView(UpdateView):
    model = Coupler
    form_class = CouplerForm
    template_name = 'generic/form.html'


class CouplerDeleteView(DeleteView):
    model = Coupler
    success_url = reverse_lazy('plugins:netbox_access_lists:coupler_list')
    template_name = 'generic/delete_confirm.html'
