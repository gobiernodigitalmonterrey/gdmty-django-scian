# Generated by Django 4.2.2 on 2024-02-13 00:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    def poblateSCIAN(apps, schema_editor):
        from django.core.management import call_command
        call_command('loaddata', '../fixtures/cat_scian.json')

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SCIAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tn_ancestors_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Ancestors pks')),
                ('tn_ancestors_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Ancestors count')),
                ('tn_children_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Children pks')),
                ('tn_children_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Children count')),
                ('tn_depth', models.PositiveIntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Depth')),
                ('tn_descendants_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Descendants pks')),
                ('tn_descendants_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Descendants count')),
                ('tn_index', models.PositiveIntegerField(default=0, editable=False, verbose_name='Index')),
                ('tn_level', models.PositiveIntegerField(default=1, editable=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Level')),
                ('tn_priority', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='Priority')),
                ('tn_order', models.PositiveIntegerField(default=0, editable=False, verbose_name='Order')),
                ('tn_siblings_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Siblings pks')),
                ('tn_siblings_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Siblings count')),
                ('nivel', models.CharField(choices=[('sector', 'Sector'), ('subsector', 'Subsector'), ('rama', 'Rama'), ('subrama', 'Subrama'), ('clase', 'Clase')], max_length=16)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('incluye', models.TextField(blank=True, null=True)),
                ('excluye', models.TextField(blank=True, null=True)),
                ('indice', models.TextField(blank=True, null=True)),
                ('tn_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tn_children', to='cat_scian.cat_scian', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Taxón',
                'verbose_name_plural': 'Taxonomía',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.RunPython(poblateSCIAN),
    ]