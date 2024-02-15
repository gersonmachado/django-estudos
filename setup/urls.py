from django.contrib import admin
from django.urls import path

from todos.views import todo_list, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

# from todos.views import home  #Exemplo: importando função criada no arquivo view na pasta todos
# from todos.views import todo_list(função), CreateView(classe) etc

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", home),  #Exemplo: Declarando a nova rota criada na todo.views com a função home
    path("", todo_list, name="home_pg"),
    path("create", TodoCreateView.as_view(), name="create_pg"),
    # adicionar variável na path através de <>, tipo de variável e nome da variável <tipo:nome>
    path("update/<int:pk>", TodoUpdateView.as_view(), name="update_pg"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="delete_pg"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="complete_pg"),

]
