from django.urls import path, include
from rest_framework import routers

from .views import todo_list_create, todo_detail, Todos, TodoDetail, todoMVS

router = routers.DefaultRouter()
router.register("todo", todoMVS)


urlpatterns = [
    # path("list-create", todo_list_create),
    # path("detail/<int:id>", todo_detail),
    # path("list-created/", Todos.as_view()), #class basic yapı kullandıysak as_view kullanıyoru
    # path("detail/<int:id>",TodoDetail.as_view()),
    
    path ("", include(router.urls)),
    
]