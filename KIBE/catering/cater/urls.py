from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import (SignUpView,
                     Packageview, 
                     Aboutview, 
                     Homeview, 
                     PackageDetailview, 
                     BookPackageView, 
                     DecisionView,
                     MerchantCreateView, 
                     MerchantPackageview, 
                     PackageDeleteView, 
                     PackageUpdateView)
                     

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('decision/', DecisionView.as_view(), name='decision'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(template_name='cater/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cater/logout.html'), name='logout'),
    path('about/', Aboutview.as_view(), name='about'),
    path('package/', Packageview.as_view(), name='package'),
    path('package/<str:pk>/', PackageDetailview.as_view(), name='package-detail'),
    path('package_merchant/', MerchantPackageview.as_view(), name='merchant_package_detail'),
    path('book-package/<int:package_id>/', BookPackageView.as_view(), name='book_package'),
    path('merchants/', MerchantCreateView.as_view(), name='merchant_list'),

    # path for deleting a package
    path('package/<int:pk>/delete/', PackageDeleteView.as_view(), name='package_delete'),
    # path for updating a package
    path('package/<int:pk>/update/', PackageUpdateView.as_view(), name='package_update')
]
