from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from rest_framework.authentication import TokenAuthentication
from .models import *
from .permissions import IsOwner


#Представления для api с ограничением доступа к чужим записям и аутентификацией по токену


#Представление для создания записей

class NoteCreateView(generics.CreateAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        text = self.request.data['text']
        # Замена названия категории в запросе на id
        category = Category.objects.filter(title=self.request.data['category'])[0].id
        user = self.request.user
        data = {'text': text, 'user': user, 'category': category}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = super().get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#Представление для передачи всех записей пользователя

class NoteListView(generics.ListAPIView):
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)


#Представление для передачи конкретной записи пользователя для чтения, редактирования и удаления

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
    permission_classes = (IsOwner, )
    authentication_classes = (TokenAuthentication, )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {}
        #Замена названия категории в запросе на id
        if request.data['category']:
            category = Category.objects.filter(title=request.data['category'])[0].id
            data['category'] = category
        data['text'] = request.data.get('text', Note.objects.filter(pk=kwargs['pk'])[0].text)
        data['date'] = request.data.get('date', timezone.now())
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    serializer_class = RetrieveUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        self.serializer_class = RetrieveUserSerializer
        return super().get(request, *args, **kwargs)