from django.apps import AppConfig


class TicketCreatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket_creator'
    verbose_name = 'Создание тикетов'