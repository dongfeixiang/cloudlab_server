from django.db import models


class AbstractSample(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get(self, attr):
        if self.parent:
            return self.parent.get(attr)
        else:
            return getattr(self, attr)


class Plasmid(AbstractSample):
    concentration = models.FloatField()
    _sequence = models.TextField(blank=True)

    @property
    def sequence(self):
        return self.get("_sequence")

    @sequence.setter
    def sequence(self, value):
        self._sequence = value


class CellLine(AbstractSample):
    density = models.DecimalField(max_digits=12, decimal_places=2)
    _plasmids = models.ManyToManyField(Plasmid, blank=True)

    @property
    def plasmids(self):
        return self.get("_plasmids")


class Protein(AbstractSample):
    concentration = models.FloatField()
    _host = models.ForeignKey(
        CellLine,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    @property
    def host(self):
        return self.get("_host")

    @property
    def mw(self):
        '''分子量 (Da)'''
        MR = {"A": 89.09, "C": 121.16, "D": 133.10, "E": 147.13, "F": 165.19,
              "G": 75.07, "H": 155.16, "I": 131.17, "K": 146.19, "L": 131.17,
              "M": 149.21, "N": 132.12, "P": 115.13, "Q": 146.15, "R": 174.20,
              "S": 105.09, "T":	119.16, "V": 117.15, "W": 204.22, "Y": 181.19}
        ret = 0
        for p in self.host.plasmids.all():
            for aa in p.sequence:
                ret += MR[aa]
            ret -= 18
        return ret

    @property
    def pi(self):
        '''等电点'''
        ret = 8.0
        return ret

    @property
    def exco(self):
        '''消光系数 (L/g)'''
        EP = {"W": 5500, "Y": 1490, "C": 125}
        epsilon = 0
        for p in self.host.plasmids.all():
            for aa in p.sequence:
                if aa in EP:
                    epsilon += EP[aa]
        return epsilon/self.mw
