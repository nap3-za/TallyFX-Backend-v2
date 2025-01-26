from django.urls import path
from . import views

app_name="misc"


urlpatterns = [
	path("field-choices/<formID>/", views.RetrieveFieldChoices.as_view(), name="field-choices"),
]
