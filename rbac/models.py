from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


class Role(models.Model):
    '''
    角色模型
    - `name: Char` 角色名称
    - `status: Boolean` 角色状态
    - `permissions: M2M` 角色权限
    '''
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    '''
    自定义用户模型，继承`AbstractUser`
    - `gender: MEN|WOMEN` 性别
    - `roles: M2M` 角色集
    '''
    class Gender(models.IntegerChoices):
        MEN = 1
        WOMEN = 0

    gender = models.IntegerField(choices=Gender.choices)
    roles = models.ManyToManyField(Role, blank=True,)
