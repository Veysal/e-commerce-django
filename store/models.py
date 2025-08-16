from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, help_text="Используется для URL, например 'videokarty'")

    class Meta:
        # Настройки для отображения в админ-панели
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products',verbose_name="Категория")
    name = models.CharField(max_length=255, unique=True, verbose_name="Название товара")
    slug = models.SlugField(max_length=255, unique=True, help_text="Используется для URL, например 'videokarty'")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Изображения")
    stock = models.PositiveIntegerField(verbose_name="Количество на складе")
    is_available = models.BooleanField(default=True,verbose_name="Доступен для продажи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        # Настройки для отображения в админ-панели
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('-created_at',)

        def __str__(self):
            return self.name