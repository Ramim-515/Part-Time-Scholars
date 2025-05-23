# Generated by Django 5.2 on 2025-05-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0009_area_district_remove_job_location_alter_job_job_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='area',
        ),
        migrations.RemoveField(
            model_name='job',
            name='district',
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('part-time', 'Part-Time'), ('remote', 'Remote'), ('internship', 'Internship')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
