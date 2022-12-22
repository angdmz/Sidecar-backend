# Generated by Django 4.1.4 on 2022-12-21 22:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PUBLIC_STOCK', 'Public stock')], default='PUBLIC_STOCK', max_length=50)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_legal_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('invested_since', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shares', models.BigIntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='investments.asset')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='investments.investor')),
            ],
            options={
                'unique_together': {('asset', 'investor', 'created_at')},
            },
        ),
    ]
