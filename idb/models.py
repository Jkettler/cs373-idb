from django.db import models

import watson

class Senator(models.Model):
  name = models.CharField(max_length=70)
  party = models.CharField(max_length=70)
  occupation = models.CharField(max_length=200, blank=True)
  legislative_experience = models.CharField(max_length=200, blank=True)
  district = models.IntegerField(blank=True, null=True)
  # photo_url = models.URLField(blank=True, null=True)
  twitter = models.CharField(max_length=50, blank=True)
  facebook = models.URLField(blank=True)
  map = models.TextField(blank=True)

  def get_absolute_url(self):
    return "/senators/%i/" % self.id

  def __str__(self):
    return self.name

watson.register(Senator, exclude=("map",))

class Committee(models.Model):
  name = models.CharField(max_length=70)
  description = models.TextField(blank=True)
  appointment_date = models.DateField(null=True, blank=True)
  chair = models.ForeignKey(Senator, related_name='committee_chair_set', blank=True, null=True)
  vice_chair = models.ForeignKey(Senator, related_name='committee_vice_chair_set', blank=True, null=True)
  senators = models.ManyToManyField(Senator, related_name='committee_set', blank=True, null=True)

  def get_absolute_url(self):
    return "/committees/%i/" % self.id

  def __str__(self):
    return self.name

watson.register(Committee)

class Bill(models.Model):
  name = models.CharField(max_length=70)
  legislative_session = models.CharField(max_length=70, blank=True)
  date_proposed = models.DateField(blank=True, null=True)
  date_signed = models.DateField(blank=True, null=True)
  date_effective = models.DateField(blank=True, null=True)
  status = models.CharField(max_length=70, blank=True)
  url = models.CharField(max_length=200, blank=True)
  description = models.TextField(blank=True)
  authors = models.ManyToManyField(Senator, related_name='bill_set', blank=True, null=True)
  primary_committee = models.ForeignKey(Committee, related_name='bill_set', blank=True, null=True, on_delete=models.SET_NULL)
  voters = models.ManyToManyField(Senator, through='Vote', related_name='voted_bill_set', blank=True)

  def get_absolute_url(self):
    return "/bills/%i/" % self.id

  def __str__(self):
    return self.name

watson.register(Bill)

class Vote(models.Model):
  VOTE_TYPES = (
      ('AYE', 'Aye'),
      ('NAY', 'Nay'),
      ('PNV', 'Present Not Voting'),
      ('ABS', 'Absent'),
  )
  senator = models.ForeignKey(Senator)
  bill = models.ForeignKey(Bill, related_name='vote_set')
  vote = models.CharField(max_length=3, choices=VOTE_TYPES)
  date_voted = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.senator.name + ': ' + self.get_vote_display() + ' (' + self.bill.name + ')'

class Picture(models.Model):

    parent = models.ForeignKey(Senator, related_name='pictures_set', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.link + ' (' + self.parent.name + ')'
