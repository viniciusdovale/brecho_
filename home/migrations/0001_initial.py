# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=b'User Id')),
                ('user_nick', models.CharField(max_length=20, verbose_name=b'User Nick')),
                ('imagem', models.CharField(max_length=10, null=True, verbose_name=b'Imagem', blank=True)),
                ('estado', models.CharField(max_length=100, null=True, verbose_name=b'Estado', blank=True)),
                ('cidade', models.CharField(max_length=200, null=True, verbose_name=b'Cidade', blank=True)),
                ('altura', models.CharField(max_length=10, null=True, verbose_name=b'Altura', blank=True)),
                ('cintura', models.CharField(max_length=10, null=True, verbose_name=b'Cintura', blank=True)),
                ('calcado', models.CharField(max_length=200, null=True, verbose_name=b'Calcado', blank=True)),
                ('celular', models.CharField(max_length=200, null=True, verbose_name=b'Celular', blank=True)),
                ('whatsapp', models.CharField(max_length=12, null=True, verbose_name=b'Whatsapp', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name=b'Email', blank=True)),
                ('facebook', models.CharField(max_length=200, null=True, verbose_name=b'Facebook', blank=True)),
                ('instagram', models.CharField(max_length=200, null=True, verbose_name=b'Instagram', blank=True)),
                ('user_premium', models.CharField(max_length=200, null=True, verbose_name=b'User_premium', blank=True)),
                ('data_expiracao_premium', models.DateField(max_length=50, null=True, verbose_name=b'Data Expire', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
