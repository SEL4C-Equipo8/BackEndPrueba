# Generated by Django 4.2.5 on 2023-09-27 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SEL4c_app', '0002_alter_modulos_instrucciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadisticas',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.usuario'),
        ),
        migrations.AlterField(
            model_name='evidenciamodulos',
            name='id_modulo',
            field=models.OneToOneField(db_column='id_modulo', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.modulos'),
        ),
        migrations.AlterField(
            model_name='modulos',
            name='id_actividad',
            field=models.ForeignKey(db_column='id_actividad', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.actividades'),
        ),
        migrations.AlterField(
            model_name='progresoactividades',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.usuario'),
        ),
        migrations.AlterField(
            model_name='progresousuarios',
            name='id_actividad',
            field=models.ForeignKey(db_column='id_actividad', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.actividades'),
        ),
        migrations.AlterField(
            model_name='progresousuarios',
            name='id_modulo',
            field=models.ForeignKey(db_column='id_modulo', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.modulos'),
        ),
        migrations.AlterField(
            model_name='progresousuarios',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='SEL4c_app.usuario'),
        ),
    ]
