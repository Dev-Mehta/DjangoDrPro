# Generated by Django 3.0.3 on 2020-08-11 18:05

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChiefComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DrugDosageTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('dosage', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basic_app.Dosage')),
                ('drug', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basic_app.Drug')),
            ],
            options={
                'db_table': 'DrugDosageTime',
            },
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Menstrual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ObstericHistroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PastHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.CharField(blank=True, default='', max_length=256)),
                ('mobile', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='PostiveNegative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Precaution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TetanusImmunisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_tt1', models.DateField(blank=True)),
                ('date_tt2', models.DateField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Patient')),
            ],
            options={
                'db_table': 'TetanusImmunisation',
            },
        ),
        migrations.CreateModel(
            name='PreviousReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hb', models.CharField(blank=True, default='', max_length=256)),
                ('platelet', models.CharField(blank=True, default='', max_length=256)),
                ('bt', models.CharField(blank=True, default='', max_length=256)),
                ('ct', models.CharField(blank=True, default='', max_length=256)),
                ('bs_f', models.CharField(blank=True, default='', max_length=256)),
                ('bs_pp', models.CharField(blank=True, default='', max_length=256)),
                ('ur_m', models.CharField(blank=True, default='', max_length=256)),
                ('s_tsh', models.CharField(blank=True, default='', max_length=256)),
                ('usg', models.CharField(blank=True, default='', max_length=256)),
                ('mri_ct_scan', models.CharField(blank=True, default='', max_length=256)),
                ('ecg', models.CharField(blank=True, default='', max_length=256)),
                ('chest_x_ray', models.CharField(blank=True, default='', max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('hbs_ag', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hbs_ag', to='basic_app.PostiveNegative')),
                ('hcv', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hcv', to='basic_app.PostiveNegative')),
                ('hiv', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hiv', to='basic_app.PostiveNegative')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Patient')),
                ('vdrl', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vdrl', to='basic_app.PostiveNegative')),
            ],
            options={
                'db_table': 'PreviousReport',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('follow_up', models.CharField(blank=True, default='', max_length=256)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnosis', models.ManyToManyField(to='basic_app.Diagnosis')),
                ('drug_dostage_time', models.ManyToManyField(to='basic_app.DrugDosageTime')),
                ('investigation', models.ManyToManyField(to='basic_app.Investigation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Patient')),
                ('precaution', models.ManyToManyField(to='basic_app.Precaution')),
            ],
            options={
                'db_table': 'Prescription',
            },
        ),
        migrations.CreateModel(
            name='PhysicalExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('bp', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('wt', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('ht', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('uterus_funal_ht', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('presentation', models.CharField(blank=True, default='', max_length=256)),
                ('fms', models.DecimalField(blank=True, decimal_places=3, default=Decimal('0'), max_digits=15)),
                ('per_vaginum', models.CharField(blank=True, default='', max_length=256)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Patient')),
            ],
            options={
                'db_table': 'PhysicalExamination',
            },
        ),
        migrations.CreateModel(
            name='HistoryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g', models.CharField(max_length=50)),
                ('p', models.CharField(max_length=50)),
                ('a', models.CharField(max_length=50)),
                ('l', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('chief_complaints', models.ManyToManyField(to='basic_app.ChiefComplaint')),
                ('menstrual', models.ManyToManyField(to='basic_app.Menstrual')),
                ('obsteric_histroy', models.ManyToManyField(to='basic_app.ObstericHistroy')),
                ('past_history', models.ManyToManyField(to='basic_app.PastHistory')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='historyforms', to='basic_app.Patient')),
                ('treatment_history', models.ManyToManyField(to='basic_app.TreatmentHistory')),
            ],
            options={
                'db_table': 'HistoryForm',
            },
        ),
        migrations.AddField(
            model_name='drugdosagetime',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Patient'),
        ),
        migrations.AddField(
            model_name='drugdosagetime',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basic_app.Time'),
        ),
    ]