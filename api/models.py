from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    membership_id = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'client' 
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'workout'
class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'trainer'

class HealthProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'health_profile'