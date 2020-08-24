from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,UpdateView
from .models import *
from .forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import date
new_ddt = []
new_ddt_dis = []

# Variable names are actually model names' initial letters
# For Eg:
#   p = Patient.objects.get(patient_id=1)
#   ddt = DrugDosageTime
#   hf = HistoryForm etc. etc.
def PatientCreateView(request):
    if request.method == 'POST':
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            # if(len(str(mobile))!=10):
            #     messages.error(request, "Check your mobile number")
            #     return render(request, "basic_app/patient_form.html", {"form":form})
            p = Patient(
                name=name,
                age=age,
                gender=gender,
                address=address,
                mobile=mobile
            )
            p.save()
            return redirect(f'/patient/{p.patient_id}/create_history/')
    else:
        form = PatientCreateForm()
        return render(request, "basic_app/patient_form.html", {"form":form})
    return HttpResponse("Hey")


def PatientListView(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'basic_app/patient_list.html', {"patients":patients})


@csrf_exempt
def PatientDetailView(request, pk):
    if request.method == "POST":
        btn_id = request.POST.get('btn_id')
        if btn_id == "form-submit-physical":
            print("Success")
            pr = PhysicalExamination(
                patient=Patient.objects.get(patient_id=pk),
                pr=request.POST.get('pr'),
                bp=request.POST.get('bp'),
                wt=request.POST.get('wt'),
                ht=request.POST.get('ht'),
                uterus_funal_ht=request.POST.get('uterus_funal_ht'),
                presentation=request.POST.get('presentation'),
                fhs=request.POST.get('fhs'),
                per_vaginum=request.POST.get('per_vaginum'),
            )
            pr.save()
            # return HttpResponse('created')
        else:
            hb_date = request.POST.get('hb_date')
            if hb_date == '':
                hb_date = None
            platelet_date = request.POST.get('platelet_date')
            if platelet_date == '':
                platelet_date = None
            bt_date = request.POST.get('bt_date')
            if bt_date == '':
                bt_date = None
            ct_date = request.POST.get('ct_date')
            if ct_date == '':
                ct_date = None
            bs_f_date = request.POST.get('bs_f_date')
            if bs_f_date == '':
                bs_f_date = None
            bs_pp_date = request.POST.get('bs_pp_date')
            if bs_pp_date == '':
                bs_pp_date = None
            ur_m_date = request.POST.get('ur_m_date')
            if ur_m_date == '':
                ur_m_date = None
            s_tsh_date = request.POST.get('s_tsh_date')
            if s_tsh_date == '':
                s_tsh_date = None
            usg_date = request.POST.get('usg_date')
            if usg_date == '':
                usg_date = None
            mri_ct_scan_date = request.POST.get('mri_ct_scan_date')
            if mri_ct_scan_date == '':
                mri_ct_scan_date = None
            ecg_date = request.POST.get('ecg_date')
            if ecg_date == '':
                ecg_date = None
            chest_x_ray_date = request.POST.get('chest_x_ray_date')
            if chest_x_ray_date == '':
                chest_x_ray_date = None
            blood_group_date = request.POST.get('blood_group_date')
            if blood_group_date == '':
                blood_group_date = None
            hcv_date = request.POST.get('hcv_date')
            if hcv_date == '':
                hcv_date = None
            hbs_ag_date = request.POST.get('hbs_ag_date')
            if hbs_ag_date == '':
                hbs_ag_date = None
            hiv_date = request.POST.get('hiv_date')
            if hiv_date == '':
                hiv_date = None
            vdrl_date = request.POST.get('vdrl_date')
            if vdrl_date == '':
                vdrl_date = None
            p = PreviousReport(
                patient=Patient.objects.get(patient_id=pk),
                hb=request.POST.get('hb'),
                hb_date=hb_date,
                platelet=request.POST.get('platelet'),
                platelet_date=platelet_date,
                bt=request.POST.get('bt'),
                bt_date=bt_date,
                ct=request.POST.get('ct'),
                ct_date=ct_date,
                bs_f=request.POST.get('bs_f'),
                bs_f_date=bs_f_date,
                bs_pp=request.POST.get('bs_pp'),
                bs_pp_date=bs_pp_date,
                ur_m=request.POST.get('ur_m'),
                ur_m_date=ur_m_date,
                s_tsh=request.POST.get('s_tsh'),
                s_tsh_date=s_tsh_date,
                usg=request.POST.get('usg'),
                usg_date=usg_date,
                mri_ct_scan=request.POST.get('mri_ct_scan'),
                mri_ct_scan_date=mri_ct_scan_date,
                ecg=request.POST.get('ecg'),
                ecg_date=ecg_date,
                chest_x_ray=request.POST.get('chest_x_ray'),
                chest_x_ray_date=chest_x_ray_date,
                blood_group=request.POST.get('blood_group'),
                blood_group_date=blood_group_date,
                hcv=request.POST.get('hcv'),
                hcv_date=hcv_date,
                hbs_ag=request.POST.get('hbs_ag'),
                hbs_ag_date=hbs_ag_date,
                hiv=request.POST.get('hiv'),
                hiv_date=hiv_date,
                vdrl=request.POST.get('vdrl'),
                vdrl_date=vdrl_date,
            )
            p.save()
        return HttpResponse('created')
    else:
        form = PreviousReportForm()
        physical_form = PhysicalExaminationForm()
        patient_details = Patient.objects.filter(patient_id=pk)
        if patient_details.exists():
            patient_details = patient_details[0]
            hf = HistoryForm.objects.filter(patient=patient_details)
            if hf.exists():
                hf = hf[0]
                patient_history_exist = "true"
            else:
                patient_history_exist = "false"
            tetimm = TetanusImmunisation.objects.filter(patient=patient_details)
            if tetimm.exists():
                tetimm = tetimm[0]
                tit_exist = "true"
            else:
                tit_exist = "false"
            pr = PreviousReport.objects.filter(patient=patient_details).order_by('-created_at')[:5]
            phy = PhysicalExamination.objects.filter(patient=patient_details).order_by('-created_at')[:5]
            prescription = Prescription.objects.filter(patient=patient_details)
            downloadable = "false"
            ddt = ""
            if prescription.exists():
                prescription = prescription.last()
                ddt = DrugDosageTime.objects.filter(prescription=prescription)
                if ddt.exists():
                    downloadable = "true"


            discharge_summary = DischargeSummary.objects.filter(patient=patient_details)
            ddt_dis = ""
            dischdownload = "false"
            if discharge_summary.exists():
                discharge_summary = discharge_summary.last()
                ddt_dis = DrugDosageTimeDischarge.objects.filter(discharge_summary = discharge_summary)
                if ddt_dis.exists():
                    dischdownload = "true"

            return render(request, "basic_app/patient_detail.html",
                {"patient_details":patient_details,
                "patient_history":hf,
                "patient_history_exist":patient_history_exist,
                "tetanus_immunisation":tetimm,
                "tit_exist":tit_exist,
                "previous_reports":pr,
                "physical_examination":phy,
                "form":form,
                "physical_form":physical_form,
                "prescription":prescription,
                "ddt":ddt,
                "downloadable":downloadable,
                "discharge":discharge_summary,
                "dischdownload":dischdownload,
                "ddt_dis":ddt_dis,
                })
        else:
            return HttpResponse("Patient Does Not Exist")

