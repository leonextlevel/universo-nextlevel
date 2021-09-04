from django.urls import path


from .views import (
    PersonagemListView,
    PersonagemCreateView,
    PersonagemUpdateView,
    PersonagemDetailView,
    personagem_delete_view,
)

urlpatterns = [
    path('list/', PersonagemListView.as_view(), name="personagem_list"),
    path('new/', PersonagemCreateView.as_view(), name="personagem_form"),
    path('update/<int:pk>/', PersonagemUpdateView.as_view(), name="personagem_form"),
    path('detail/<int:pk>/', PersonagemDetailView.as_view(), name="personagem_detail"),
    path('delete/<int:pk>/', personagem_delete_view, name="personagem_delete"),
]
