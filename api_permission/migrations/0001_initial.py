from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIPermissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=128, verbose_name='API正则')),
                ('method', models.CharField(choices=[('POST', '创建/编辑/删除'), ('GET', '查看'), ('ALL', '所有')], max_length=16, verbose_name='方法类型')),
                ('active', models.BooleanField(default=True, verbose_name='是否生效')),
                ('comment', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('group', models.ManyToManyField(related_name='api_permissions', to='auth.Group', verbose_name='组/角色')),
            ],
            options={
                'verbose_name': 'API 权限',
                'verbose_name_plural': 'API 权限列表',
                'db_table': 'api_permission',
            },
        ),
    ]
