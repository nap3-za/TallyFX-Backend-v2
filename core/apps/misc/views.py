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
				"Nasdaq": "Nasdaq",
				"Dow Jones": "Dow Jones",
				"Standards & Poors": "Standards & Poors",
			}
			field_choices["journals"] = {
				"January": "January",
				"Indices": "Indices",
				"Low risk": "Low Risk",
				"Ney york session": "New York Session",
			}
			field_choices["tradingModels"] = {
				"London Snipper": "London Snipper",
				"22 Caliber": "22 Caliber",
				"Opening Range Gap Expansion": "Opening Range Gap Expansion",
			}
			field_choices["entryModels"] = {
				"Breaker block": "Breaker-block",
				"Turtle soup": "Turtle soup",
				"Fair value gap": "Fair Value Gap",
			}
		else:
			return Response({"error": "Invalid form identified"}, status=status.HTTP_400_BAD_REQUEST)

		return Response(field_choices, status=status.HTTP_200_OK)

	