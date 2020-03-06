# Generated by Django 3.0.3 on 2020-03-06 00:22

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', django_extensions.db.fields.ShortUUIDField(blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nome', models.TextField(blank=True, default='Sem identificação', null=True)),
                ('pos_x', models.PositiveIntegerField()),
                ('pos_y', models.PositiveIntegerField()),
                ('hor_abertura', models.TimeField(blank=True, null=True)),
                ('hor_fechamento', models.TimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]