def PreviousReportView(request, pk):
    if request.method == "POST":
        content = PreviousReport.objects.filter(patient=Patient.objects.get(patient_id=pk)).order_by('-created_at')
        form = PreviousReportForm(request.POST)
        hb_date = request.POST.get('hb_date')
        if hb_date == '':
            hb_date = None
        platelet_date = request.POST.get('platelet_date')
        if platelet_date == '':
            platelet_date = None
        bt_date = request.POST.get('bt_date')
        if bt_date == '':
            bt_date = None
        ct_date = request.POST.get('ct_date')
        if ct_date == '':
            ct_date = None
        bs_f_date = request.POST.get('bs_f_date')
        if bs_f_date == '':
            bs_f_date = None
        bs_pp_date = request.POST.get('bs_pp_date')
        if bs_pp_date == '':
            bs_pp_date = None
        ur_m_date = request.POST.get('ur_m_date')
        if ur_m_date == '':
            ur_m_date = None
        s_tsh_date = request.POST.get('s_tsh_date')
        if s_tsh_date == '':
            s_tsh_date = None
        usg_date = request.POST.get('usg_date')
        if usg_date == '':
            usg_date = None
        mri_ct_scan_date = request.POST.get('mri_ct_scan_date')
        if mri_ct_scan_date == '':
            mri_ct_scan_date = None
        ecg_date = request.POST.get('ecg_date')
        if ecg_date == '':
            ecg_date = None
        chest_x_ray_date = request.POST.get('chest_x_ray_date')
        if chest_x_ray_date == '':
            chest_x_ray_date = None
        blood_group_date = request.POST.get('blood_group_date')
        if blood_group_date == '':
            blood_group_date = None
        hcv_date = request.POST.get('hcv_date')
        if hcv_date == '':
            hcv_date = None
        hbs_ag_date = request.POST.get('hbs_ag_date')
        if hbs_ag_date == '':
            hbs_ag_date = None
        hiv_date = request.POST.get('hiv_date')
        if hiv_date == '':
            hiv_date = None
        vdrl_date = request.POST.get('vdrl_date')
        if vdrl_date == '':
            vdrl_date = None
        pr = PreviousReport(
            patient=Patient.objects.get(patient_id=pk),
            hb=request.POST.get('hb'),
            hb_date=hb_date,
            platelet=request.POST.get('platelet'),
            platelet_date=platelet_date,
            bt=request.POST.get('bt'),
            bt_date=bt_date,
            ct=request.POST.get('ct'),
            ct_date=ct_date,
            bs_f=request.POST.get('bs_f'),
            bs_f_date=bs_f_date,
            bs_pp=request.POST.get('bs_pp'),
            bs_pp_date=bs_pp_date,
            ur_m=request.POST.get('ur_m'),
            ur_m_date=ur_m_date,
            s_tsh=request.POST.get('s_tsh'),
            s_tsh_date=s_tsh_date,
            usg=request.POST.get('usg'),
            usg_date=usg_date,
            mri_ct_scan=request.POST.get('mri_ct_scan'),
            mri_ct_scan_date=mri_ct_scan_date,
            ecg=request.POST.get('ecg'),
            ecg_date=ecg_date,
            chest_x_ray=request.POST.get('chest_x_ray'),
            chest_x_ray_date=chest_x_ray_date,
            blood_group=request.POST.get('blood_group'),
            blood_group_date=blood_group_date,
            hcv=request.POST.get('hcv'),
            hcv_date=hcv_date,
            hbs_ag=request.POST.get('hbs_ag'),
            hbs_ag_date=hbs_ag_date,
            hiv=request.POST.get('hiv'),
            hiv_date=hiv_date,
            vdrl=request.POST.get('vdrl'),
            vdrl_date=vdrl_date,
        )
        pr.save()
        return render(request, "basic_app/patient_previous_report.html", {"form":form,"reports":content})
    form = PreviousReportForm()
    content = PreviousReport.objects.filter(patient=Patient.objects.get(patient_id=pk)).order_by('-created_at')
    return render(request, "basic_app/patient_previous_report.html", {"form":form, "reports":content})

