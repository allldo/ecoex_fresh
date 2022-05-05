# Generated by Django 4.0.3 on 2022-05-05 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_alter_passdocs_file_pdf_2_alter_passdocs_file_pdf_3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='service_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.servicegroup'),
        ),
    ]
