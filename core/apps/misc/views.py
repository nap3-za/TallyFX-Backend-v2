from rest_framework import (
	generics,
	status,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from core.apps.misc.field_choices import FormIDs


class RetrieveFieldChoices(generics.GenericAPIView):

	def get(self, request, *args, **kwargs):
		form_id = kwargs.get("formID")
		field_choices = {}

		if form_id == FormIDs.ADD_TRADE:
			field_choices["symbols"] = {
				"NSQ": "Nasdaq",
				"DOW": "Dow Jones",
				"SPY": "Standards & Poors",
			}
			field_choices["journals"] = {
				"JAN": "January",
				"INX": "Indices",
				"LRS": "Low Risk",
				"NYS": "New York Session",
			}
			field_choices["tradingModels"] = {
				"LSN": "London Snipper",
				"TTC": "22 Caliber",
				"ORG": "Opening Range Gap Expansion",
			}
			field_choices["entryModels"] = {
				"BRK": "Breaker-block",
				"TSP": "Turtle soup",
				"FVG": "Fair Value Gap",
			}
		else:
			return Response({"error": "Invalid form identified"}, status=status.HTTP_400_BAD_REQUEST)

		return Response(field_choices, status=status.HTTP_200_OK)

	