def PhysicalExaminationView(request, pk):
    if request.method == "POST":
        content = PhysicalExamination.objects.filter(patient=Patient.objects.get(patient_id=pk))
        physical_form = PhysicalExaminationForm(request.POST)
        pr = PhysicalExamination(
            patient=Patient.objects.get(patient_id=pk),
            pr=request.POST.get('pr'),
            bp=request.POST.get('bp'),
            wt=request.POST.get('wt'),
            ht=request.POST.get('ht'),
            uterus_funal_ht=request.POST.get('uterus_funal_ht'),
            presentation=request.POST.get('presentation'),
            fhs=request.POST.get('fhs'),
            per_vaginum=request.POST.get('per_vaginum'),
        )
        pr.save()
        return render(request, "basic_app/patient_physical_examination.html", {"physical_form":physical_form,"physical_examination":content})
    physical_form = PhysicalExaminationForm()
    content = PhysicalExamination.objects.filter(patient=Patient.objects.get(patient_id=pk))
    return render(request, "basic_app/patient_physical_examination.html", {"physical_form":physical_form, "physical_examination":content})

def HistoryFormCreateView(request,pk):
    if request.method == "POST":
        form = HistoryCreateForm(request.POST)
        if form.is_valid():
            p = Patient.objects.get(patient_id=pk)
            chief_complaints = form.cleaned_data.get('chief_complaints')
            past_history = form.cleaned_data.get('past_history')
            treatment_history = form.cleaned_data.get('treatment_history')
            menstrual = form.cleaned_data.get('menstrual')
            obsteric_histroy = form.cleaned_data.get('obsteric_histroy')
            h = HistoryForm.objects.filter(patient=p)
            hf_g = form.cleaned_data.get('g')
            hf_p = form.cleaned_data.get('p')
            hf_a = form.cleaned_data.get('a')
            hf_l = form.cleaned_data.get('l')
            if h.exists():
                h = h[0]
                existing_chief_complaints = h.chief_complaints.all()
                existing_past_history = h.past_history.all()
                existing_treatment_history = h.treatment_history.all()
                existing_menstrual = h.menstrual.all()
                existing_obstreic_history = h.obsteric_histroy.all()
                for i in existing_chief_complaints.iterator():
                    h.chief_complaints.remove(i)
                for i in existing_past_history.iterator():
                    h.past_history.remove(i)
                for i in existing_treatment_history.iterator():
                    h.treatment_history.remove(i)
                for i in existing_menstrual.iterator():
                    h.menstrual.remove(i)
                for i in existing_obstreic_history.iterator():
                    h.obsteric_histroy.remove(i)

                for i in chief_complaints.iterator():
                    h.chief_complaints.add(i)
                for i in past_history.iterator():
                    h.past_history.add(i)
                for i in treatment_history.iterator():
                    h.treatment_history.add(i)
                for i in menstrual.iterator():
                    h.menstrual.add(i)
                for i in obsteric_histroy.iterator():
                    h.obsteric_histroy.add(i)
                h.g,h.p,h.a,h.l = hf_g,hf_p,hf_a,hf_l
                h.save()
            else:
                h = HistoryForm.objects.create(patient=p)
                for i in chief_complaints.iterator():
                    h.chief_complaints.add(i)
                for i in past_history.iterator():
                    h.past_history.add(i)
                for i in treatment_history.iterator():
                    h.treatment_history.add(i)
                for i in menstrual.iterator():
                    h.menstrual.add(i)
                for i in obsteric_histroy.iterator():
                    h.obsteric_histroy.add(i)
                h.g,h.p,h.a,h.l = hf_g,hf_p,hf_a,hf_l
                h.save()
            return redirect(f'/patient/{p.patient_id}')
    else:
        form = HistoryCreateForm()
        h = HistoryForm.objects.filter(patient=Patient.objects.get(patient_id=pk))
        if h.exists():
            return redirect('update_history')
        else:
            text = "Create Patient History"
        print(text)
        return render(request, "basic_app/historyform_form.html", {"form":form,"text":text})


