#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin

''' Key-Value Configuration Model '''

from django.db import models
from django.utils.translation import ugettext as _


class Configuration(models.Model):

    ''' Key-Value Configuration Model '''

    key = models.CharField(_(u"Key"), max_length=50, db_index=True)
    value = models.CharField(_(u"Value"), max_length=255)
    description = models.CharField(_(u"Description"), max_length=255)

    class Meta:
        unique_together = ('key', 'value')

    def __unicode__(self):
        return u"%(key)s: %(value)s" % {'key': self.key, 'value': self.value}

    @classmethod
    def get(cls, key=None, value=None):
        ''' get config value of specified key '''
        try:
            cfg = cls.objects.get(key=key)
            return cfg.value
        except cls.DoesNotExist:
            if value:
                return value
            raise
