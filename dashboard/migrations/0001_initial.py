# Generated by Django 2.1.7 on 2019-07-11 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('vehicle', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=32)),
                ('destination', models.CharField(max_length=32)),
                ('ship_date', models.DateField()),
                ('budget', models.FloatField()),
                ('description', models.CharField(max_length=1024)),
                ('status', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transporters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='shippers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Shippers'),
        ),
        migrations.AddField(
            model_name='bids',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Jobs'),
        ),
        migrations.AddField(
            model_name='bids',
            name='transporters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Transporters'),
        ),
    ]