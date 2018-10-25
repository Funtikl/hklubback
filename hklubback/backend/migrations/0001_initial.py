# Generated by Django 2.1.2 on 2018-10-23 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inneed_people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_az', models.TextField()),
                ('name_ru', models.TextField()),
                ('name_eng', models.TextField()),
                ('story_az', models.TextField()),
                ('story_ru', models.TextField()),
                ('story_eng', models.TextField()),
                ('photo', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('money_stat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts_az',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('photo', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('Inneed_people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Inneed_people')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('group_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users_Inneed_People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Inneed_people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Inneed_people')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Users')),
            ],
        ),
    ]