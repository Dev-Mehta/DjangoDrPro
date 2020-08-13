# Generated by Django 3.0.3 on 2020-08-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20200812_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyform',
            name='a',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='chief_complaints',
            field=models.ManyToManyField(blank=True, null=True, to='basic_app.ChiefComplaint'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='g',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='l',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='menstrual',
            field=models.ManyToManyField(blank=True, null=True, to='basic_app.Menstrual'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='obsteric_histroy',
            field=models.ManyToManyField(blank=True, null=True, to='basic_app.ObstericHistroy'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='p',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='past_history',
            field=models.ManyToManyField(blank=True, null=True, to='basic_app.PastHistory'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='treatment_history',
            field=models.ManyToManyField(blank=True, null=True, to='basic_app.TreatmentHistory'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='blood_group_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='bs_f_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='bs_pp_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='bt_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='chest_x_ray_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='ct_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='ecg_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hb_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hbs_ag',
            field=models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('neutral', 'Neutral')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hbs_ag_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hcv',
            field=models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('neutral', 'Neutral')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hcv_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hiv',
            field=models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('neutral', 'Neutral')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='hiv_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='mri_ct_scan_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='platelet_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='s_tsh_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='ur_m_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='usg_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='vdrl',
            field=models.CharField(blank=True, choices=[('+ve', '+ve'), ('-ve', '-ve'), ('neutral', 'Neutral')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='previousreport',
            name='vdrl_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tetanusimmunisation',
            name='date_tt1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tetanusimmunisation',
            name='date_tt2',
            field=models.DateField(blank=True, null=True),
        ),
    ]