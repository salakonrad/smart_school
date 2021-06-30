from django.db import models


# Create your models here.
class ClassInfo(models.Model):
    name = models.CharField(max_length=45, unique=True)
    display_name = models.CharField(max_length=30, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name


class ClassRegistration(models.Model):
    name = models.CharField(max_length=10, unique=True)
    department_select = (
        ('mat-fiz', 'Mat-fiz'),
        ('mat-geo', 'Mat-geo'),
        ('mat-ang', 'Mat-ang'),
        ('dziennikarstwo', 'Dziennikarstwo')
    )
    department = models.CharField(choices=department_select, max_length=15)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name']

    def __str__(self):
        return self.name
