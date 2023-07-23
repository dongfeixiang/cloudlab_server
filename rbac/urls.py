from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *


rbac_router = SimpleRouter()
rbac_router.register(r"user", UserView)
rbac_router.register(r"role", RoleView)
rbac_router.register(r"permission", PermissionView)

urlpatterns = [
    path("", include(rbac_router.urls)),
    path("token/", JwtView.as_view()),
    path("token/refresh/", JwtRefreshView.as_view())
]
