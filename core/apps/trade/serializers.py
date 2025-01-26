from django.conf import settings
from rest_framework import serializers

from .models import (
	Trade
)


class TradeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Trade
		fields = (
			"id",
			"risk_appetite",
			"riskreward_profile",
			"order_type",
			"fill_price",
			"exit_price",
			"stoploss_price",
			"takeprofit_price",
			"execution_time",
			"exit_time",

			"outcome",
			"trade_review",
			
			# Yet to be relational fields
			"journal",
			"trading_model",
			"entry_model",
		)
		read_only_fields = (
			"id",
		)

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance
