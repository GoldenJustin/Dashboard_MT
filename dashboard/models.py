from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Reporter(models.Model):
    reporter_id = models.AutoField(primary_key=True)
    reporter_number = PhoneNumberField(blank=False, null=False, unique=True)

    def __str__(self):
        return str(self.reporter_number)


class Scammer(models.Model):
    class Meta:
        unique_together = ('reporter_id', 'scammer_number')

    reporter_id = models.ForeignKey(Reporter, related_name='S_reporter_id', on_delete=models.CASCADE)
    scammer_id = models.AutoField(primary_key=True)
    scammer_number = PhoneNumberField()

    def __str__(self):
        return str(self.scammer_number)


class Info(models.Model):
    info_id = models.AutoField(primary_key=True)
    reporter_id = models.ForeignKey(Reporter, related_name='r_reporter_id', on_delete=models.CASCADE)
    scammer_number = models.ManyToManyField(Scammer, related_name='r_scammer_number')
    contained_sms = models.TextField()
    sms_date = models.DateField()
    sms_time = models.TimeField()
    date_reported = models.DateField(auto_now_add=True)
    time_reported = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.scammer_number)


class Registration(models.Model):
    REGISTRATION = (
        ('REGISTERED', 'Imesajiliwa'),
        ('NOT_REGISTERED', 'Haijasajiliwa')
    )
    phone_number = models.OneToOneField(Reporter, related_name='phone_number', on_delete=models.CASCADE,
                                        primary_key=True)
    scammer_id2 = models.ForeignKey(Scammer, related_name='scammer_id2', on_delete=models.CASCADE)
    reg_name = models.CharField(max_length=200)
    reg_date_time = models.DateTimeField()
    reg_status = models.CharField(max_length=18, null=False, default='Inachakatwa', choices=REGISTRATION)
    location = models.TextField()

    def __str__(self):
        return str(self.reg_status)
