from django.urls import path, include

from .views import (
    CenarioCreateView,
    CenarioDetailView,
    CenarioListView,
    CenarioUpdateView,
    HomeView,
    LoginView,
    cenario_delete_view,
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cenario/', include([
        path('list/', CenarioListView.as_view(), name='cenario_list'),
        path('new/', CenarioCreateView.as_view(), name="cenario_form"),
        path('update/<int:pk>/', CenarioUpdateView.as_view(), name="cenario_form"),
        path('detail/<int:pk>/', CenarioDetailView.as_view(), name="cenario_detail"),
        path('delete/<int:pk>/', cenario_delete_view, name="cenario_delete"),
    ]))
]