def TetanusImmunisationCreateView(request,pk):
    if request.method == "POST":
        form = TetanusImmunisationCreateForm(request.POST)
        if form.is_valid():
            p = Patient.objects.get(patient_id=pk)
            date_tt1 = request.POST.get('date_tt1')
            if date_tt1 == '':
                date_tt1 = None
            date_tt2 = request.POST.get('date_tt2')
            if date_tt2 == '':
                date_tt2 = None
            h = TetanusImmunisation.objects.filter(patient=p)
            if h.exists():
                h = h[0]
                h.date_tt1=date_tt1,
                h.date_tt2=date_tt2
                h.save()
            else:
                h = TetanusImmunisation.objects.create(
                    patient=p,
                    date_tt1=date_tt1,
                    date_tt2=date_tt2
                )
                h.save()
            return redirect(f'/patient/{p.patient_id}')
        else:
            date_tt1 = request.POST.get('date_tt1')
            date_tt2 = request.POST.get('date_tt2')
            x = form.errors
            for i in x:
                print(i)
                print(form.errors)
            return HttpResponse(form.errors)
    else:
        form = TetanusImmunisationCreateForm()
        h = TetanusImmunisation.objects.filter(patient=Patient.objects.get(patient_id=pk))
        if h.exists():
            return redirect('update_tetanus_immunisation')
        else:
            pass
        return render(request, "basic_app/tetanusimmunisation_form.html", {"form":form})


