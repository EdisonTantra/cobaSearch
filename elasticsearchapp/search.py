from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class DiseaseIndex(DocType):
    diseaseName = Text()
    diseaseSearchName = Text()
    photoLarge = Text()
    photoSmall = Text()
    diseaseOverview = Text()
    diseaseCausesEffect = Text()
    diseaseCallDoctor = Text()
    diseasePrevention = Text()
    diseaseTreatment = Text()
    createddAt = Date()
    updateddAt = Date()

def isExistIndex(indexName):
    es = Elasticsearch()
    if es.indices.exists(index="index"):
        return True
    return False


def bulkIndexing():
    es = Elasticsearch()
    DiseaseIndex.init(index='diseases')
    bulk(client=es, actions=(element.indexing() for element in models.Disease.objects.all().iterator()))

def search(symptoms):
    query1 = Q("multi_match", query=symptoms,fields=["diseaseName^2", "diseaseOverview"])
    query2 = Q("match", diseaseCausesEffect=symptoms)
    query3 = Q("match", diseaseSearchName=symptoms)
    query4 = Q("match", diseaseCallDoctor=symptoms)
    query5 = Q("match", diseasePrevention=symptoms)
    # query6 = Q("bool", should=[query2, query3, query4, query5])
    queryFinal = query1 | query2 | query3 | query4 | query5

    s = Search(using=client, index='diseases')
    s = s.query(queryFinal)
    response = s.execute()
    for hit in s:
        print("{} : {}".format(hit.meta.score, hit.diseaseName))
    return response