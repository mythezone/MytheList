# Generated by Django 5.1 on 2024-08-14 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_user_create_at_user_update_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "用户信息", "verbose_name_plural": "用户信息"},
        ),
    ]