@csrf_exempt
def CreatePrescription(request,pk):
    if request.method == "GET":
        patient_details = Patient.objects.get(patient_id=pk)
        hf = HistoryForm.objects.get(patient=patient_details)
        pr = PreviousReport.objects.filter(patient=patient_details).order_by('-created_at')
        form = PrescriptionCreateForm()
        ddt_form = DrugDosageTimeForm()
        context = {"form":form,
                    "ddt_form":ddt_form,
                    "patient":patient_details,
                    "history":hf,
                    "previous_reports":pr
                    }
        return render(request, "basic_app/patient_prescription.html", context)
    if request.method == "POST":
        global new_ddt
        diag = request.POST.get('diagnosis')
        diag = diag.split('<opt>')
        diag.pop()
        invest = request.POST.get('investigation')
        invest = invest.split('<opt>')
        invest.pop()
        precaut = request.POST.get('precaution')
        precaut = precaut.split('<opt>')
        precaut.pop()
        # drug = request.POST.get('drug')
        # dosage = request.POST.get('dosage')
        # time = request.POST.get('time')

        follow_up = request.POST.get("follow_up")
        comment = request.POST.get("comment")
        prescription = Prescription(
            # prescription_id=len(Prescription.objects.all())+1,
            patient=Patient.objects.get(patient_id=pk),
            follow_up=follow_up,
            comment=comment,
        )
        prescription.save()
        for i in diag:
            d = Diagnosis.objects.get(name=i)
            prescription.diagnosis.add(d)
        for invest in invest:
            d = Investigation.objects.get(name=invest)
            prescription.investigation.add(d)
        for precaut in precaut:
            d = Precaution.objects.get(name=precaut)
            prescription.precaution.add(d)
        prescription.save()
        # old_ddts = DrugDosageTime.objects.all()
        # for i in old_ddts.iterator():
        #     i.delete()
        # for i in new_ddt:
        #     i.save()
        # ddt = DrugDosageTime(
        #     patient=Patient.objects.get(patient_id=pk),
        #     drug=Drug.objects.get(name=drug),
        #     dosage=Dosage.objects.get(name=dosage),
        #     time=Time.objects.get(name=time)
        # )
        # ddt.save()
        p = Patient.objects.get(patient_id=pk)
        new_ddt = []
        return HttpResponse("created")

@csrf_exempt
def createDDT(request,pk):
    global new_ddt
    if request.method == 'POST':
        drug = request.POST.get('drug')
        dosage = request.POST.get('dosage')
        time = request.POST.get('time')
        ddt = DrugDosageTime(
            patient=Patient.objects.get(patient_id=pk),
            drug=Drug.objects.get(name=drug),
            dosage=Dosage.objects.get(name=dosage),
            time=Time.objects.get(name=time)
        )
        print(drug, dosage, time)
        ddt.save()
        new_ddt.append(ddt)
        return HttpResponse('added')
    else:
        return redirect('/')

