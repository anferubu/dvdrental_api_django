# Generated by Django 4.1.2 on 2022-10-15 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
        migrations.AlterField(
            model_name='film',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.language'),
        ),
        migrations.AlterField(
            model_name='filmactor',
            name='actor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.actor'),
        ),
        migrations.AlterField(
            model_name='filmactor',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.film'),
        ),
        migrations.AlterField(
            model_name='filmcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.AlterField(
            model_name='filmcategory',
            name='film',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.film'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.film'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rental'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.staff'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inventory'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
        migrations.AlterField(
            model_name='store',
            name='manager_staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.staff'),
        ),
    ]
