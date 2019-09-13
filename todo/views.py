from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Category, TodoList

# Create your views here.


def indexView(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        try:
            if 'addTask' in request.POST:
                title = request.POST['description']
                date = str((request.POST['date']))
                category = request.POST['select_category']
                content = title + " -- " + date + " -- " + category

                todo = TodoList(title=title, date_due=date, category=Category.objects.get(name=category), content=content)
                todo.save()

                return redirect("/")
        except Exception:
            return render(request, "index.html", {"todos": todos, "categories": categories})

        try:
            if 'deleteTask' in request.POST:
                checkedList = request.POST["checkedbox"]

                for todo_id in checkedList:
                    todo = TodoList.objects.get(id)
                    todo.delete()

                return redirect("/")

        except Exception:
            return render(request, "index.html", {"todos": todos, "categories": categories})

    return render(request, "index.html", {"todos": todos, "categories": categories})