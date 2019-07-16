from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Radiostation

from .serializers import RadiostationSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def getputdelete_one_radio(request, pk):
    try:
        radio = Radiostation.objects.get(pk=pk)
    except Radiostation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single radio
    if request.method == 'GET':
        serializer = RadiostationSerializer(radio)
        return Response(serializer.data)

    # update details of a single radio
    if request.method == 'PUT':
        serializer = RadiostationSerializer(radio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single radio
    if request.method == 'DELETE':
        radio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET', 'POST'])
def getpost_all_radio(request):

    # get all radio
    if request.method == 'GET':
        stations = Radiostation.objects.all()
        serializer = RadiostationSerializer(stations, many=True)
        return Response(serializer.data)

    # insert a new record for a RadioStation
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'genre': request.data.get('genre'),
            'country': int(request.data.get('country')),
            'adress': request.data.get('adress')
        }
        serializer = RadiostationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)