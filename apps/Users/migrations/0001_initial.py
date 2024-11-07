

from django.db import migrations, models
import django.utils.timezone
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='profile/default.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='profile/')),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nid', models.CharField(blank=True, max_length=20, null=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('trede_license', models.TextField(blank=True, null=True)),
                ('tin_number', models.CharField(blank=True, max_length=20, null=True)),
                ('vat_registration', models.TextField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
