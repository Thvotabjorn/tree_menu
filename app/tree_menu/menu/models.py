from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('id',)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    parent_node = models.ForeignKey(
        'MenuItem',
        on_delete=models.CASCADE,
        related_name='child_items',
        verbose_name='Дочерный пункт',
        null=True
    )
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        verbous_name='Пункты'
    )
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('id',)

    def __str__(self):
        return self.name
