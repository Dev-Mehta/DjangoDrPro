from django import forms
from .models import (Patient, HistoryForm,
					PreviousReport, TetanusImmunisation, PhysicalExamination, Prescription,
					DrugDosageTime, DrugDosageTimeDischarge, DischargeSummary)

class PatientCreateForm(forms.ModelForm):
	class Meta:
		model = Patient
		exclude = ['created_at']

class HistoryCreateForm(forms.ModelForm):
	class Meta:
		model = HistoryForm
		exclude = ['patient','created_at']

class PreviousReportForm(forms.ModelForm):
	hb_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	platelet_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	bt_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	ct_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	bs_f_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	bs_pp_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	ur_m_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	s_tsh_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	usg_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	mri_ct_scan_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	ecg_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	chest_x_ray_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	blood_group_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	hcv_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	hbs_ag_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	hiv_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	vdrl_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	class Meta:
		model = PreviousReport
		exclude = ['patient','created_at']

class TetanusImmunisationCreateForm(forms.ModelForm):
	date_tt1 = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	date_tt2 = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}))
	class Meta:
		model = TetanusImmunisation
		exclude = ['patient']

class PhysicalExaminationForm(forms.ModelForm):
	class Meta:
		model = PhysicalExamination
		exclude = ['patient','created_at']

class PrescriptionCreateForm(forms.ModelForm):
	class Meta:
		model = Prescription
		# exclude = ['patient','created_at']
		fields = ['diagnosis','investigation','precaution','follow_up','comment']

class DischargeSummaryCreateForm(forms.ModelForm):
	class Meta:
		model = DischargeSummary
		# exclude = ['patient','created_at']
		fields = ['husband_name','diagnosis','procedure','per_op','baby_details','hospital_stay','advice_on_discharge',
					'precaution','follow_up','comment']


class DrugDosageTimeForm(forms.ModelForm):
	class Meta:
		model = DrugDosageTime
		exclude = ['patient','created_at',]

class DrugDosageTimeDischargeForm(forms.ModelForm):
	class Meta:
		model = DrugDosageTimeDischarge
		exclude = ['patient','created_at',]
