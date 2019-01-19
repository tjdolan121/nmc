# Generated by Django 2.1.5 on 2019-01-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poc', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low')], default='Normal', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NetworkBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_status', models.CharField(choices=[('FMC', 'FMC'), ('PMC', 'PMC'), ('NMC', 'NMC'), ('ASI', 'ASI')], max_length=3)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('FMC', 'FMC'), ('PMC', 'PMC'), ('NMC', 'NMC'), ('ASI', 'ASI')], max_length=3)),
                ('more_info', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='')),
                ('favorites', models.ManyToManyField(blank=True, related_name='_unit_favorites_+', to='netdash.Unit')),
            ],
        ),
    ]
