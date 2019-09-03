import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser, Permission
from imagekit.models import ImageSpecField


class Travel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin = models.CharField(max_length=100, verbose_name = 'Origem')
    destiny = models.CharField(max_length=100, verbose_name = 'Destino')
    image = models.ImageField(upload_to='accounts/', verbose_name='Imagem')
    date = models.DateField(verbose_name = 'Data', auto_now=False)
    hour = models.TimeField(verbose_name = 'Hora', auto_now=False)

class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(verbose_name='Número da poltrona')
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name='Viagem', related_name = 'seats')
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Passageiro', related_name = 'seats')

class Friendship(models.Model):

    user1 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Passageiro 1', related_name='friendships')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Passageiro 2', related_name='friend')

# class UUIDUser (AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user_permissions = models.ManyToManyField(Permission, blank=True, related_name='uuiduser_set', related_query_name='user')

#     def __str__(self):
#         return self.username
