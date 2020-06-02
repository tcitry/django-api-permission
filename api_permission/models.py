from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class APIPermissionModel(models.Model):
    POST = 'POST'
    GET = 'GET'
    ALL = 'ALL'
    METHODS = (
        (POST, _("create/edit/delete")),
        (GET, _("readonly")),
        (ALL, _("all")),
    )

    pattern = models.CharField(_("api pattern"), max_length=128)
    method = models.CharField(_("method"), max_length=16, choices=METHODS)
    active = models.BooleanField(_("is Active"), default=True)
    group = models.ManyToManyField(Group, db_constraint=True, verbose_name=_("group"),
                                   related_name='api_permissions')
    comment = models.CharField(_("comment"), max_length=256, blank=True, null=True)

    created_at = models.DateTimeField(_("created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("updated"), auto_now=True, null=True)

    class Meta:
        db_table = 'api_permission'
        verbose_name = _('API Permission')
        verbose_name_plural = _('API Permissions')
