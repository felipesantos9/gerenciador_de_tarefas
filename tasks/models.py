from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('realizando', 'Realizando'),
        ('concluida', 'Concluída')
    ]

    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
