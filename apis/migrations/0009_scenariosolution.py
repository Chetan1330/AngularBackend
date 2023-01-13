# Generated by Django 4.1.5 on 2023-01-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_scenariouser_alter_scenario_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainingdata', models.FileField(blank=True, upload_to='files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenariosolution', to='apis.scenariouser')),
            ],
        ),
    ]