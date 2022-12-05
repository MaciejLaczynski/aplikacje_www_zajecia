from rest_framework import serializers
from django.utils import timezone
from .models import Gun, Choice, Osoba, Druzyna

class GunModelSerializer(serializers.Serializer):
    model = Gun
    fields = ['id', 'Gun_name', 'pub_date']
    read_only_fields = ['id', 'pub_date']

class DruzynaModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length=64)
    kraj = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

class OsobaModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=64)
    nazwisko = serializers.CharField(max_length=64)
    miesiac_urodzenia = serializers.ChoiceField(choices=Osoba.Dates.choices, default=Osoba.Dates.JANUARY)
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(), allow_null=True)
    data_dodania = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("W polu moga znalezc sie tylko litery")
        return value

    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("W polu moga znalezc sie tylko litery")
        return value
	
    def validate_data_dodania(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Data urodzenia nie moze byc z przyszlosci")
        return value

class GunModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Gun.objects.all(), allow_null=True)
    choice_text = serializers.CharField(required=True)
    votes = serializers.IntegerField()

    def create(self, validated_data):
        return Gun.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.choice_text = validated_data.get('choice_text', instance.choice_text)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.save()
        return instance