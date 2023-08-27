from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

class McDomain(NetBoxModel):
    name = models.CharField(max_length=100)
    domain_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    devices = models.ManyToManyField(
        to='dcim.Device',
        related_name="mc_domains"
    )
    def __str__(self):
        return self.name

class McLag(NetBoxModel):
    name = models.CharField(max_length=100)
    lag_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    mc_domain = models.ForeignKey(
        to=McDomain,
        on_delete=models.CASCADE,
        related_name="mc_lags"
    )
    def __str__(self):
        return self.name