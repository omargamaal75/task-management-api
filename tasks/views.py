from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'status', 'priority']
    ordering_fields = ['due_date', 'priority', 'created_at']
    ordering = ['due_date']
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        
        # تصفية يدوية بدون django-filter
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        if task.status != 'completed':
            task.status = 'completed'
            task.save()
            return Response({'status': 'task marked as complete'})
        return Response({'error': 'Task is already completed'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        if task.status == 'completed':
            task.status = 'pending'
            task.save()
            return Response({'status': 'task marked as incomplete'})
        return Response({'error': 'Task is not completed'}, status=status.HTTP_400_BAD_REQUEST)