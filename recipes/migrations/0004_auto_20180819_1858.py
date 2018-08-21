# Generated by Django 2.0.6 on 2018-08-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180819_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='course',
            field=models.CharField(blank=True, choices=[('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Sides', 'Sides'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks'), (None, 'None')], default=None, max_length=100, null=True),
        ),
    ]