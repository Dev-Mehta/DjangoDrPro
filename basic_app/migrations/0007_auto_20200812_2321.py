# Generated by Django 3.0.3 on 2020-08-12 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20200812_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='previousreport',
            name='blood_group_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='bs_f_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='bs_pp_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='bt_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='chest_x_ray_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='ct_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='ecg_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='hb_date',
            field=models.DateField(blank=True, default='2020-08-08'),
        ),
        migrations.AddField(
            model_name='previousreport',
            name='hbs_ag_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='hcv_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='hiv_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='mri_ct_scan_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='platelet_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='s_tsh_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='ur_m_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='usg_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='previousreport',
            name='vdrl_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historyform',
            name='chief_complaints',
            field=models.ManyToManyField(blank=True, to='basic_app.ChiefComplaint'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='menstrual',
            field=models.ManyToManyField(blank=True, to='basic_app.Menstrual'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='obsteric_histroy',
            field=models.ManyToManyField(blank=True, to='basic_app.ObstericHistroy'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='past_history',
            field=models.ManyToManyField(blank=True, to='basic_app.PastHistory'),
        ),
        migrations.AlterField(
            model_name='historyform',
            name='treatment_history',
            field=models.ManyToManyField(blank=True, to='basic_app.TreatmentHistory'),
        ),
    ]