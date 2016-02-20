from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

import bcrypt
import requests

##Token generator function
def get_token():
    ## Simple random word request.
    request = requests.get('http://randomword.setgetgo.com/get.php')
    word = request.text
    print("")
    print('\x1b[0m' + "Hashing the word "  + '\033[93m' + word + '\x1b[0m' + ". Please wait..." + '\033[92m')
    print('\033[92m')
    password = word.encode(encoding='UTF-8',errors='strict')

    ## BCrypt uses a random salt to hash the random password.
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    return hashed


##Invitation Code Model
class InvitationCode(models.Model):
    code = models.CharField(default=get_token,blank = False, max_length = 60, unique=True, verbose_name=(u"Invitation code"))
    is_used = models.BooleanField(default=False, verbose_name=(u"Used?"))
    is_issued = models.BooleanField(default=True, verbose_name=(u"Issued?"))
    user = models.ForeignKey(User, blank=True, null=True)
    issued_date = models.DateTimeField(blank=False, default=timezone.now, verbose_name=(u"Issued on"))
    used_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name=(u"Used on"))

    def __str__(self):
        return self.code


##Feel free to modify the model or token gen function.
