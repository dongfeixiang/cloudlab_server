from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField

from .models import Plasmid, Protein, CellLine


class PlasmidSerializer(ModelSerializer):
    sequence = CharField(required=False)

    class Meta:
        model = Plasmid
        fields = [
            "id", "name", "parent", "concentration", "sequence"
        ]


class CellLineSerializer(ModelSerializer):
    plasmids = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CellLine
        fields = [
            "id", "name", "parent", "density",
            "_plasmids", "plasmids"
        ]
        extra_kwargs = {
            "_plasmids": {"write_only": True},
            "plasmids": {"read_only": True}
        }


class ProteinSerializer(ModelSerializer):
    host = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Protein
        fields = [
            "id", "name", "parent", "concentration",
            "_host", "host", "mw", "pi", "exco"
        ]
        read_only_fields = ["mw", "pi", "exco"]
        extra_kwargs = {
            "_host": {"write_only": True},
            "host": {"read_only": True}
        }
