from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from . models import Book
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# REGISTER
@api_view(['POST'])
def registration(request):
  User.objects.create_user(username=request.data["user"],
                           email=request.data["email"],
                           password=request.data["password"],
                           is_staff=1,is_superuser=0)
  return JsonResponse({"done":"test"} )

# Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username        
        token['email'] = user.email
        token['Check'] = "Works"
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBook(request):
    title= request.data['title'],
    author= request.data['author'],
    publishYear= request.data['publishYear']
    Book.objects.create(title=title, author=author,publishYear=publishYear, user=request.user)
    return JsonResponse({"adding_book":"success"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userbooks(request):
  user = request.user
  res = []  # create an empty list
  for bookObj in user.book_set.all():  # user.book_set.all - returns all the books of the loged user
        res.append(
            {"title": bookObj.title,
             "author": bookObj.author,
             "publishYear": bookObj.publishYear,
             "id": bookObj._id})

  return JsonResponse(res, safe=False)
