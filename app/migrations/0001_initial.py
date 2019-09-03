# Generated by Django 2.2.5 on 2019-09-03 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=100, verbose_name='Origem')),
                ('destiny', models.CharField(max_length=100, verbose_name='Destino')),
                ('date', models.CharField(max_length=100, verbose_name='Data')),
                ('hour', models.CharField(max_length=100, verbose_name='Hora')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.IntegerField(verbose_name='Número da poltrona')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to=settings.AUTH_USER_MODEL, verbose_name='Passageiro')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='app.Travel', verbose_name='Viagem')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships', to=settings.AUTH_USER_MODEL, verbose_name='Passageiro 1')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL, verbose_name='Passageiro 2')),
            ],
        ),
    ]