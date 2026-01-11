from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from .models import MovieFBV, MovieCBV, MovieMixin, MovieGeneric, MovieViewSetModel
from .serializers import (
    MovieFBVSerializer,
    MovieCBVSerializer,
    MovieMixinSerializer,
    MovieGenericSerializer,
    MovieViewSetSerializer,
)


@api_view(['GET', 'POST'])
def fbv_movie_list(request):
    if request.method == 'GET':
        movies = MovieFBV.objects.all()
        return Response(MovieFBVSerializer(movies, many=True).data)

    if request.method == 'POST':
        serializer = MovieFBVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def fbv_movie_detail(request, pk):
    movie = get_object_or_404(MovieFBV, pk=pk)

    if request.method == 'GET':
        return Response(MovieFBVSerializer(movie).data)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#---------------------------------------------------------------------

class CBVMovie(APIView):
    def get(self, request):
        movies = MovieCBV.objects.all()
        return Response(MovieCBVSerializer(movies, many=True).data)

    def post(self, request):
        serializer = MovieCBVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CBVMovieDetail(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(MovieCBV, pk=pk)
        return Response(MovieCBVSerializer(movie).data)
 
#----------------------------------------------------------------------
class MixinMovieList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = MovieMixin.objects.all()
    serializer_class = MovieMixinSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MixinMovieDetail(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = MovieMixin.objects.all()
    serializer_class = MovieMixinSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#-----------------------------------------------------
class GenericMovieList(generics.ListCreateAPIView):
    queryset = MovieGeneric.objects.all()
    serializer_class = MovieGenericSerializer

class GenericMovieDetail(generics.RetrieveDestroyAPIView):
    queryset = MovieGeneric.objects.all()
    serializer_class = MovieGenericSerializer
#---------------------------------------------------------

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieViewSetModel.objects.all()
    serializer_class = MovieViewSetSerializer
