from rest_framework import serializers
from .models import Payments_TRNs, Payments
from django.contrib.auth.models import User

class PaymentSerializer(serializers.ModelSerializer):
	# is_paid = serializers.BooleanField(required=False) #read_only=True
	# amount = serializers.IntegerField()

	# def create(self, validate_data):
	# 	"""
	# 	Create and return a new Payment instance given the validate data
	# 	"""
	# 	return Payments.objects.create(**validate_data)

	# def update(self, instance, validate_data):
	# 	""" 
	# 	Update and return an existing Payment given the validate date
	# 	"""
	# 	instance.is_paid = validate_data.get('is_paid', instance.is_paid)
	# 	instance.amount = validate_data.get('amount', instance.amount)

	# 	instance.save()
	# 	return instance

	owner = serializers.ReadOnlyField(source='created_by.username')

	class Meta:
		model = Payments
		fields = ('amount', 'owner')

class UserSerializer(serializers.ModelSerializer):
	payments_trns = serializers.PrimaryKeyRelatedField(many=True, queryset=Payments_TRNs.objects.all()) #This line 
	payments = serializers.PrimaryKeyRelatedField(many=True, queryset=Payments.objects.all())

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
			'payments_trns',
			'payments'
		)