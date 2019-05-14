# Generated by Django 2.2.1 on 2019-05-13 16:27

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('opening_hours', models.TextField(null=True)),
                ('contact_information', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GymImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='gym/')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.Gym')),
            ],
        ),
    ]