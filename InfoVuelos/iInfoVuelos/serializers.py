from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Airport, Company, Flight

class CompanySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='company-detail')
    flight = HyperlinkedRelatedField(many=True, read_only=True, view_name='flight-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Company
        fields = ('url', 'name', 'code', 'user')

class FlightSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='flight-detail')
    company = HyperlinkedRelatedField(view_name='company-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Flight
        fields = ('url', 'code', 'origin', 'destination', 'gate', 'company', 'user')

