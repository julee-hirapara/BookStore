# Generated by Django 4.2.2 on 2023-07-23 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=200)),
                ('bookPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book')),
            ],
        ),
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.author')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authorName',
            field=models.ManyToManyField(through='store.Bookstore', to='store.author'),
        ),
    ]
