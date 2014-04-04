from django.db import models

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

  def __str__(self):
    return self.name


class Committee(models.Model):
  name = models.CharField(max_length=70)
  description = models.TextField(blank=True)
  appointment_date = models.DateField(null=True, blank=True)
  chair = models.ForeignKey(Senator, related_name='committee_chair_set', blank=True, null=True)
  vice_chair = models.ForeignKey(Senator, related_name='committee_vice_chair_set', blank=True, null=True)
  senators = models.ManyToManyField(Senator, related_name='committee_set', blank=True, null=True)

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
  authors = models.ManyToManyField(Senator, related_name='bill_set', blank=True, null=True)
  primary_committee = models.ForeignKey(Committee, related_name='bill_set', blank=True, null=True)
  voters = models.ManyToManyField(Senator, through='Vote', related_name='voted_bill_set', blank=True)

  def __str__(self):
    return self.name

  def votes_summary(self):
    votes = [vote.vote for vote in self.vote_set.all()]
    if not votes :
      return "No voting record"
    counts = dict((i[0], votes.count(i[0])) for i in Vote.VOTE_TYPES)
    return "{0} Ayes, {1} Nays, {2} Present Not Voting, {3} Absent - {4}".format(counts["AYE"], counts["NAY"], counts["PNV"], counts["ABS"], self.vote_set.first().date_voted)


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
    return self.senator.name + ': ' + self.get_vote_display() + ' (' + self.bill.name + ')'

class Picture(models.Model):

    parent = models.ForeignKey(Senator, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.link + ' (' + self.parent.name + ')'