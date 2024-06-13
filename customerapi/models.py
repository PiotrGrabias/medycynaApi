from django.db import models


class Entry(models.Model):
    description = models.TextField()
    user_mood = models.IntegerField()
    calculated_mood = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Entry - {self.created_at}'