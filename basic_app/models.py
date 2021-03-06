from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.

sex_choice = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

post_negat = (
    ('+ve', '+ve'),
    ('-ve', '-ve'),
    ('neutral', 'Neutral')
)

blood_group = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=sex_choice, default='F')
    address = models.CharField(max_length=256, blank=True, default='')
    mobile = models.CharField(max_length=10, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name+", Id: "+str(self.pk)


    # def get_absolute_url(self):
    #     return reverse("basic_app:detail",kwargs={'pk':self.pk})

    class Meta:
        db_table = "Patient"

class ChiefComplaint(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class PastHistory(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class TreatmentHistory(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Menstrual(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class ObstericHistroy(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Diagnosis(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Investigation(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Precaution(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Drug(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Dosage(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class Time(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class PostiveNegative(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name

        class Meta:
            ordering = ('name',)


class BloodGroup(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name


class HistoryForm(models.Model):
    patient = models.OneToOneField(Patient, related_name='historyforms', on_delete=models.CASCADE)
    chief_complaints = models.ManyToManyField(ChiefComplaint, blank=True)
    past_history = models.ManyToManyField(PastHistory, blank=True)
    treatment_history = models.ManyToManyField(TreatmentHistory, blank=True)
    menstrual = models.ManyToManyField(Menstrual, blank=True)
    obsteric_histroy = models.ManyToManyField(ObstericHistroy, blank=True)
    g = models.CharField(max_length=200, blank=True, default='')
    p = models.CharField(max_length=200, blank=True, default='')
    a = models.CharField(max_length=200, blank=True, default='')
    l = models.CharField(max_length=200, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

    class Meta:
        db_table = "HistoryForm"

class PreviousReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hb = models.CharField(max_length=256, blank=True, default='')
    hb_date = models.DateField(blank=True, null=True)
    platelet = models.CharField(max_length=256, blank=True, default='')
    platelet_date = models.DateField(blank=True, null=True)
    bt = models.CharField(max_length=256, blank=True, default='')
    bt_date = models.DateField(blank=True, null=True)
    ct = models.CharField(max_length=256, blank=True, default='')
    ct_date = models.DateField(blank=True, null=True)
    bs_f = models.CharField(max_length=256, blank=True, default='')
    bs_f_date = models.DateField(blank=True, null=True)
    bs_pp = models.CharField(max_length=256, blank=True, default='')
    bs_pp_date = models.DateField(blank=True, null=True)
    ur_m = models.CharField(max_length=256, blank=True, default='')
    ur_m_date = models.DateField(blank=True, null=True)
    s_tsh = models.CharField(max_length=256, blank=True, default='')
    s_tsh_date = models.DateField(blank=True, null=True)
    usg = models.CharField(max_length=256, blank=True, default='')
    usg_date = models.DateField(blank=True, null=True)
    mri_ct_scan = models.CharField(max_length=256, blank=True, default='')
    mri_ct_scan_date = models.DateField(blank=True, null=True)
    ecg = models.CharField(max_length=256, blank=True, default='')
    ecg_date = models.DateField(blank=True, null=True)
    chest_x_ray = models.CharField(max_length=256, blank=True, default='')
    chest_x_ray_date = models.DateField(blank=True, null=True)

    blood_group = models.CharField(max_length=3, choices=blood_group, blank=True, default='')
    blood_group_date = models.DateField(blank=True, null=True)
    hcv = models.CharField(max_length=10, choices=post_negat, blank=True, default='')
    hcv_date = models.DateField(blank=True, null=True)
    hbs_ag = models.CharField(max_length=10, choices=post_negat, blank=True, default='')
    hbs_ag_date = models.DateField(blank=True, null=True)
    hiv =  models.CharField(max_length=10, choices=post_negat, blank=True, default='')
    hiv_date = models.DateField(blank=True, null=True)
    vdrl =  models.CharField(max_length=10, choices=post_negat, blank=True, default='')
    vdrl_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

    class Meta:
        db_table = "PreviousReport"

class TetanusImmunisation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_tt1 = models.DateField(blank=True, null=True)
    date_tt2 = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.patient.name

    class Meta:
        db_table = "TetanusImmunisation"

class PhysicalExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pr = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    bp = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    wt = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    ht = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    uterus_funal_ht = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    presentation = models.CharField(max_length=256, blank=True, default='')
    fhs = models.DecimalField(max_digits=15, decimal_places=3, blank=True, default=Decimal(0))
    per_vaginum = models.CharField(max_length=256, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

    class Meta:
        db_table = "PhysicalExamination"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_id = models.AutoField(primary_key=True)
    diagnosis = models.ManyToManyField(Diagnosis, blank=True)
    investigation = models.ManyToManyField(Investigation, blank=True)
    precaution = models.ManyToManyField(Precaution, blank=True)
    follow_up = models.CharField(max_length=256, blank=True, default='')
    comment = models.CharField(max_length=256, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    # drug_dostage_time = models.ForeignKey(DrugDosageTime, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name + ": "+ (self.created_at).strftime("%d %b %Y at %H:%M:%S")

    class Meta:
        db_table = "Prescription"

class DischargeSummary(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_id = models.AutoField(primary_key=True)
    husband_name = models.CharField(max_length=200, blank=True, default='')
    doa = models.DateTimeField(blank=True, null=True)
    dod = models.DateTimeField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, default='')
    procedure = models.CharField(max_length=256, blank=True, default='')
    per_op = models.TextField(blank=True, default='')
    baby_details = models.TextField(blank=True, default='')
    hospital_stay = models.CharField(max_length=256, blank=True, default='')
    advice_on_discharge = models.CharField(max_length=256, blank=True, default='')
    precaution = models.ManyToManyField(Precaution, blank=True)
    follow_up = models.CharField(max_length=256, blank=True, default='')
    comment = models.CharField(max_length=256, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    # drug_dostage_time_discharge = models.ManyToManyField(DrugDosageTimeDischarge)

    def __str__(self):
        return self.patient.name + ": "+ (self.created_at).strftime("%d %b %Y at %H:%M:%S")

    class Meta:
        db_table = "DischargeSummary"



class DrugDosageTime(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=1)
    dosage = models.ForeignKey(Dosage, on_delete=models.CASCADE, default = 1)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, default = 1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name+": "+ self.drug.name+", "+ self.dosage.name+", "+ self.time.name+" - "+ (self.created_at).strftime("%d %b %Y at %H:%M:%S")

    class Meta:
        db_table = "DrugDosageTime"

class DrugDosageTimeDischarge(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_summary = models.ForeignKey(DischargeSummary, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=1)
    dosage = models.ForeignKey(Dosage, on_delete=models.CASCADE, default = 1)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, default = 1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name+": "+ self.drug.name+", "+ self.dosage.name+", "+ self.time.name+" - "+ (self.created_at).strftime("%d %b %Y at %H:%M:%S")

    class Meta:
        db_table = "DrugDosageTimeDischarge"
