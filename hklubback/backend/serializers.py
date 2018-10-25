from django.contrib.auth.models import User, Group
from rest_framework import serializers
from hklubback.backend.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('firstmname', 'lastname', 'email', 'groups_id')


class InnerPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inner_people
        fields = ('name_az', 'name_ru','name_eng','story_az','story_ru','story_eng','photo','email','adress','money_stat')

class UsersInneedPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Inned_People
        fields = ('user_id', 'Inneed_people_id', 'date')

class PostAzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post_az
        fields = ('title', 'text', 'photo', 'Inneed_people_id', 'created_at', 'updated_at')
        