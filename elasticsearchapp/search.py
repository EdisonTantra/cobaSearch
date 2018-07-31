from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()
es = Elasticsearch()

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
    if es.indices.exists(index=indexName):
        return True
    return False


def bulkIndexing():
    es = Elasticsearch()
    DiseaseIndex.init(index='diseases')
    bulk(client=es, actions=(element.indexing() for element in models.Disease.objects.all().iterator()))

def search(symptoms):
    query1 = Q("multi_match", query=symptoms,fields=["diseaseName^2", "diseaseSearchName^2", "diseaseOverview"])
    query2 = Q("match", diseaseCausesEffect=symptoms)
    query3 = Q("match", diseaseCallDoctor=symptoms)
    query4 = Q("match", diseasePrevention=symptoms)
    query5 = Q("bool", filter=[query2, query3, query4])
    queryFinal = query1 | query5

    s = Search(using=es, index='diseases')
    s = s.query(queryFinal)
    response = s.execute()
    for hit in s:
        print("{} : {}".format(hit.meta.score, hit.diseaseName))
    return response