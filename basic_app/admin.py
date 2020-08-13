from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(HistoryForm)
admin.site.register(ChiefComplaint)
admin.site.register(PastHistory)
admin.site.register(TreatmentHistory)
admin.site.register(Menstrual)
admin.site.register(ObstericHistroy)
admin.site.register(PreviousReport)
admin.site.register(PhysicalExamination)
admin.site.register(TetanusImmunisation)

admin.site.register(Diagnosis)
admin.site.register(Investigation)
admin.site.register(Precaution)
admin.site.register(Drug)
admin.site.register(Dosage)
admin.site.register(Time)
admin.site.register(Prescription)
admin.site.register(DrugDosageTime)
admin.site.register(DrugDosageTimeDischarge)

admin.site.register(DischargeSummary)
admin.site.register(PostiveNegative)
admin.site.register(BloodGroup)
