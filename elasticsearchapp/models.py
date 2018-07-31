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
    photoLarge = models.CharField(max_length=200, default=None, null=True, blank=True)
    photoSmall = models.CharField(max_length=200, default=None, null=True, blank=True)
    diseaseOverview = models.TextField(default=None, null=True, blank=True)
    diseaseCausesEffect = models.TextField(default=None, null=True, blank=True)
    diseaseCallDoctor = models.TextField(default=None, null=True, blank=True)
    diseasePrevention = models.TextField(default=None, null=True, blank=True)
    diseaseTreatment = models.TextField(default=None, null=True, blank=True)
    createddAt = models.DateField(default=timezone.now)
    updateddAt = models.DateField(default=timezone.now)
    #################### NOT AVAILABLE DATA
    diseaseDescription = models.TextField(default=None, null=True, blank=True)
    diseaseSymptom = models.TextField(default=None, null=True, blank=True)
    diseaseComplication = models.TextField(default=None, null=True, blank=True)
    diseaseDiagnosis = models.TextField(default=None, null=True, blank=True)
    diseaseHomeTreatment = models.TextField(default=None, null=True, blank=True)
    diseaseMetaDescription = models.TextField(default=None, null=True, blank=True)
    diseaseFactMyth = models.TextField(default=None, null=True, blank=True)
    diseaseExamTests = models.TextField(default=None, null=True, blank=True)
    diseaseHealthTools = models.TextField(default=None, null=True, blank=True)
    diseaseHappening = models.TextField(default=None, null=True, blank=True)
    diseaseMedications = models.TextField(default=None, null=True, blank=True)
    diseaseMetaKeywords = models.TextField(default=None, null=True, blank=True)
    diseaseMetaTitle = models.TextField(default=None, null=True, blank=True)
    diseaseOtherPlaces = models.TextField(default=None, null=True, blank=True)
    diseaseOtherTreatment = models.TextField(default=None, null=True, blank=True)
    diseaseRiskIncrease = models.TextField(default=None, null=True, blank=True)
    diseaseSpread = models.TextField(default=None, null=True, blank=True)
    diseaseSurgery = models.TextField(default=None, null=True, blank=True)

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