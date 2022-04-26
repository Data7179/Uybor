# Generated by Django 4.0.3 on 2022-04-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uybor', '0012_alter_uylar_viloyat_alter_uylar_xonalar_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uylar',
            name='Aftoturargox',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=1, max_length=100, verbose_name='Aftoturargox'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='bino_asosi',
            field=models.CharField(choices=[('2', 'Panel'), ('1', "G'ishtli")], default=1, max_length=100, verbose_name='Bino Asosi'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='bolalar_maydonchasi',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=1, max_length=100, verbose_name='Bolalar Maydonchasi'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='internet',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=1, max_length=5, verbose_name='Internet'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='kanalizatsiya',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=1, max_length=100, verbose_name='Kanalizatsiya'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='lift',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=2, max_length=100, verbose_name='Lift'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='qoriqlash',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=2, max_length=100, verbose_name="Qo'riqlash"),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='uy_turi',
            field=models.CharField(choices=[('1', 'Ijara'), ('2', 'Sotuv')], default=1, max_length=100, verbose_name='Tanlang'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='video_kuzatuv',
            field=models.CharField(choices=[('1', 'Bor'), ('2', "Yo'q")], default=1, max_length=100, verbose_name='Video Kuzatuv'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='viloyat',
            field=models.CharField(choices=[('5', 'Namangan'), ('6', 'Buxoro'), ('12', "Qoraqalpog'iston"), ('4', 'Andijon'), ('1', 'Toshkent Shahar'), ('11', 'Navoiy'), ('10', 'Surxandaryo'), ('2', 'Toshkent Viloyat'), ('7', 'Samarqand'), ('3', "Farg'ona"), ('8', 'Xorazm'), ('9', 'Qashqadaryo')], default=1, max_length=100, verbose_name='Viloyat'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='xonalar_soni',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('4', '4'), ('6', '6'), ('3', '3'), ('5', '5')], default=2, max_length=1, verbose_name='Xonalar Soni'),
        ),
    ]