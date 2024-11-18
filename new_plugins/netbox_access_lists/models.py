# models.py
from django.db import models
from utilities.querysets import RestrictedQuerySet


class SpliceTray(models.Model):
    objects = RestrictedQuerySet.as_manager()

    name = models.CharField(max_length=100)
    location = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name='splice_trays'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        app_label = 'netbox_access_lists'

    def __str__(self):
        return self.name


class Coupler(models.Model):
    objects = RestrictedQuerySet.as_manager()

    name = models.CharField(max_length=50)
    type = models.PositiveSmallIntegerField(choices=[
        (1, 'FC'),
        (2, 'LC'),
        (3, 'SC')
    ])
    manufacturer = models.ForeignKey(to='dcim.Manufacturer', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        app_label = 'netbox_access_lists'

    def __str__(self):
        return f'{self.name} ({self.get_type_display()})'
        

