from rest_framework import serializers
from .models import Expense


class ExpenseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('uuid', 'description', 'created_at', 'amount', 'currency', 'employee', 'approved')
