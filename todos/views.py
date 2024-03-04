from django.shortcuts import render

# Importar classe de tabelas/bd do arquivo models.py
from .models import Todo

# Página básica exemplo com HttpResponse
# # from django.http import HttpResponse
# # # Create your views here.
# # def home(request):
# #     return render(request, "todos\home.html")


# View baseada em função - Function views (LISTVIEW)
def todo_list(request):
    todos = Todo.objects.all() # Context - Buscanto todos os objetos de Todo
    #A busca é realizada já na pasta 'templates'. Portanto, restam as subpastas todos/<arquivos>
    return render(request, "todos/todo_list.html", {"todos": todos})




# View baseadas em classes - CBV ClassBaseViews (Recurso mais recente e recomendado)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
'''
Isso substitui o código acima baseado em função - Deve atualizar os nomes em URL e Templates
class TodoListView(ListView):
    model = Todo
'''

# Página de cadastro de tarefas
# 1 Importe o CreateView
# 2 Crie a class base
# 3 Defina a rota
# 4 Informe os nomes dos campos na classe (fields) numa lista e entre aspas
# 5 Atribua nomes para as urls em urls.py
# 6 Importar o reverse_lazy para usar o nome da rota aqui.
# 7 Defina um sucess_url para redirecionar a página após novo registro, com reverse_lazy("NOME")


from django.urls import reverse_lazy
class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("home_pg")

# Repetir processo para página de UpdateView
# Repete basicamente todos os parâmetros do CreateView
# Diferença: Necessário identificar o item através do ID ou PK
    # Por padrão, o UpdateView já envia o todo.pk, então o objeto existe na página html
    # possibilitando fazer verificação condicional para alterar título "if todo.pk is True: [...]"
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("home_pg")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("home_pg")

# CRUD FINALIZADO ACIMA --------------------------
    

# Função de concluir tarefa
    
from datetime import date
'''
class TodoCompleteView(View):
    def get(self, request, pk): # Receba estes parâmetros
        todo.objects.get(pk=pk) # Busque no banco de dados uma tarefa que tenha pk = pk
        todo.finalizado = date.today()
        todo.save()
        return #Redirecionar para página inicial 
'''

#Utilizando biblioteca shortcuts
from django.shortcuts import get_object_or_404, redirect

class TodoCompleteView(View):
    def get(self, request, pk): # Receba estes parâmetros
        todo = get_object_or_404(Todo, pk=pk) # Busque no banco de dados uma tarefa que tenha pk == pk ou apresente #404
        todo.finalizado = date.today()
        todo.save()
        return redirect("home_pg") #Redirecionar para página inicial 
