# Generated by Django 3.0.3 on 2020-02-22 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpsls', '0006_auto_20200222_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='rpsls.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='oponent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oponent', to='rpsls.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='rpsls.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nick_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Ápodo'),
        ),
        migrations.DeleteModel(
            name='ResultGame',
        ),
    ]