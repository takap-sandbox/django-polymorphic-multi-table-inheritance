# Generated by Django 5.1.6 on 2025-02-10 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hobbyplan",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="plan",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="proplan",
            options={"base_manager_name": "objects"},
        ),
        migrations.AddField(
            model_name="plan",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="proplan",
            name="pro_rate",
            field=models.IntegerField(default=100),
        ),
    ]
