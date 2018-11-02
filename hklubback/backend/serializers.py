from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('firstname', 'lastname', 'email', 'group_id')


class InneedPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inneed_people
        fields = ('name_az', 'name_ru','name_eng','story_az','story_ru','story_eng','photo','email','adress','money_stat')

class UsersInneedPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users_Inneed_people
        fields = ('user_id', 'Inneed_people_id', 'date')

class PostAzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts_az
        fields = ('title', 'text', 'photo', 'Inneed_people_id', 'created_at', 'updated_at')
        