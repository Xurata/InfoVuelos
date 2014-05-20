from django.forms import ModelForm
from iInfoVuelos.models import Company, Flight

class CompanyForm (ModelForm):
	class Meta:
		model = Company
		exclude = ('user', 'date',)

class FlightForm (ModelForm):
	class Meta:
		model = Flight
		exclude = ('user', 'date','company',)
