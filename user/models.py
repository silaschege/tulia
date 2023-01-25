from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self,email, first_name,last_name,other_name,phone_number, date_of_birth,password=None):
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        email = email.lower()



        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            other_name=other_name,
            phone_number=phone_number,
            date_of_birth= date_of_birth
        )

        user.set_password(password)
        user.save(using = self._db)
        'first_name','last_name','other_name','phone_number','date_of_birth'
        return user

    def create_primary_merchant (self,email, first_name,last_name,other_name,phone_number, date_of_birth,password=None):
        user = self.create_user(email, first_name,last_name,other_name,phone_number, date_of_birth,password)

        user.is_primary_merchant  = True
        user.save(using = self._db)

        return user

    def create_secondary_merchant(self,email, first_name,last_name,other_name,phone_number, date_of_birth,password=None):
        user = self.create_user(email, first_name,last_name,other_name,phone_number, date_of_birth,password)

        user.is_secondary_merchant= True
        user.save(using=self._db)

        return user

    
    def create_captain(self,email, first_name,last_name,other_name,phone_number, date_of_birth,password=None):
        user = self.create_user(email, first_name,last_name,other_name,phone_number, date_of_birth,password)

        user.is_captain = True
        user.save(using=self._db)

        return user

    def create_superuser(self,email, first_name,last_name,other_name,phone_number, date_of_birth,password=None):
        user = self.create_user(email, first_name,last_name,other_name,phone_number, date_of_birth,password)

        user.is_superuser = True
        user.is_staff = True
        user.is_primary_merchant  = True
        user.is_secondary_merchant = True
        user.is_captain = True
        
        user.save(using = self._db)

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=TRUE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    # have a regex validator
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_primary_merchant = models.BooleanField(default=False)
    is_secondary_merchant = models.BooleanField(default=False)
    is_captain = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','other_name','phone_number','date_of_birth']

    def __str__(self):
        return self.email

        # lands model and merchant model will be on separate apps

class MerchantBioData(models.Model):
    email = models.EmailField(max_length=255,unique=TRUE)
    merchant_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    major_landmark = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    primary_merchant = models.ForeignKey(UserAccount,on_delete=models.SET_DEFAULT,default=1)
    
    def __str__(self):
        return self.email


class MerchantEmployees(models.Model):
    merchant =  models.ForeignKey(MerchantBioData,on_delete=models.SET_DEFAULT,default=1)
    employee =  models.ForeignKey(UserAccount,on_delete=models.SET_DEFAULT,default=1)
   
    


