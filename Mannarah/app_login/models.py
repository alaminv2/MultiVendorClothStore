from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an Email address...')
        email = self.normalize_email(email)
        user = self.model(email=email)
        print(f'user = {user}\npass = {password}\n\n')
        user.set_password(password)
        user.save(using=self._db)
        print(f'user = {user}')
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    address = models.TextField(max_length=350, blank=True)
    country = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + "'s Profile"

    def is_fully_filled(self):
        fields = [f.name for f in self._meta.get_fields()]
        for field in fields:
            value = getattr(self, field)
            if value is None or value == '':
                return False
        return True


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
