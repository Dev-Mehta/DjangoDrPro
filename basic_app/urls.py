from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    # Home Page
    path('',views.PatientListView,name='list'),
    # Patient Detail Page
    path('patient/<int:pk>', views.PatientDetailView, name='detail'),
    # Page to create patient obj.
    path('patient/new/', views.PatientCreateView, name='create'),
    # Page to create patient's history. Triggered only once
    path('patient/<int:pk>/create_history/', views.HistoryFormCreateView, name='create_history'),
    # Page to update patient's history. Triggered each time, when
    # patient's history need to be updated
    path('patient/<int:pk>/update_history/', views.HistoryFormUpdateView.as_view(), name='update_history'),
    # Page to view Patient's previous reports
    path('patient/<int:pk>/previous_reports/', views.PreviousReportView, name='previous_report'),

    path('patient/<int:pk>/create_tetanus_immunisation/', views.TetanusImmunisationCreateView, name='create_tetanus_immunisation'),
    path('patient/<int:pk>/update_tetanus_immunisation/', views.TetanusImmunisationUpdateView.as_view(), name='update_tetanus_immunisation'),
    # Page to view Patient's previous reports
    path('patient/<int:pk>/physical_examination/', views.PhysicalExaminationView, name='physical_examination'),

    # Page to Create Patient's Prescription
    path('patient/<int:pk>/create_prescription/', views.CreatePrescription),
    # Page to Create Patient's Prescription
    path('patient/<int:pk>/create_discharge_summary/', views.CreateDischargeSummary),
    # This is where pdfs are created
    # 2 Ways to access this page
    # 1: /patient/1/view_prescription/: Here you can view pdf online
    # 2: /patient/1/view_prescription/?download="whatevervalue" to download pdf
    path('patient/<int:pk>/view_prescription/', views.ViewPrescription),
    path('patient/<int:pk>/view_discharge_summary/', views.ViewDischargeSummary),
    # This is a kindof api type url to create
    # drug dosage time. Used in add more feature during patient prescription
    # form. Only POST request are accepted. POST request are sent using xhr with javascript
    path('patient/<int:pk>/add_ddt/', views.createDDT),
    path('patient/<int:pk>/add_ddt_dis/', views.createDDTDischarge),
    # Page to view all prescriptions ordered in descending order
    path('patient/<int:pk>/view_prescriptions/', views.ViewAllPrescription.as_view()),
    # Page to view prescription in detail
    path('patient/<int:pk>/view_prescriptions/<int:ppk>/', views.PrescriptionDetail.as_view(),name='prescription_detail')
]
