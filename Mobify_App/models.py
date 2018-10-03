from django.db import models

# Create your models here.
class Payments_TRNs(models.Model):
	distance = models.IntegerField()
	initial_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
	on_count_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
	created_by = models.ForeignKey('auth.User', related_name='payments_trns', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.distance, self.on_count_amount)

class Payments(models.Model):
	amount = models.IntegerField(blank=False, default=0)
	is_paid = models.BooleanField(default=False)
	owner = models.ForeignKey('auth.User', related_name='payments', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	# class Meta:
	# 	db_table = 'payments'

	def __str__(self):
		return str(self.amount)

class Locations(models.Model):
	initial_location = models.CharField(max_length=30)
	end_location = models.CharField(max_length=30)
	distance = models.IntegerField()

	def ___str__(self):
		return str(self.distance)
