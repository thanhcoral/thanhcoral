# Generated by Django 4.1.1 on 2022-09-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, choices=[('Associate Degree', 'Associate Degree'), ('Bachelor Degree', 'Bachelor Degree'), ('Specialist Degree', 'Specialist Degree'), ('Undergraduate Degrees', 'Undergraduate Degrees'), ('Professional Degree', 'Professional Degree'), ('Doctoral Degree', 'Doctoral Degree'), ('Professional Certificate', 'Professional Certificate'), ('Master Degree', 'Master Degree'), ('Transfer Degree', 'Transfer Degree'), ('Graduate Degrees', 'Graduate Degrees')], max_length=100, null=True, verbose_name='degree'),
        ),
    ]
