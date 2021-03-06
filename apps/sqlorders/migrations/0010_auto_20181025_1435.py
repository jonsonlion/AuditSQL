# Generated by Django 2.1.2 on 2018-10-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0009_auto_20181019_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sqlordersexectasks',
            name='backup_dbname',
        ),
        migrations.RemoveField(
            model_name='sqlordersexectasks',
            name='rollback_sqlsha1',
        ),
        migrations.RemoveField(
            model_name='sqlordersexectasks',
            name='sequence',
        ),
        migrations.RemoveField(
            model_name='sqlordersexectasks',
            name='sqlsha1',
        ),
        migrations.AddField(
            model_name='sqlordersexectasks',
            name='rollback_sql',
            field=models.TextField(default='', verbose_name='回滚的SQL'),
        ),
        migrations.AlterField(
            model_name='sqlordersexectasks',
            name='affected_row',
            field=models.IntegerField(default=0, verbose_name='影响行数'),
        ),
    ]
