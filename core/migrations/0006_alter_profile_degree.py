# Generated by Django 4.1.1 on 2022-09-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_certificate_alter_profile_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, choices=[('Specialist Degree', 'Specialist Degree'), ('Bachelor Degree', 'Bachelor Degree'), ('Transfer Degree', 'Transfer Degree'), ('Professional Degree', 'Professional Degree'), ('Graduate Degrees', 'Graduate Degrees'), ('Associate Degree', 'Associate Degree'), ('Doctoral Degree', 'Doctoral Degree'), ('Professional Certificate', 'Professional Certificate'), ('Undergraduate Degrees', 'Undergraduate Degrees'), ('Master Degree', 'Master Degree')], max_length=100, null=True, verbose_name='degree'),
        ),
    ]
