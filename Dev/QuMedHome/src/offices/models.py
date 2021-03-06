from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_job_title
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class Prospect(models.Model):
    # owner = models.ForeignKey(User) # setting certain users as owners of prospects # django models unleashed
    first_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    business_email = models.EmailField(max_length=120, null=False, blank=False)
    company_name = models.CharField(max_length=120, null=False, blank=False)
    job_title = models.CharField(max_length=120, null=True, blank=True, validators=[validate_job_title])
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=False, blank=False)  # validators should be a list
    city = models.CharField(max_length=120, null=False, blank=False)
    state = models.CharField(max_length=120, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # creating slugs
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.company_name

    @property
    def title(self):
        return self.company_name  # obj.tiletile


def off_pre_save_receiver(sender, instance, *args, **kwargs):
    #saving stuff
    instance.company_name = instance.company_name.upper()

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def off_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save(# )


pre_save.connect(off_pre_save_receiver, sender=Prospect)

# post_save.connect(off_post_save_receiver, sender=Office)
