from django.db import models

class StatisticsData(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='graphs/')  # Для графиков
    table_data = models.TextField(help_text="Введите данные таблицы в HTML формате")  # Для табличных данных

    def __str__(self):
        return self.title