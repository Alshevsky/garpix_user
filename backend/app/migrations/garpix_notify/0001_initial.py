# Generated by Django 3.2.8 on 2021-10-25 05:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import garpix_notify.mixins.user_notify_mixin
import garpix_notify.utils.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcm_django', '0005_auto_20170808_1145'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('subject', models.CharField(blank=True, default='', max_length=255, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Текст')),
                ('html', models.TextField(blank=True, default='', verbose_name='HTML')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email Получателя')),
                ('sender_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email Отправителя')),
                ('type', models.IntegerField(choices=[(0, 'E-mail'), (1, 'SMS'), (2, 'Push'), (3, 'Telegram'), (4, 'Viber')], verbose_name='Тип')),
                ('state', models.IntegerField(choices=[(1, 'Доставлено'), (-1, 'Отклонено'), (0, 'В ожидании'), (-2, 'Не отправлено (отправка запрещена настройками)')], default=0, verbose_name='Состояние')),
                ('event', models.IntegerField(blank=True, choices=[(2021, 'Подтверждение номера телефона')], null=True, verbose_name='Событие')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('data_json', models.TextField(blank=True, null=True, verbose_name='Данные пуш-уведомления (JSON)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('send_at', models.DateTimeField(blank=True, null=True, verbose_name='Время начала отправки')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='NotifyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('template', models.TextField(default='{{text}}', verbose_name='Шаблон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='NotifyConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodic', models.IntegerField(default=60, verbose_name='Периодичность отправки уведомлений (сек.)')),
                ('email_max_day_limit', models.IntegerField(default=240, verbose_name='Дневной лимит отправки писем')),
                ('email_max_hour_limit', models.IntegerField(default=40, verbose_name='Часовой лимит отправки писем')),
                ('sms_url', models.CharField(default='http://sms.ru/sms/send', max_length=255, verbose_name='URL СМС провайдера')),
                ('sms_api_id', models.CharField(blank=True, default='1234567890', max_length=255, verbose_name='API ID СМС провайдера')),
                ('sms_from', models.CharField(blank=True, default='', help_text='Например, Garpix', max_length=255, verbose_name='Отправитель СМС')),
                ('telegram_api_key', models.CharField(blank=True, default='000000000:AAAAAAAAAA-AAAAAAAA-_AAAAAAAAAAAAAA', max_length=255, verbose_name='Telegram API Key')),
                ('telegram_bot_name', models.CharField(blank=True, default='', help_text='Например, MySuperBot', max_length=255, verbose_name='Telegram Имя бота')),
                ('telegram_welcome_text', models.TextField(blank=True, default='Добрый день! Здесь вы можете получать уведомления от нашего сайта', verbose_name='Telegram - Приветственный текст бота')),
                ('telegram_help_text', models.TextField(blank=True, default='Используйте команду /set <уникальный код> для того, чтобы получать сообщения от бота. Уникальный код вы можете получить на нашем сайте', verbose_name='Telegram - Текст помощи бота')),
                ('telegram_bad_command_text', models.TextField(blank=True, default='Неправильный формат команды', verbose_name='Telegram - Текст неправильной команды бота')),
                ('telegram_success_added_text', models.TextField(blank=True, default='Ваша учетная запись успешно привязана к боту. Вы будете получать уведомления!', verbose_name='Telegram - Текст успешно добавлен код')),
                ('telegram_failed_added_text', models.TextField(blank=True, default='Ошибка при привязке учетной записи. Пожалуйста, свяжитесь с техподдержкой', verbose_name='Telegram - Текст провал, не добавлен код')),
                ('viber_api_key', models.CharField(blank=True, default='000000000:AAAAAAAAAA-AAAAAAAA-_AAAAAAAAAAAAAA', max_length=255, verbose_name='Viber API Key')),
                ('viber_bot_name', models.CharField(blank=True, default='Viber bot', max_length=255, verbose_name='Название viber бота')),
                ('is_email_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку Email')),
                ('is_sms_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку SMS')),
                ('is_push_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку PUSH')),
                ('is_telegram_enabled', models.BooleanField(default=True, help_text='Внимание! Telegram недоступен на серверах на территории РФ и работать на них не будет!.', verbose_name='Разрешить отправку Telegram')),
                ('is_viber_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку Viber')),
                ('viber_success_added_text', models.TextField(blank=True, default='Ваша учетная запись успешно привязана к боту. Вы будете получать уведомления!', verbose_name='Viber - Текст успешно добавлен код')),
                ('viber_failed_added_text', models.TextField(blank=True, default='Ошибка при привязке учетной записи. Пожалуйста, свяжитесь с техподдержкой', verbose_name='Viber - Текст провал, не добавлен код')),
                ('viber_text_for_new_sub', models.TextField(blank=True, default='cпасибо за подписку, Введите secret_key чтобы получать сообщения от бота.', verbose_name='Viber - Текст  для новых подписчиков')),
                ('viber_welcome_text', models.TextField(blank=True, default='для активации бота нужно отправить любое сообщения', verbose_name='Viber - Приветственный текст бота')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='NotifyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1000, upload_to=garpix_notify.utils.file.get_file_path, verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='NotifyUserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название списка пользователей')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('mail_to_all', models.BooleanField(default=False, verbose_name='Отправить всем')),
                ('user_groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Группы пользователей')),
            ],
            options={
                'verbose_name': 'Список пользователей для рассылки',
                'verbose_name_plural': 'Списки пользователей для рассылки',
            },
        ),
        migrations.CreateModel(
            name='NotifyDevice',
            fields=[
            ],
            options={
                'verbose_name': 'FCM аккаунт',
                'verbose_name_plural': 'FCM аккаунты',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('fcm_django.fcmdevice',),
        ),
        migrations.CreateModel(
            name='SMTPAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default='smtp.yandex.ru', max_length=255, verbose_name='Хост')),
                ('port', models.IntegerField(default=587, verbose_name='Порт')),
                ('is_use_tls', models.BooleanField(default=True, verbose_name='Использовать TLS?')),
                ('is_use_ssl', models.BooleanField(default=False, verbose_name='Использовать SSL?')),
                ('sender', models.EmailField(blank=True, default='', max_length=255, verbose_name='Отправитель')),
                ('username', models.CharField(blank=True, default='', max_length=255, verbose_name='Имя пользователя')),
                ('password', models.CharField(blank=True, default='', max_length=255, verbose_name='Пароль пользователя')),
                ('timeout', models.IntegerField(default=5000, verbose_name='Таймаут (сек.)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Включить аккаунт')),
                ('email_hour_used_times', models.IntegerField(default=0, verbose_name='Количество использований в час')),
                ('email_day_used_times', models.IntegerField(default=0, verbose_name='Количество использований в день')),
                ('email_hour_used_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата использований в час')),
                ('email_day_used_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата использований в день')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='garpix_notify.notifycategory', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'SMTP аккаунт',
                'verbose_name_plural': 'SMTP аккаунты',
            },
        ),
        migrations.CreateModel(
            name='NotifyUserListParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email Получателя')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_lists', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)')),
                ('user_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='garpix_notify.notifyuserlist', verbose_name='Список пользователей для рассылки')),
            ],
            options={
                'verbose_name': 'Участник списка пользователей',
                'verbose_name_plural': 'Участники списка пользователей',
            },
        ),
        migrations.CreateModel(
            name='NotifyTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('title', models.CharField(max_length=255, verbose_name='Название для админа')),
                ('subject', models.CharField(blank=True, default='', max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='HTML')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email получатель')),
                ('type', models.IntegerField(choices=[(0, 'E-mail'), (1, 'SMS'), (2, 'Push'), (3, 'Telegram'), (4, 'Viber')], verbose_name='Тип')),
                ('event', models.IntegerField(blank=True, choices=[(2021, 'Подтверждение номера телефона')], null=True, verbose_name='Событие')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('send_at', models.DateTimeField(blank=True, null=True, verbose_name='Время начала отправки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='garpix_notify.notifycategory', verbose_name='Категория')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)')),
                ('user_lists', models.ManyToManyField(blank=True, to='garpix_notify.NotifyUserList', verbose_name='Списки пользователей, которые получат копию уведомления')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
            },
        ),
        migrations.CreateModel(
            name='NotifyErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField(blank=True, default='', null=True, verbose_name='Ошибка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='garpix_notify.notify', verbose_name='Notify')),
            ],
            options={
                'verbose_name': 'Ошибка отправки уведомления',
                'verbose_name_plural': 'Ошибки отправки уведомления',
            },
        ),
        migrations.AddField(
            model_name='notify',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifies', to='garpix_notify.notifycategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='notify',
            name='files',
            field=models.ManyToManyField(to='garpix_notify.NotifyFile', verbose_name='Файлы'),
        ),
        migrations.AddField(
            model_name='notify',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifies', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь (получатель)'),
        ),
    ]
