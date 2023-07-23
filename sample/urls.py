from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *


sample_router = SimpleRouter()
sample_router.register(r"plasmid", PlasmidView)
sample_router.register(r"protein", ProteinView)
sample_router.register(r"cellline", CellLineView)

urlpatterns = [
    path("", include(sample_router.urls)),
]
