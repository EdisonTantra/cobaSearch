# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Disease
from .search import isExistIndex, bulkIndexing, search
from .loadData import loadJSON

@api_view(['GET'])
def index(request):
    return Response("Welcome to API", status=status.HTTP_200_OK)

@api_view(['GET'])
def setup(request):
    # try:
    if not isExistIndex("diseases"):
        if Disease.objects.count() ==  0:
            loadJSON('data/dataPenyakit.json')
        bulkIndexing()
    # except:
    #     return Response("Something Wrogn!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response("Setup ready!", status=status.HTTP_200_OK)

@api_view(['POST'])
def searchDiseases(request):
    symp1 = request.data["symptom1"]
    symp2 = request.data["symptom2"]
    symp3 = request.data["symptom3"]
    sympFinal = symp1 + " " + symp2 + " " + symp3
    response = search(sympFinal)
    result = {}
    sortedDisease = []
    resultDict = {}
    for hits in response:
        resultDict[hits.meta.score] = hits.diseaseName

    for key in sorted(resultDict):
        sortedDisease.append(resultDict[key])

    result["sortedDisease"] = sortedDisease
    result["rawResult"] = resultDict
    
    return Response(result, status=status.HTTP_200_OK)