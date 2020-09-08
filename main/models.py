from django.db import models
from django.contrib.auth import get_user_model

import random
import string

def buildstr():
	size = random.randint(2,10)
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

class ShortURL(models.Model):
    url = models.URLField(max_length=300, unique=True)
    new_url = models.CharField(max_length=50, unique=True, default=buildstr)