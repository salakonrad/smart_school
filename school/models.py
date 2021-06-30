from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    absence_types = (
        ('śpóźnienie', 'Śpóźnienie'),
        ('nieobecność', 'Nieobecność'),
        ('nieobecność usprawiedliwiona', 'Nieobecność usprawiedliwiona'),
    )
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    uczen = models.ForeignKey(User, on_delete=models.CASCADE)
    typ_nieobecnosci = models.CharField(max_length=30, choices=absence_types, default='spóźnienie')

    # def __(self):
    #     return self.uczen

    def get_absolute_url(self):
        return reverse('school-detail', kwargs={"pk": self.pk})
