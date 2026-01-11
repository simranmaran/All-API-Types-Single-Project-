# # serializers.py
# from rest_framework import serializers
# from .models import MovieFBV,MovieCBV, MovieMixin,MovieGeneric,MovieViewSetModel

# class MovieFBVSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieFBV
#         fields = '__all__'
        
        
# class MovieCBVSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieCBV
#         fields = '__all__'
        

# class MovieMixinSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieMixin
#         fields = '__all__'
        

# class MovieGenericSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieGeneric
#         fields = '__all__'


# class MovieViewSetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieViewSetModel
#         fields = '__all__'



from rest_framework import serializers
from .models import *

class MovieFBVSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFBV
        fields = '__all__'
        


class MovieCBVSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCBV
        fields = '__all__'


class MovieMixinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieMixin
        fields = '__all__'



class MovieGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGeneric
        fields = '__all__'
        


class MovieViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieViewSetModel
        fields = '__all__'
