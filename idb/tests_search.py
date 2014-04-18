#!/usr/bin/env python3

from django.test import TestCase
import httplib
import json

#host = "texaslawdb.herokuapp.com"
host = "0.0.0.0:12345"

def senators_post():
    connection = httplib.HTTPConnection(host)
    values = json.dumps({
    "bills": [
        1
    ],
    "committees": [
        1
    ],
    "district": 17,
    "facebook": "https://www.facebook.com/SenatorJaneNelson",
    "legislative_experience": "Senate Member, December 2008 - present",
    "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3348.899273384878!2d-97.0779837!3d32.927259399999954!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864c2b26c440b8cb%3A0xe8f6fb2969de0ad!2s1235+S+Main+St+%23280!5e0!3m2!1sen!2sus!4v1395279135094",
    "name": "Joan tests test",
    "occupation": "Attorney",
    "party": "Republican",
    "twitter": "SenJaneNelson"
    })
    headers = {"Content-Type": "application/json"}
    connection.request("POST", "/api/senators/", values, headers)
    return connection

def senators_delete(sen_id):
    connection = httplib.HTTPConnection(host)
    connection.request("DELETE", "/api/senators/" + str(sen_id) + "/")
    return connection


def bills_post():
    connection = httplib.HTTPConnection(host)
    values = json.dumps({
        "authors":
            [
                1
            ],
        "date_effective": "2013-06-14",
        "date_proposed": "2012-11-12",
        "date_signed": "2013-06-14",
        "description": "Relating to consent to the immunization of certain children.",
        "legislative_session": "83(R)",
        "name": "SB 747 test",
        "primary_committee": 1,
        "status": "Signed into law",
        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63"
    })

    headers = {"Content-Type": "application/json"}
    connection.request("POST", "/api/bills/", values, headers)
    return connection

def bills_delete(bill_id):
    connection = httplib.HTTPConnection(host)
    connection.request("DELETE", "/api/bills/" + str(bill_id) + "/")
    return connection


def committees_post():
    connection = httplib.HTTPConnection(host)
    values = json.dumps(
        {
        "appointment_date": "2013-01-08",
        "bills": [
            1
        ],
        "chair": 1,
        "description": "Helping humans test on animals",
        "name": "Health & Human Services test ",
        "senators": [
            1
        ],
        "vice_chair": 1
        }
    )

    headers = {"Content-Type": "application/json"}
    connection.request("POST", "/api/committees/", values, headers)
    return connection

def committees_delete(committee_id):
    connection = httplib.HTTPConnection(host)
    connection.request("DELETE", "/api/committees/" + str(committee_id) + "/")
    return connection

class tests_search (TestCase) :
    """
    Tests for the Senator class
    """

    def test_senators_search(self) :
        connection = senators_post()
        sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
        sen_name = json.loads(connection.getresponse().read().decode("utf-8"))['name']
        connection.close()

        connection = httplib.HTTPConnection(host)
        connection.request("GET", "/search/?q=" + str(sen_name))
        response = connection.getresponse()

        self.assertTrue(response.status == 200)
        #self.assertTrue(json.loads(response.read().decode("utf-8")))
        connection.close()

        connection = senators_delete(sen_id)
        self.assertTrue(connection.getresponse().status == 204)
        connection.close()



    def test_bills_search(self) :
        connection = bills_post()
        bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
        bill_name = json.loads(connection.getresponse().read().decode("utf-8"))['name']
        connection.close()

        connection = httplib.HTTPConnection(host)
        connection.request("GET", "/search/?q=" + str(bill_name))
        response = connection.getresponse()

        self.assertTrue(response.status == 200)
        #self.assertTrue(json.loads(response.read().decode("utf-8")))
        connection.close()

        connection = bills_delete(bill_id)
        self.assertTrue(connection.getresponse().status == 204)
        connection.close()


    def test_committees_search(self) :
        connection = committees_post()
        committee_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
        com_name = json.loads(connection.getresponse().read().decode("utf-8"))['name']
        connection.close()

        connection = httplib.HTTPConnection(host)
        connection.request("GET", "/search/?q=" + str(com_name))
        response = connection.getresponse()

        self.assertTrue(response.status == 200)
        #self.assertTrue(json.loads(response.read().decode("utf-8")))
        connection.close()

        connection = committees_delete(committee_id)
        self.assertTrue(connection.getresponse().status == 204)
        connection.close()
