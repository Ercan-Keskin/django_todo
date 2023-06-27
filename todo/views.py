from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .seralizers import TodoSerializers



# Create your views here.
@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method == 'GET':
        #todo = Todo.objects.filter(is_done = False) #filter dememizin sebebi kullanıcının yapmamış olduğu görevler
        todo = Todo.objects.all() # bu şekilde dersek tüm yapılanları gösterir
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id): #id==pk
    
    todo = get_object_or_404 (Todo, id = id) # bunu buraya yazınca altta tekrar yamamıza gerek yok
    
    if request.method == 'GET':
        # todo = Todo.objects.get(id = id)
        # todo = get_object_or_404(Todo, id = id)
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # todo = get_object_or_404 (Todo, id = id)
        serializer = TodoSerializers(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.delete()
        message = {
            'message' : "Todo deleted succesfully"
            
        }
        
        return Response (message)
        
        
class Todos(ListCreateAPIView):
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializers #bu objene hangi serializers classını kullanacağızımı yazıyoruz
    
class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializers
    lookup_field = 'id'
        

class todoMVS (ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers