from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User


class GetVm(models.Model):
    vm_name = models.CharField(max_length=40)

    def __str__(self):
        return self.vm_name


class ComposeVM(models.Model):

    vm_name = models.CharField(max_length=25,help_text="Inter Your vm name",verbose_name='نام ماشین مجازی')
    number_of_cores = models.IntegerField(verbose_name='تعداد هسته')
    number_of_memory = models.IntegerField(verbose_name='رم')
    creation_of_vm = models.DateTimeField(verbose_name='تاریخ ایجاد')
    describtion = models.TextField(max_length=150,blank=True,verbose_name='توضیخات')

    class Meta:
        verbose_name = 'ماشین مجازی'
        verbose_name_plural = 'ماشین مجازی ها'

    def __str__(self):
        return self.vm_name


class UserProfile(models.Model):
    user_name = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=100)
    phone_number = models.IntegerField(blank=False)
    website = models.URLField()

# class UserProfileManager(models.Manager):
#     def __get_queryset(self):
#         return super(UserProfileManager, self).get_queryset()

