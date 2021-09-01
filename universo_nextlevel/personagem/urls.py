from django.urls import path


from .views import PersonagemListView, PersonagemCreateView

urlpatterns = [
    path('list/', PersonagemListView.as_view(), name="personagem_list"),
    path('new/', PersonagemCreateView.as_view(), name="personagem_form"),
]