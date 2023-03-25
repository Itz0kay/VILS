from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status
 
from Contents.models import *
from Contents.serializer import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def contentList(request):
    if request.method == 'GET':
        allcontent = Content.objects.all()
        
        contents_serializer = ContentSerializer(allcontent, many=True) # Serialising the content
        return JsonResponse(contents_serializer.data, safe=False)
    
    elif request.method == 'POST':
        content_serializer = ContentSerializer(data=request.data) # Getting the data from the 
        if content_serializer.is_valid():
            content_serializer.save()
            return JsonResponse(content_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def contentdetail(request, pk):
    try: 
        content = Content.objects.get(pk=pk) # Getting content according to the pk passed through apis
    except Content.DoesNotExist: 
        return JsonResponse({'message': 'The Content does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        content_serializer = ContentSerializer(content) 
        return JsonResponse(content_serializer.data) 
 
    elif request.method == 'PUT': 
        print(request.data )

        field_to_update = request.data.get('field')
        new_value = request.data.get('value')

        if not field_to_update or not new_value:
            return JsonResponse({'error': 'field and new_value fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the specified field
        setattr(content, field_to_update, new_value)
        content.save()

        content_serializer = ContentSerializer(content)
 
        return JsonResponse(content_serializer.data) 
 
    elif request.method == 'DELETE': 
        content.delete() 
        return JsonResponse({'message': 'Content was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)