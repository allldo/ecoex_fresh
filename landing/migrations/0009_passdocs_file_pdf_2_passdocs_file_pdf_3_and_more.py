# Generated by Django 4.0.3 on 2022-04-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_passdocs'),
    ]

    operations = [
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_2',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_3',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_4',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_5',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_6',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_7',
            field=models.FileField(null=True, upload_to='docs'),
        ),
        migrations.AddField(
            model_name='passdocs',
            name='file_pdf_8',
            field=models.FileField(null=True, upload_to='docs'),
        ),
    ]
