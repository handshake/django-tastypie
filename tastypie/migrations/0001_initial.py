from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import tastypie.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255)),
                ('url', models.CharField(default=b'', max_length=255, blank=True)),
                ('request_method', models.CharField(default=b'', max_length=10, blank=True)),
                ('accessed', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=b'', max_length=256, db_index=True, blank=True)),
                ('created', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('user', models.OneToOneField(related_name='api_key', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]