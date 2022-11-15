# Generated by Django 4.1.3 on 2022-11-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gun_text', models.CharField(max_length=200)),
                ('is_legal', models.BooleanField(verbose_name='Is legal?')),
                ('amount', models.IntegerField()),
            ],
        ),
    ]