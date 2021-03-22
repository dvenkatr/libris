# Generated by Django 3.1.6 on 2021-03-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20210316_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='book',
        ),
        migrations.AddField(
            model_name='tag',
            name='books',
            field=models.ManyToManyField(related_name='tags_for_this_book', to='book.Book'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
