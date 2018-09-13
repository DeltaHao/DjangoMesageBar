from django.db import models
from django.contrib.auth.models import User


class normal_user_form(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(blank=False, max_length=50)
    birthday = models.DateField(blank=True, null=True)
    phonenumber = models.CharField(blank=False, max_length=12)
    class Meta:
        verbose_name_plural = "normal_user_form"


class Mesage (models.Model):
    content = models.TextField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    approval = models.IntegerField()

    def __str__(self):
        return '<mesage: %s>' % self.author

    class Meta:
        ordering = ['-created_time']

