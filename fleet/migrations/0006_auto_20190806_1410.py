# Generated by Django 2.2.4 on 2019-08-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0005_auto_20190806_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='tipo_veiculo',
            field=models.CharField(choices=[('Carro', 'Carro'), ('Moto', 'Moto')], default='Carro', max_length=5),
        ),
    ]