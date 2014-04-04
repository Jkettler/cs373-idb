#!/usr/bin/env python3

import unittest
import http.client
import urllib.parse
import json

def senators_post():
	connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
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
			  "map": "<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3348.899273384878!2d-97.0779837!3d32.927259399999954!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864c2b26c440b8cb%3A0xe8f6fb2969de0ad!2s1235+S+Main+St+%23280!5e0!3m2!1sen!2sus!4v1395279135094\" width=\"400\" height=\"300\" frameborder=\"0\" style=\"border:0\"></iframe>",
			  "name": "Joan tests test",
			  "occupation": "Attorney",
			  "party": "Republican",
			  "twitter": "SenJaneNelson"
			})
	headers = {"Content-Type": "application/json"}
	connection.request("POST", "/api/senators/", values, headers)
	return connection

def senators_delete(sen_id):
	connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
	connection.request("DELETE", "/api/senators/" + str(sen_id) + "/")
	return connection


def bills_post():
	connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
	values = json.dumps(
    {
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
    }
	)

	headers = {"Content-Type": "application/json"}
	connection.request("POST", "/api/bills/", values, headers)
	return connection

def bills_delete(bill_id):
	connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
	connection.request("DELETE", "/api/bills/" + str(bill_id) + "/")
	return connection