@csrf_exempt
def createDDTDischarge(request,pk):
    global new_ddt_dis
    if request.method == 'POST':
        drug = request.POST.get('drug')
        dosage = request.POST.get('dosage')
        time = request.POST.get('time')
        ddt_dis = DrugDosageTimeDischarge(
            patient=Patient.objects.get(patient_id=pk),
            drug=Drug.objects.get(name=drug),
            dosage=Dosage.objects.get(name=dosage),
            time=Time.objects.get(name=time)
        )
        print(drug, dosage, time)
        ddt_dis.save()
        new_ddt_dis.append(ddt_dis)
        return HttpResponse('added')
    else:
        return redirect('/')

def ViewPrescription(request,pk):
    patient_details = Patient.objects.get(patient_id=pk)
    # hf = HistoryForm.objects.get(patient=patient_details)
    # pr = PreviousReport.objects.filter(patient=patient_details).order_by('-created_at')
    prescription = Prescription.objects.filter(patient=patient_details).order_by('-created_at')[0]
    ddt = DrugDosageTime.objects.filter(prescription=prescription)
    context = {
                "patient":patient_details,
                # "history":hf,
                # "previous_reports":pr,
                "ddt":ddt,
                "prescription":prescription
            }
    return  render(request, "basic_app/patient_prescription_view.html", context)
    # pdf = render_to_pdf('basic_app/patient_prescription_view.html', context)
    # if pdf:
    #         response = HttpResponse(pdf, content_type='application/pdf')
    #         # filename = f"Prescription_{patient_details.name}.pdf"
    #         # content = f"inline; filename={filename}"
    #         # download = request.GET.get("download")
    #         # if download:
    #         #     content = f"attachment; filename={filename}"
    #         # response['Content-Disposition'] = content
    #         return response
    # return HttpResponse("PDF Not Found")

@csrf_exempt
def CreateDischargeSummary(request,pk):
    if request.method == "GET":
        patient_details = Patient.objects.get(patient_id=pk)
        form_dis = DischargeSummaryCreateForm()
        ddt_form_dis = DrugDosageTimeDischargeForm()
        context = {"form_dis":form_dis,
                    "ddt_form_dis":ddt_form_dis,
                    "patient":patient_details,
                    }
        return render(request, "basic_app/patient_discharge_summary.html", context)
    if request.method == "POST":
        global new_ddt_dis
        husband_name = request.POST.get('husband_name')

        doa = request.POST.get('doa')
        if doa == '':
            doa = None
        dod = request.POST.get('dod')
        if dod == '':
            dod = None
        diagnosis = request.POST.get('diagnosis')
        procedure = request.POST.get('procedure')
        per_op = request.POST.get('per_op')
        baby_details = request.POST.get('baby_details')
        hospital_stay = request.POST.get('hospital_stay')
        advice_on_discharge = request.POST.get('advice_on_discharge')

        drug = request.POST.get('drug')
        dosage = request.POST.get('dosage')
        time = request.POST.get('time')

        precaut = request.POST.get('precaution')
        precaut = precaut.split('<opt>')
        precaut.pop()

        follow_up = request.POST.get('follow_up')
        comment = request.POST.get('comment')
        discharge_summary = DischargeSummary(
            # discharge_id=len(DischargeSummary.objects.all())+1,
            patient=Patient.objects.get(patient_id=pk),
            husband_name=husband_name,
            doa=doa,
            dod=dod,
            diagnosis=diagnosis,
            procedure=procedure,
            per_op=per_op,
            baby_details=baby_details,
            hospital_stay=hospital_stay,
            advice_on_discharge = advice_on_discharge,
            follow_up=follow_up,
            comment=comment,
        )
        discharge_summary.save()

        for precaut in precaut:
            d = Precaution.objects.get(name=precaut)
            discharge_summary.precaution.add(d)
        discharge_summary.save()
        old_ddts = DrugDosageTimeDischarge.objects.all()
        for i in old_ddts.iterator():
            i.delete()
        for i in new_ddt_dis:
            i.save()
        ddt_dis = DrugDosageTimeDischarge(
            patient=Patient.objects.get(patient_id=pk),
            drug=Drug.objects.get(name=drug),
            dosage=Dosage.objects.get(name=dosage),
            time=Time.objects.get(name=time)
        )
        ddt_dis.save()
        p = Patient.objects.get(patient_id=pk)
        new_ddt_dis = []
        return HttpResponse("created")

