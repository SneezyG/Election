from django.db import models

# Create your models here.



class AnnouncedLGAResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=40, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_lga_results'




class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=40, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_pu_results'
        
 


class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=40, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'lga'




class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True, default=None)
    polling_unit_number = models.CharField(max_length=50, null=True, default=None)
    polling_unit_name = models.CharField(max_length=50, null=True, default=None)
    polling_unit_description = models.TextField(null=True, default=None)
    lat = models.CharField(max_length=255, null=True, default=None)
    long = models.CharField(max_length=255, null=True, default=None)
    entered_by_user = models.CharField(max_length=50, null=True, default=None)
    date_entered = models.CharField(max_length=40, null=True, default=None)
    user_ip_address = models.CharField(max_length=50, null=True, default=None)

    class Meta:
        db_table = 'polling_unit'




class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=40, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'



class NewVote(models.Model):
    polling_unit_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    user_name = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'new_vote'