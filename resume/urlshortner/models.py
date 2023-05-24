from django.db import models

class Shortner(models.Model):
    """Модель ссылки."""
    urls_text = models.CharField(max_length=500)

    def __str__(self):
        """Для корректного выведения навания обьекта в shell."""
        return self.urls_text
