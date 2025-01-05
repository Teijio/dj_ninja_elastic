from django.apps import AppConfig

# from .containers import ProductContainer

# container = ProductContainer()


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.products"
    verbose_name = "Товары"

    container = None

    def ready(self):
        from .containers import ProductContainer
        self.container = ProductContainer()
