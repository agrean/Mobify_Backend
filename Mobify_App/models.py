from django.db import models

# Create your models here.

class Payments(models.Model):
	amount = models.IntegerField()
	is_paid = models.BooleanField(default=False)

	# class Meta:
	# 	db_table = 'payments'

	def __str__(self):
		return str(self.amount)