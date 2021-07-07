# Generated by Django 2.2.6 on 2019-10-04 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('register_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('register_date', models.DateField(blank=True)),
                ('complain', models.TextField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
