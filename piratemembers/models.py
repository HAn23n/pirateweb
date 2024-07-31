from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    academy = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=[('Men', 'Men'), ('Female', 'Female'), ('LGBTQ+', 'LGBTQ+')])
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    stamina = models.IntegerField(null=True, blank=True)  # New field
    heal = models.IntegerField(null=True, blank=True)  # New field
    skill = models.IntegerField(null=True, blank=True)  # New field
    rank = models.CharField(max_length=50, null=True, blank=True)  # New field
    random_used = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.name
