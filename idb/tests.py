from django.utils import unittest
from idb.models import Senator, Committee, Bill, Vote

class SenateTestCase(unittest.TestCase):
    def setUp(self):
        Senator.objects.get_or_create(name="Bob Deuell", party="Republican")
        Bill.objects.get_or_create(name="SB 21")
        Committee.objects.get_or_create(name="Economic Development")
        self.senator = Senator.objects.get(name="Bob Deuell")
        self.bill = Bill.objects.get(name="SB 21")
        self.committee = Committee.objects.get(name="Economic Development")
    def testSenator(self):
        self.assertEqual(str(self.senator),"Bob Deuell")
    def testBill(self):
        self.assertEqual(str(self.bill),"SB 21")
    def testCommittee(self):
        self.assertEqual(str(self.committee),"Economic Development")
    def testMemberType(self):
        self.committee.chair = self.senator
        self.assertEqual(self.committee.membertype(self.senator)," - Chair")
