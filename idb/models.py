from django.db import models

class Senator(models.Model):
  full_name = models.CharField(max_length=70)
  party     = models.CharField(max_length=70)
  occupation = models.CharField(max_length=200, blank=True)
  legislative_experience = models.CharField(max_length=200, blank=True)
  district = models.IntegerField(blank=True, null=True)
  committees = models.ManyToManyField(Committee)
  
  def __str__(self):
    return self.full_name

class Committee(models.Model):
  name = models.CharField(max_length=70)
  description = models.TextField(blank=True)
  appointment_date = models.DateField(null=True, blank=True)

  chair = models.ForeignKey(Senator, related_name='committee_chair_set', blank=True, null=True)
  vice_chair = models.ForeignKey(Senator, related_name='committee_vice_chair_set', blank=True, null=True)
  senators = models.ManyToManyField(Senator)

  def __str__(self):
    return self.name

class Bill(models.Model):
  name = models.CharField(max_length=70)
  legislative_session = models.CharField(max_length=70, blank=True)
  date_proposed = models.DateField(blank=True, null=True)
  date_signed = models.DateField(blank=True, null=True)
  date_effective = models.DateField(blank=True, null=True)
  status = models.CharField(max_length=70, blank=True)
  url = models.CharField(max_length=200, blank=True)

  description = models.TextField(blank=True)
  author = models.ForeignKey(Senator, related_name='authored_bill_set')
  primary_committee = models.ForeignKey(Committee, blank=True, null=True)
  voters = models.ManyToManyField(Senator, through='Vote', related_name='voted_bill_set')

  def __str__(self):
    return self.name

class Vote(models.Model):
  VOTE_TYPES = (
      ('AYE', 'Aye'), 
      ('NAY', 'Nay'),
      ('PNV', 'Present Not Voting'),
      ('ABS', 'Absent'),
  )
  senator = models.ForeignKey(Senator)
  bill = models.ForeignKey(Bill)
  vote = models.CharField(max_length=3, choices=VOTE_TYPES)
  date_voted = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.senator.full_name + ': ' + self.get_vote_display()