def ViewDischargeSummary(request,pk):
    patient_details = Patient.objects.get(patient_id=pk)
    # hf = HistoryForm.objects.get(patient=patient_details)
    # pr = PreviousReport.objects.filter(patient=patient_details).order_by('-created_at')
    discharge_summary = DischargeSummary.objects.filter(patient=patient_details).order_by('-created_at')[0]
    ddt = DrugDosageTimeDischarge.objects.filter(discharge_summary=discharge_summary)
    context = {
                "patient":patient_details,
                "ddt":ddt,
                "discharge":discharge_summary
            }
    return  render(request, "basic_app/discharge_summary_view.html", context)
    # pdf = render_to_pdf('basic_app/discharge_summary_view.html', context)
    # if pdf:
    #         response = HttpResponse(pdf, content_type='application/pdf')
    #         # filename = f"Prescription_{patient_details.name}.pdf"
    #         # content = f"inline; filename={filename}"
    #         # download = request.GET.get("download")
    #         # if download:
    #         #     content = f"attachment; filename={filename}"
    #         # response['Content-Disposition'] = content
    #         return response
    # return HttpResponse("PDF Not Found")

class HistoryFormUpdateView(UpdateView):
    model = HistoryForm
    template_name = 'basic_app/historyform_form.html'

    fields = ["chief_complaints","past_history","treatment_history","menstrual","obsteric_histroy","g","p","a","l"]

    def get_success_url(self):
            return reverse('basic_app:detail', kwargs={'pk': self.object.id})


class TetanusImmunisationUpdateView(UpdateView):
    model = TetanusImmunisation
    template_name = 'basic_app/tetanusimmunisation_form.html'
    fields = ["date_tt1","date_tt2"]
    def get_success_url(self):
            return reverse('basic_app:detail', kwargs={'pk': self.object.id})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class ViewAllPrescription(ListView):
    model = Prescription

    def get_queryset(self, *args, **kwargs):
        qs = Prescription.objects.filter(patient=Patient.objects.get(patient_id=self.kwargs['pk']))
        qs = qs.order_by("-created_at")
        return qs

class PrescriptionDetail(DetailView):
    model = Prescription

    def get_context_data(self, *args, **kwargs):
        context = super(PrescriptionDetail, self).get_context_data(*args, **kwargs)
        p = Patient.objects.get(patient_id=self.kwargs['pk'])
        context['patient'] = Patient.objects.get(patient_id=p.patient_id)
        context['history'] = HistoryForm.objects.get(patient=p)
        context['previous_reports'] = PreviousReport.objects.filter(patient=p).order_by('-created_at')
        context['ddt'] = DrugDosageTime.objects.filter(patient=p)
        return context


class DischargeSummaryDetail(DetailView):
    model = DischargeSummary

    def get_context_data(self, *args, **kwargs):
        context = super(DischargeSummaryDetail, self).get_context_data(*args, **kwargs)
        p = Patient.objects.get(patient_id=self.kwargs['pk'])
        context['patient'] = Patient.objects.get(patient_id=p.patient_id)
        context['ddt_dis'] = DrugDosageTimeDischarge.objects.filter(patient=p)
        return context
