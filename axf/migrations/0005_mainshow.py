# Generated by Django 2.1.1 on 2018-09-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=150)),
                ('categoryid', models.CharField(max_length=16)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=16)),
                ('productid1', models.CharField(max_length=16)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.FloatField(default=0)),
                ('marketprice1', models.FloatField(default=1)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=16)),
                ('productid2', models.CharField(max_length=16)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.FloatField(default=0)),
                ('marketprice2', models.FloatField(default=1)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=16)),
                ('productid3', models.CharField(max_length=16)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.FloatField(default=0)),
                ('marketprice3', models.FloatField(default=1)),
            ],
        ),
    ]