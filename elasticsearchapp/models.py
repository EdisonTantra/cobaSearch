# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import DiseaseIndex
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers

class Disease(models.Model):
    diseaseName = models.CharField(max_length=200)
    diseaseSearchName = models.CharField(max_length=200)
    photoLarge = models.CharField(max_length=200)
    photoSmall = models.CharField(max_length=200)
    diseaseOverview = models.TextField()
    diseaseCausesEffect = models.TextField()
    diseaseCallDoctor = models.TextField()
    diseasePrevention = models.TextField()
    diseaseTreatment = models.TextField()
    createddAt = models.DateField(default=timezone.now)
    updateddAt = models.DateField(default=timezone.now)
    #################### NOT AVAILABLE DATA
    diseaseDescription = models.TextField()
    diseaseSymptom = models.TextField()
    diseaseComplication = models.TextField()
    diseaseDiagnosis = models.TextField()
    diseaseHomeTreatment = models.TextField()
    diseaseMetaDescription = models.TextField()
    diseaseFactMyth = models.TextField()
    diseaseExamTests = models.TextField()
    diseaseHealthTools = models.TextField()
    diseaseHappening = models.TextField()
    diseaseMedications = models.TextField()
    diseaseMetaKeywords = models.TextField()
    diseaseMetaTitle = models.TextField()
    diseaseOtherPlaces = models.TextField()
    diseaseOtherTreatment = models.TextField()
    diseaseRiskIncrease = models.TextField()
    diseaseSpread = models.TextField()
    diseaseSurgery = models.TextField()

    def indexing(self):
        obj = DiseaseIndex(
            meta={'id': self.id},
            diseaseName=self.diseaseName,
            diseaseSearchName=self.diseaseSearchName,
            photoLarge=self.photoLarge,
            photoSmall=self.photoSmall,
            diseaseOverview=self.diseaseOverview,
            diseaseCausesEffect=self.diseaseCausesEffect,
            diseaseCallDoctor=self.diseaseCallDoctor,
            diseasePrevention=self.diseasePrevention,
            diseaseTreatment=self.diseaseTreatment,
            createddAt=self.createddAt,
            updateddAt=self.updateddAt
        )
        obj.save(index='diseases')
        return obj.to_dict(include_meta=True)