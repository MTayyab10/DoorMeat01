# Generated by Django 3.2.3 on 2021-06-22 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders3', '0012_delete_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=10)),
                ('cpn_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='orders3.customer')),
            ],
        ),
    ]