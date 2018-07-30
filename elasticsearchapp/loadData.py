from .serializers import DiseaseSerializer
from .models import Disease
import json

def loadJSON(fileLoc):
    with open(fileLoc) as file:
        data = json.load(file)

    for disease in data["diseases"]:
        Disease.objects.create(**disease)