from django.db import models


CHOICES_BODY = (
            ('Седаны', 'Седаны'),
            ('Гибриды', 'Гибриды'),
            ('Кроссоверы', 'Кроссоверы'),
            ('Универсалы', 'Универсалы'),
            ('Хэтчбеки', 'Хэтчбеки'),
            ('Внедорожники', 'Внедорожники'),
        )

CHOICES_WHEEL = (
            ('4WD', '4WD'),
            ('RWD', 'RWD'),
            ('FWD', 'FWD'),
        )

class Post(models.Model):
    car_model = models.CharField(max_length=50)
    image = models.FileField(upload_to='', null=True, blank=True)
    body = models.CharField(max_length=30, choices=CHOICES_BODY, default='')

    year = models.IntegerField(default=2010)
    price = models.CharField(max_length=50)
    engine = models.FloatField(max_length=4, default=0.0)
    wheel = models.CharField(max_length=5, choices=CHOICES_WHEEL, default='')


    def __str__(self):
        return f"{self.car_model}"

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.phone}"
