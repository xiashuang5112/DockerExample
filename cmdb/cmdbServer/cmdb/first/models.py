#coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Configure(models.Model):
    """
    发布系统动态配置
    """
    name = models.CharField(verbose_name=u'配置项名', max_length=128, help_text=u'配置项名')
    alias = models.CharField(verbose_name=u'配置项中文名', max_length=128, help_text=u'配置项中文名')
    active = models.BooleanField(verbose_name=u'是否启用', default=True, help_text=u'是否启用')
    params = models.TextField(verbose_name=u'配置附加值', default='', help_text=u'配置附加值')
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, help_text=u'创建时间')
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, help_text=u'更新时间')

    class Meta:
        verbose_name = u'全局配置表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


