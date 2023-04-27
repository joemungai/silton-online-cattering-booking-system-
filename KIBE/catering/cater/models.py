from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    team_number = models.PositiveIntegerField(default=0)
    charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    phone = models.CharField(max_length=20, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

# class Panesic_Hotel(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name

# class Mini_Inn_Hotel(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name

# class Mama_Africa_company(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name

# class Kamuketha_pork_joint(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name

# class Debaniers_Pizza_Place(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name

# class Quivers_Bar_Grill(models.Model):
#     name = models.CharField(max_length=30)
#     team_number = models.PositiveIntegerField(default=0)
#     charging_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
#     phone = models.CharField(max_length=20)
#     images = models.ImageField(blank=True)

#     def __str__(self):
#         return self.name