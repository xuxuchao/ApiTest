# Generated by Django 2.0 on 2018-05-11 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180511_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcaseresult',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TestCase', verbose_name='测试用例'),
        ),
    ]