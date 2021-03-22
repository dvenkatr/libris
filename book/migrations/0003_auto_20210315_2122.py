# Generated by Django 3.1.6 on 2021-03-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210315_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(blank=True, choices=[('4', 'Outstanding'), ('3', 'Good'), ('2', 'Not good'), ('1', 'Bad')], max_length=1, null=True)),
                ('review', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='book.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='blurb',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='award',
            field=models.CharField(blank=True, choices=[('Pulitzer', 'Pulitzer'), ('Booker', 'Booker'), ('Hugo', 'Hugo')], max_length=10, null=True),
        ),
    ]
