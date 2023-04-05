from rest_framework import viewsets
from .models import User, List, Item
from .serializers import ItemSerializer, ListSerializer, UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

# User has the custom behaviour of creating a new list for them 
# upon creation so we'll need to define a custom create method
# to override the default provided by rest-framework
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # When creating a new user, create a new list for them
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data['id'])
        # user.save()

        # Create list for user
        list = List(name=f"{user.name}'s List", user=user)
        list.save()

        return response
