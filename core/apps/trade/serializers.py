from django.conf import settings
from rest_framework import serializers

from .models import (
	Trade
)


class TradeSerializer(serializers.ModelSerializer):
	outcome_display 					= serializers.CharField(source="get_outcome_display", read_only=True)
	risk_appetite_display  				= serializers.CharField(source="get_risk_appetite_display", read_only=True)
	order_type_display  				= serializers.CharField(source="get_order_type_display", read_only=True)
	
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

			# Calculated fields
			"duration",
			"net_profit_loss",
			
			# Yet to be relational fields
			"symbol",
			"journal",
			"trading_model",
			"entry_model",

			"order_type_display",
			"outcome_display",
			"risk_appetite_display",

		)
		read_only_fields = (
			"id",
			"outcome",
			"order_type_display",
			"outcome_display",
			"risk_appetite_display",
		)

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance
