from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User, Role


class UserSerializer(ModelSerializer):
    '''
    用户模型序列化器
    - `id: int` 用户ID
    - `username: str` 账号
    - `password: str` 密码【只写】
    - `email: str` 邮箱
    - `gender: int` 性别【0: 女, 1: 男】
    - `roles: list` 角色集
    '''
    roles = SlugRelatedField(
        slug_field="name",
        many=True,
        queryset=Role.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "gender", "roles"]
        # 密码只写
        # extra_kwargs = {"password": {"write_only": True}}

    def to_internal_value(self, data):
        '''
        Encodeing the `password` when created or updated
        '''
        ret = super().to_internal_value(data)
        if "password" in ret:
            ret["password"] = make_password(ret["password"])
        return ret


class RoleSerializer(ModelSerializer):
    '''
    角色模型序列化器
    - `id: int` 角色ID
    - `name: str` 角色名称
    - `permissions: list` 权限集
    '''
    permissions = SlugRelatedField(
        slug_field="codename",
        many=True,
        queryset=Permission.objects.exclude(
            content_type__model__in=["logentry", "contenttype", "session"])
    )

    class Meta:
        model = Role
        fields = ["id", "name", "permissions"]


class PermissionSerializer(ModelSerializer):
    '''
    权限模型序列化器
    - `id` 权限ID
    - `codename` 权限编码
    - `model` 关联模型
    '''
    model = SlugRelatedField(
        slug_field="model",
        read_only=True,
        source="content_type"
    )

    class Meta:
        model = Permission
        fields = ["id", "codename", "model"]
