from django.db import models

# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    group_id = models.IntegerField()


    def __str__(self):
        return self.firstname
        

class Inneed_people(models.Model):
    name_az = models.TextField()
    name_ru = models.TextField()
    name_eng = models.TextField()
    story_az = models.TextField()
    story_ru = models.TextField()
    story_eng = models.TextField()
    photo = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    money_stat = models.IntegerField()


class Users_Inneed_people(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)
    Inneed_people_id = models.ForeignKey(Inneed_people, on_delete = models.CASCADE)
    date = models.DateField()
    # amount = something_that_i_forgot :D


class Posts_az(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.CharField(max_length=255)
    Inneed_people_id = models.ForeignKey(Inneed_people, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


# class Categories(models.Model):
#     cat_ids = models.ForeignKey(Inneed_people, on_delete = models.CASCADE)
#     names = models.ForeignKey(Inneed_people, on_delete = models.CASCADE)



