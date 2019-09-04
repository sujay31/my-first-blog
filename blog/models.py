#New code written after deletion of what was previously written
#lines starting with 'from' or 'import' are used to copy a portion from other files
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): 
#line defines our model(object) namely Post
#(models.Model) means that the Post is a Django Model so Django knows that it should be saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #'models.ForeignKey' is a link to another model
    title = models.CharField(max_length=200) #'models.CharField' is used to define text with a limited number of characters
    text = models.TextField() #'models.TextField' is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now) #'models.DateTimeField' is for date and time
    published_date = models.DateTimeField(blank=True, null=True) #'models.DateTimeField' is for date and time

    def publish(self): #'def' implies that it is a function and 'publish' is the name of the function 
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #'def' implies that it is a function and '_str_' is the name of the function
        return self.title #return call 