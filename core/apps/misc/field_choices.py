from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Genders(TextChoices):
	MALE = "MLE", _("Male")
	FEMALE = "FML", _("Female")
	NON_BINARY = "NBN", _("Non-binary")


# = = = Trade

class RiskAppetites(TextChoices):
	HIGH = "HIG", _("High")
	MEDIUM = "MED", _("Medium")
	LOW = "LOW", _("Low")

class RiskRewardProfiles(TextChoices):
	ONE_TWO = "OTT", _("1:2")
	ONE_THREE = "OTR", _("1:3")
	ONE_FOUR = "OTF", _("1:4")

class OrderTypes(TextChoices):
	BUY = "BUY", _("Buy")
	SELL = "SEL", _("Sell")
	SELL_LIMIT = "SLL", _("Sell limit")
	BUY_LIMIT = "BYL", _("Buy limit")

class TradeOutcomes(TextChoices):
	IN_PROGRESS = "INP", _("In progress")
	WIN = "WIN", _("Win")
	LOSS = "LOS", _("Loss")

class FormIDs(TextChoices):
	ADD_TRADE = "ADT", _("Add Trade")