# Generated by Django 2.0.7 on 2018-11-15 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managment_system', '0008_auto_20181115_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_sent', to='managment_system.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_recieved', to='managment_system.User')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to='managment_system.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='managment_system.Message'),
        ),
    ]