class tests (unittest.TestCase) : 
	"""
	Tests for the Senator class
	"""

	def test_senators_post(self) : 
		connection = senators_post()
		response = connection.getresponse()
		response_body = json.loads(response.read().decode("utf-8"))
		self.assertTrue(response.status == 201)
		self.assertTrue("id" in response_body)
		sen_id = response_body['id']
		connection.close()

		senators_delete(sen_id).close()


	def test_senators_id_delete(self) :
		connection = senators_post()
		sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()

		connection = senators_delete(sen_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_senators_get(self) :
		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/senators/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		connection.close()

	def test_senators_id_get(self) :
		connection = senators_post()
		sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()		

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/senators/" + str(sen_id) + "/")
		response = connection.getresponse()
		desired_body = {
		  "bills": [
		    1
		  ],
		  "committees": [
		    1
		  ],
		  "district": 17,
		  "facebook": "https://www.facebook.com/SenatorJaneNelson",
		  "id": sen_id,
		  "legislative_experience": "Senate Member, December 2008 - present",
		  "map": "<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3348.899273384878!2d-97.0779837!3d32.927259399999954!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864c2b26c440b8cb%3A0xe8f6fb2969de0ad!2s1235+S+Main+St+%23280!5e0!3m2!1sen!2sus!4v1395279135094\" width=\"400\" height=\"300\" frameborder=\"0\" style=\"border:0\"></iframe>",
		  "name": "Joan tests test",
		  "occupation": "Attorney",
		  "party": "Republican",
		  "twitter": "SenJaneNelson"
		}
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_senators_id_put(self) :
		connection = senators_post()
		sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		values = json.dumps({
		  "bills": [
		    1
		  ],
		  "committees": [
		    1
		  ],
		  "district": 20,
		  "facebook": "https://www.facebook.com/SenatorJaneNelson",
		  "id": sen_id,
		  "legislative_experience": "Senate Member, December 2008 - present",
		  "map": "<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3348.899273384878!2d-97.0779837!3d32.927259399999954!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864c2b26c440b8cb%3A0xe8f6fb2969de0ad!2s1235+S+Main+St+%23280!5e0!3m2!1sen!2sus!4v1395279135094\" width=\"400\" height=\"300\" frameborder=\"0\" style=\"border:0\"></iframe>",
		  "name": "Joan tests test",
		  "occupation": "Attorney",
		  "party": "Republican",
		  "twitter": "SenJaneNelson"
		})
		headers = {"Content-Type": "application/json"}

		connection.request("PUT", "/api/senators/" + str(sen_id) + "/", values, headers)		
		response = connection.getresponse()
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8"))['district']== 20)

		connection.close()

		connection = senators_delete(sen_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_senators_id_committees(self) :
		connection = senators_post()
		sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/senators/" + str(sen_id) + "/committees/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		response_list = json.loads(response.read().decode("utf-8"))
		self.assertTrue(response_list[0]['pk'] == 1)
		connection.close()

		connection = senators_delete(sen_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_senators_id_bills(self) :
		connection = senators_post()
		sen_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/senators/" + str(sen_id) + "/bills/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		response_list = json.loads(response.read().decode("utf-8"))
		self.assertTrue(response_list[0]['pk'] == 1)
		connection.close()

		connection = senators_delete(sen_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()











	def test_bills_post(self) : 
		connection = bills_post()
		response = connection.getresponse()
		response_body = json.loads(response.read().decode("utf-8"))
		self.assertTrue(response.status == 201)
		self.assertTrue("id" in response_body)
		bill_id = response_body['id']
		connection.close()

		bills_delete(bill_id).close()


	def test_bills_id_delete(self) :
		connection = bills_post()
		bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()

		connection = bills_delete(bill_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_bills_get(self) :
		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/bills/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		connection.close()

	def test_bills_id_get(self) :
		connection = bills_post()
		bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()		

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/bills/" + str(bill_id) + "/")
		response = connection.getresponse()
		desired_body = 	{
	       "authors":
	       [
				1
	       ],
	       "id": bill_id,
	       "date_effective": "2013-06-14",
	       "date_proposed": "2012-11-12",
	       "date_signed": "2013-06-14",
	       "description": "Relating to consent to the immunization of certain children.",
	       "legislative_session": "83(R)",
	       "name": "SB 747 test",
	       "primary_committee": 1,
	       "status": "Signed into law",
	       "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63"
    	}
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_bills_id_put(self) :
		connection = bills_post()
		bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		values = json.dumps({
	       "authors":
	       [
				1
	       ],
	       "id": bill_id,
	       "date_effective": "2013-06-14",
	       "date_proposed": "2012-11-12",
	       "date_signed": "2013-06-14",
	       "description": "Relating to consent to eat cookies.",
	       "legislative_session": "83(R)",
	       "name": "SB 747 test",
	       "primary_committee": 1,
	       "status": "Signed into law",
	       "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63"
    	})
		headers = {"Content-Type": "application/json"}

		connection.request("PUT", "/api/bills/" + str(bill_id) + "/", values, headers)		
		response = connection.getresponse()
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8"))['description'] == "Relating to consent to eat cookies.")

		connection.close()

		connection = bills_delete(bill_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_bills_id_authors(self) :
		connection = bills_post()
		bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/bills/" + str(bill_id) + "/authors/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		response_list = json.loads(response.read().decode("utf-8"))
		self.assertTrue(response_list[0]['pk'] == 1)
		connection.close()

		connection = bills_delete(bill_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()

	def test_bills_id_votes(self) :
		connection = bills_post()
		bill_id = json.loads(connection.getresponse().read().decode("utf-8"))['id']
		connection.close()	

		connection = http.client.HTTPConnection("texaslawdb.herokuapp.com")
		connection.request("GET", "/api/bills/" + str(bill_id) + "/votes/")
		response = connection.getresponse()

		self.assertTrue(response.status == 200)
		response_list = json.loads(response.read().decode("utf-8"))
		connection.close()

		connection = bills_delete(bill_id)
		self.assertTrue(connection.getresponse().status == 204)
		connection.close()























	# """
	# Tests for the Bill class
	# """
	# def test_bills_get(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/bills")
	# 	response = connection.getresponse()
	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
	# 	        "name": "SB 63",
	# 	        "authors": [1],
	# 	        "legislative_session": "83(R)",
	# 	        "date_proposed": "11/12/2012",
	# 	        "date_signed": "6/14/2013",
	# 	        "date_effective": "6/14/2013",
	# 	        "status": "Signed into law",
	# 	        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
	# 	        "primary_committee": 1,
	# 	        "Description": "Relating to consent to the immunization of certain children.",
 #                "voters": [2, 3]
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_bills_post(self) : 
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	values = json.dumps(
	# 	    {
	# 	        "name": "SB 63",
	# 	        "authors": [1],
	# 	        "legislative_session": "83(R)",
	# 	        "date_proposed": "11/12/2012",
	# 	        "date_signed": "6/14/2013",
	# 	        "date_effective": "6/14/2013",
	# 	        "status": "Signed into law",
	# 	        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
	# 	        "primary_committee": 1,
	# 	        "Description": "Relating to consent to the immunization of certain children.",
 #                "voters": [2, 3]	    
 #            }
	# 	)
	# 	headers = {"Content-Type": "application/json"}
	# 	connection.request("POST", "/api/bills", values, headers)
	# 	response = connection.getresponse()
	# 	desired_body = {"id": 1 }

	# 	self.assertTrue(response.status == 201)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_bills_id_get(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/bills/{id}")
	# 	response = connection.getresponse()
	# 	desired_body = {
	# 	    "id": 1,
	# 	    "name": "SB 63",
	# 	    "authors": [1],
	# 	    "legislative_session": "83(R)",
	# 	    "date_proposed": "11/12/2012",
	# 	    "date_signed": "6/14/2013",
	# 	    "date_effective": "6/14/2013",
	# 	    "status": "Signed into law",
	# 	    "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
	# 	    "primary_committee": 1,
	# 	    "Description": "Relating to consent to the immunization of certain children.",
	# 	    "voters": [2, 3]
	# 	}	
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_bills_id_put(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	values = json.dumps({
	# 	        "id": 1,
	# 	        "name": "SB 63",
	# 	        "authors": [1],
	# 	        "legislative_session": "83(R)",
	# 	        "date_proposed": "11/12/2012",
	# 	        "date_signed": "6/14/2013",
	# 	        "date_effective": "6/14/2013",
	# 	        "status": "Signed into law",
	# 	        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
	# 	        "primary_committee": 1,
	# 	        "Description": "Relating to consent to the immunization of certain children.",
 #                "voters": [2, 3]	
 #            })
	# 	headers = {"Content-Type": "application/json"}
	# 	connection.request("PUT", "/api/bills/{id}", values)
	# 	response = connection.getresponse()
		
	# 	self.assertTrue(response.status == 204)
	# 	connection.close()


	# def test_bills_id_delete(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("DELETE", "/api/bills/{id}")
	# 	response = connection.getresponse()
		
	# 	self.assertTrue(response.status == 204)
	# 	connection.close()

	# def test_bills_id_senators(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/bills/{id}/senators")
	# 	response = connection.getresponse()

	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
	# 	        "name": "Jane Nelson",
	# 	        "party": "Republican",
	# 	        "occupation": "Businesswoman, former teacher",
	# 	        "legistlative_experience": "Disaster Relief",
	# 	        "district": "12",
	# 	        "twitter": "SenJaneNelson",
	# 	        "facebook": "https://www.facebook.com/SenatorJaneNelson",
	# 	        "photo_url": "null",
 #            	"map": "null"
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()

	# def test_bills_id_authors(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/bills/{id}/authors")
	# 	response = connection.getresponse()

	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
	# 	        "name": "Jane Nelson",
	# 	        "party": "Republican",
	# 	        "occupation": "Businesswoman, former teacher",
	# 	        "legistlative_experience": "Disaster Relief",
	# 	        "district": "12",
	# 	        "twitter": "SenJaneNelson",
	# 	        "facebook": "https://www.facebook.com/SenatorJaneNelson",
	# 			"photo_url": "null",
 #            	"map": "null"
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()












	# """
	# Tests for the committees class
	# """
	# def test_committees_get(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/committees")
	# 	response = connection.getresponse()
	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
	# 	        "name": "Health & Human Services",
	# 	        "chair": 1,
	# 	        "vice_chair": 2,
	# 	        "description": "null",
	# 	        "appointment_Date": "2013-01-08",
	# 	        "senators": [1]
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_committees_post(self) : 
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	values = json.dumps({
	#         "name": "Health & Human Services",
	#         "chair": 1,
	#         "vice_chair": 2,
	#         "description": "null",
	#         "appointment_Date": "2013-01-08",
	#         "senators": [1]
	# 	})
	# 	headers = {"Content-Type": "application/json"}
	# 	connection.request("POST", "/api/committees", values, headers)
	# 	response = connection.getresponse()
	# 	desired_body = {"id": 1 }

	# 	self.assertTrue(response.status == 201)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_committees_id_get(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/committees/{id}")
	# 	response = connection.getresponse()
	# 	desired_body = {
	# 	    "id": 1,
	# 	    "name": "Health & Human Services",
	# 	    "chair": 1,
	# 	    "vice_chair": 2,
	# 	    "description": "null",
	# 	    "appointment_Date": "2013-01-08",
	# 	    "senators": [1]
	# 	}	
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_committees_id_put(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	values = json.dumps({
	# 	    "id": 1,
	# 	    "name": "Health & Human Services",
	# 	    "chair": 1,
	# 	    "vice_chair": 2,
	# 	    "description": "null",
	# 	    "appointment_Date": "2013-01-08",
	# 	    "senators": [1]
	# 	})
	# 	headers = {"Content-Type": "application/json"}
	# 	connection.request("PUT", "/api/committees/{id}", values)
	# 	response = connection.getresponse()
		
	# 	self.assertTrue(response.status == 204)
	# 	connection.close()


	# def test_committees_id_delete(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("DELETE", "/api/committees/{id}")
	# 	response = connection.getresponse()
		
	# 	self.assertTrue(response.status == 204)
	# 	connection.close()

	# def test_committees_id_senators(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/committees/{id}/senators")
	# 	response = connection.getresponse()

	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
	# 	        "name": "Jane Nelson",
	# 	        "party": "Republican",
	# 	        "occupation": "Businesswoman, former teacher",
	# 	        "legistlative_experience": "Disaster Relief",
	# 	        "district": "12",
	# 	        "twitter": "SenJaneNelson",
	# 	        "facebook": "https://www.facebook.com/SenatorJaneNelson",
	# 	        "photo_url": "null",
 #           		"map": "null"
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()


	# def test_committees_id_bills(self) :
	# 	connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
	# 	connection.request("GET", "/api/committees/{id}/bills")
	# 	response = connection.getresponse()

	# 	desired_body = [
	# 	    {
	# 	        "id": 1,
 #                "name": "SB 63",
 #                "authors": [1],
 #                "legislative_session": "83(R)",
 #                "date_proposed": "11/12/2012",
 #                "date_signed": "6/14/2013",
 #                "date_effective": "6/14/2013",
 #                "status": "Signed into law",
 #                "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
 #                "primary_committee": 1,
 #                "Description": "Relating to consent to the immunization of certain children.",
 #                "voters": [1, 2]
	# 	    }
	# 	]
	# 	self.assertTrue(response.status == 200)
	# 	self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
	# 	connection.close()







unittest.main()


