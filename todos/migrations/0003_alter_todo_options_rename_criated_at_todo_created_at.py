# Generated by Django 5.0.1 on 2024-03-03 03:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_alter_todo_finalizado"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["deadline"]},
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="criated_at",
            new_name="created_at",
        ),
    ]