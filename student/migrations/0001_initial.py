# Generated by Django 4.2.1 on 2023-05-19 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('authMain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(related_name='user_course', to='course.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authMain.authmain')),
            ],
        ),
    ]
