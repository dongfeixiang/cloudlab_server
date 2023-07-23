from django.db.models import Avg

from .models import *
from .serializer import *
from utils.response import APIModelViewSet


class PlasmidView(APIModelViewSet):
    queryset = Plasmid.objects.all()
    serializer_class = PlasmidSerializer


class ProteinView(APIModelViewSet):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer


class CellLineView(APIModelViewSet):
    queryset = CellLine.objects.all()
    serializer_class = CellLineSerializer
