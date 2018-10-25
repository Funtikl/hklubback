Admin Fuad - password - samsung 793
1) 
Serializers : Write down serializers in serializers.py 
This file represents Data for our API 
Notice that we're using hyperlinked relations in this case, with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.


2)
Views : A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response. 
We can use rest_framework viewsets instead of django-views.
Import models that serialized in serializers.py, then we can chose how endpoint will be viewed.

3) 
URLs : Here we have to write API URLs. Viewsets can automatically generate the URL configuratins for API, by simply registering the viewsets with a router class.

4) 
Pagination : It has been written in the settings.py and there we can control it.

5)

