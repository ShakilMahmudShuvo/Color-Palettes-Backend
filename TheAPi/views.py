from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Palette
from .serializers import PaletteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.views import View

class PaletteViewSet(viewsets.ModelViewSet):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

    def get_permissions(self):
        # Customize permissions based on user type
        if self.action == 'create':
            return [permissions.IsAuthenticated()]  # Only authenticated users can create
        elif self.action == 'update' or self.action == 'partial_update':
            return [IsAdminUser()]  # Only admin users can update
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        # Associate the palette with the current user if not an admin
        if not self.request.user.is_staff:
            serializer.save(user=self.request.user)
        else:
            serializer.save()  # Allow admin to set user
    def get_queryset(self):
        queryset = super().get_queryset() # Override the get_queryset method to filter palettes by public or private status and user favorites
        is_public = self.request.query_params.get("is_public") # Get the query parameters from the request URL
        user_id = self.request.query_params.get("user_id")
        favorite_id = self.request.query_params.get("favorite_id")
        
        # Filter palettes based on the is_public query parameter
        if is_public is not None:
            queryset = queryset.filter(is_public=is_public)
        else:
            queryset = queryset.filter(is_public=True)  # Default to only public palettes
        
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        if favorite_id is not None:
            queryset = queryset.filter(favorites__id=favorite_id)
        return queryset



# Extra Task

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import Palette
from .serializers import PaletteSerializer

class PaletteSearchView(View):
    template_name = 'search.html'

    def get(self, request):
        return render(request, self.template_name, {'results': []})

    def post(self, request):
        search_name = request.POST.get('name')
        if search_name:
            results = Palette.objects.filter(is_public=True, name__icontains=search_name)
            serialized_results = PaletteSerializer(results, many=True, context={'request': request}).data
            # Use the render function to return an HTML page with the results
            return render(request, self.template_name, {'results': serialized_results})
        else:
            # Use the render function to return an HTML page with a message
            return render(request, self.template_name, {'message': 'Please provide a search name.'})
