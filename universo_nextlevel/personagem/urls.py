from django.urls import path


from .views import PersonagemListView, PersonagemCreateView, PersonagemUpdateView

urlpatterns = [
    path('list/', PersonagemListView.as_view(), name="personagem_list"),
    path('new/', PersonagemCreateView.as_view(), name="personagem_form"),
    path('update/<int:pk>/', PersonagemUpdateView.as_view(), name="personagem_form"),
]
