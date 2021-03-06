# Generated by Django 3.0.6 on 2020-06-04 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('api_permission', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apipermissionmodel',
            options={'verbose_name': 'API Permission', 'verbose_name_plural': 'API Permissions'},
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='active',
            field=models.BooleanField(default=True, verbose_name='is Active'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='group',
            field=models.ManyToManyField(related_name='api_permissions', to='auth.Group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='method',
            field=models.CharField(choices=[('POST', 'create/edit/delete'), ('GET', 'readonly'), ('ALL', 'all')], max_length=16, verbose_name='method'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='pattern',
            field=models.CharField(max_length=128, verbose_name='api pattern'),
        ),
        migrations.AlterField(
            model_name='apipermissionmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated'),
        ),
    ]
