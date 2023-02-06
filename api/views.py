from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serilizers import CompanySerializers
from .models import Company
# Create your views here.

# @api_view(['GET'])
# def apiOverView(request):
#     api_urls = {
#         'List' : '/company-list',
    
#     }
#     return Response(api_urls)


@api_view(['GET'])
def showAll(request):
    companyList = Company.objects.all()
    serilizer =  CompanySerializers(companyList)

    return Response(serilizer.data)