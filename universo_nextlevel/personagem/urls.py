from django.urls import path


from .views import PersonagemListView

urlpatterns = [
    path('list/', PersonagemListView.as_view(), name="personagem_list"),
]