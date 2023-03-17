# Generated by Django 4.1.7 on 2023-03-17 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('histoiaclin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('identificacion', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('historia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='histoiaclin.histoiaclin')),
            ],
        ),
    ]