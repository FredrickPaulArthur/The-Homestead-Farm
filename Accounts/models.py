# User contains all the details of - name, dob, address, ....
# Profile contains - a display_name, display_picture, membership_type


from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics'
    )
    # primary key of a model which “extends” another model in some way


    def __str__(self):
        return self.name
    

    def save(self):
        super.save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)