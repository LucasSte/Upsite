# Generated by Django 2.2.1 on 2019-06-27 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Topics', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Topics.Comment'),
        ),
        migrations.AddField(
            model_name='topicinformation',
            name='creator',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='topicinformation',
            name='downvotes_users',
            field=models.ManyToManyField(blank=True, related_name='downvotes_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicinformation',
            name='upvotes_users',
            field=models.ManyToManyField(blank=True, related_name='upvotes_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='big_description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='small_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='title_text',
            field=models.CharField(default='', max_length=50),
        ),
    ]
