from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import *
from .serializer import *
from utils.response import APIResponse, APIModelViewSet


class JwtView(TokenObtainPairView):
    '''
    获取Token接口
    '''

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return APIResponse(code="100", msg="success", data=response.data)


class JwtRefreshView(TokenRefreshView):
    '''
    刷新Token接口
    '''

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return APIResponse(code="100", msg="success", data=response.data)


class UserView(APIModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleView(APIModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PermissionView(APIModelViewSet):
    queryset = Permission.objects.exclude(
        content_type__model__in=["logentry", "contenttype", "session"])
    serializer_class = PermissionSerializer
