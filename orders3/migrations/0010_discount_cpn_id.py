# Generated by Django 3.2.3 on 2021-06-22 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders3', '0009_remove_discount_coupon_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='cpn_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='orders3.customer'),
        ),
    ]
