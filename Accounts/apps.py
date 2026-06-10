from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = "Accounts"
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import Accounts.signals