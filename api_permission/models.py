from django.db import models
from django.contrib.auth.models import Group


class APIPermissionModel(models.Model):
    POST = 'POST'
    GET = 'GET'
    ALL = 'ALL'
    METHODS = (
        (POST, "创建/编辑/删除"),
        (GET, "查看"),
        (ALL, "所有"),
    )

    pattern = models.CharField("API正则", max_length=128)
    method = models.CharField("方法类型", max_length=16, choices=METHODS)
    active = models.BooleanField("是否生效", default=True)
    group = models.ManyToManyField(Group, db_constraint=True, verbose_name="组/角色",
                                   related_name='api_permissions')
    comment = models.CharField("备注", max_length=256, blank=True, null=True)

    created_at = models.DateTimeField("创建时间", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    class Meta:
        db_table = 'api_permission'
        verbose_name = 'API 权限'
        verbose_name_plural = 'API 权限列表'
