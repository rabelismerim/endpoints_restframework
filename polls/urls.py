from django.urls import include, path



urlpatterns = [
    path('', include("polls.mestre.api.urls")),
    path('', include("polls.aluno.api.urls")),
    path('', include("polls.mestre_aluno.api.urls")),
    path('', include("polls.reuniao.api.urls")),
    path('', include("polls.reuniao_tarefa.api.urls")),
    path('', include("polls.competencia.api.urls")),
]

