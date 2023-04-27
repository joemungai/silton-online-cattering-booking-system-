from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterForm, PackageForm
from django.views.generic import (TemplateView, ListView, 
                                  CreateView, DetailView, 
                                  FormView, UpdateView, DeleteView)
from django.views import View
from .models import Package

# Create your views here.

class Baseview(TemplateView):
    template_name = 'cater/base.html'

class Homeview(TemplateView):
    template_name = 'cater/home.html'

class DecisionView(TemplateView):
    template_name = 'cater/decision.html'

class SignUpView(CreateView):
    form_class = RegisterForm
    # success_url = reverse_lazy('login')
    template_name = 'cater/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')


@method_decorator(login_required, name='dispatch')
class Aboutview(TemplateView):
    template_name = 'cater/about.html'

@method_decorator(login_required, name='dispatch')
class Packageview(ListView):
    model = Package
    template_name = 'cater/packages.html'

class PackageDetailview(DetailView):
    model = Package
    template_name = 'cater/package_detail.html'
    context_object_name = 'package'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package = self.get_object()
        context['package'] = package
        return context

class BookPackageView(View):
    def get(self, request, package_id):
        # Get the package object
        package = get_object_or_404(Package, pk=package_id)
        context = {
            'package': package,
            'message': 'Your booking has been confirmed. We look forward to seeing you on [date] at [time].'
        }
        return render(request, 'cater/confirmation.html', context)

class MerchantCreateView(FormView):
    template_name = 'cater/package_form.html'
    form_class = PackageForm
    success_url = reverse_lazy('merchant_package_detail')
    ordering = ['-date_created']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MerchantPackageview(ListView):
    model = Package
    template_name = 'cater/merchantPackage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_merchant'] = True
        return context


class PackageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'cater/package_form.html'
    success_url = reverse_lazy('merchant_package_detail')

    def test_func(self):
        package = self.get_object()
        return package.created_by == self.request.user

class PackageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Package
    template_name = 'cater/package_confirm_delete.html'
    success_url = reverse_lazy('merchant_package_detail')

    def test_func(self):
        package = self.get_object()
        return package.created_by == self.request.user
