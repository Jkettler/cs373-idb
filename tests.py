#!/usr/bin/env python3

import unittest
import http.client
import urllib.parse
import json

class tests (unittest.TestCase) : 

	"""
	Tests for the Senator class
	"""
	def test_senators_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/senators")
		response = connection.getresponse()
		
		desired_body = [
		  {
		      "id": 1,
		      "name": "Jane Nelson",
		      "party": "Republican",
		      "occupation": "Businesswoman, former teacher",
		      "legistlative_experience": "Disaster Relief",
		      "district": "12",
		      "twitter": "https://twitter.com/SenJaneNelson",
		      "facebook": "https://www.facebook.com/SenatorJaneNelson",
		      "picture": "none",
		      "committees": [1,2]
		  }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_senators_post(self) : 
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps([
		  {
		      "name": "Jane Nelson",
		      "party": "Republican",
		      "occupation": "Businesswoman, former teacher",
		      "legistlative_experience": "Disaster Relief",
		      "district": "12",
		      "twitter": "https://twitter.com/SenJaneNelson",
		      "facebook": "https://www.facebook.com/SenatorJaneNelson",
		      "picture": "none",
		      "committees": [1,2]
		  }
		])
		headers = {"Content-Type": "application/json"}
		connection.request("POST", "/api/senators", values, headers)
		response = connection.getresponse()
		desired_body = { "id": 1 }

		self.assertTrue(response.status == 201)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_senators_id_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/senators/{id}")
		response = connection.getresponse()
		desired_body = {
		    "id": 1,
		    "name": "Jane Nelson",
		    "party": "Republican",
		    "occupation": "Businesswoman, former teacher",
		    "legistlative_experience": "Disaster Relief",
		    "district": "12",
		    "twitter": "https://twitter.com/SenJaneNelson",
		    "facebook": "https://www.facebook.com/SenatorJaneNelson",
		    "picture": "none",
		    "committees": [1,2]
		}	
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_senators_id_put(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps([
			{
		      "id": 1,
		      "name": "Jane Nelson",
		      "party": "Republican",
		      "occupation": "Businesswoman, former teacher",
		      "legistlative_experience": "Disaster Relief",
		      "district": "12",
		      "twitter": "https://twitter.com/SenJaneNelson",
		      "facebook": "https://www.facebook.com/SenatorJaneNelson",
		      "picture": "none",
		      "committees": [1,2]
			}
		])
		headers = {"Content-Type": "application/json"}
		connection.request("PUT", "/api/senators/{id}", values)
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()


	def test_senators_id_delete(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("DELETE", "/api/senators/{id}")
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()

	def test_senators_id_committees(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/senators/{id}/committees")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "Health & Human Services",
		        "chair": 1,
		        "vice_chair": [2],
		        "description": "NONE",
		        "appointment_Date": "2013-01-08",
		        "senators": [1]
		    }, 
		    {
		        "id": 2,
		        "name": "Finance",
		        "chair": 3,
		        "vice_chair": [4],
		        "description": "NONE",
		        "appointment_Date": "2013-01-08",
		        "senators": [1,2]
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_senators_id_bills(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/senators/{id}/bills")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "SB 63",
		        "author": [1],
		        "legislative_session": "83(R)",
		        "date_proposed": "11/12/2012",
		        "date_signed": "6/14/2013",
		        "date_effective": "6/14/2013",
		        "status": "Signed into law",
		        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		        "primary_committee": 1,
		        "Description": "Relating to consent to the immunization of certain children.",
		        "votes": {"1": "AYE","2": "NAY"}
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8"))== desired_body)
		connection.close()


















	"""
	Tests for the Bill class
	"""
	def test_bills_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/bills")
		response = connection.getresponse()
		desired_body = [
		    {
		        "id": 1,
		        "name": "SB 63",
		        "author": [1],
		        "legislative_session": "83(R)",
		        "date_proposed": "11/12/2012",
		        "date_signed": "6/14/2013",
		        "date_effective": "6/14/2013",
		        "status": "Signed into law",
		        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		        "primary_committee": 1,
		        "Description": "Relating to consent to the immunization of certain children.",
		        "votes": {"1": "AYE", "2": "NAY"}
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_bills_post(self) : 
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps([
		    {
		        "name": "SB 63",
		        "author": [1],
		        "legislative_session": "83(R)",
		        "date_proposed": "11/12/2012",
		        "date_signed": "6/14/2013",
		        "date_effective": "6/14/2013",
		        "status": "Signed into law",
		        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		        "primary_committee": 1,
		        "Description": "Relating to consent to the immunization of certain children.",
		        "votes": {1: "AYE",2: "NAY"}
		    }
		])
		headers = {"Content-Type": "application/json"}
		connection.request("POST", "/api/bills", values, headers)
		response = connection.getresponse()
		desired_body = {"id": 1 }

		self.assertTrue(response.status == 201)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_bills_id_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/bills/{id}")
		response = connection.getresponse()
		desired_body = {
		    "id": 1,
		    "name": "SB 63",
		    "author": [1],
		    "legislative_session": "83(R)",
		    "date_proposed": "11/12/2012",
		    "date_signed": "6/14/2013",
		    "date_effective": "6/14/2013",
		    "status": "Signed into law",
		    "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		    "primary_committee": 1,
		    "Description": "Relating to consent to the immunization of certain children.",
		    "votes": {"1": "AYE", "2": "NAY"}
		}	
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_bills_id_put(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps({
		        "id": 1,
		        "name": "SB 63",
		        "author": [1],
		        "legislative_session": "83(R)",
		        "date_proposed": "11/12/2012",
		        "date_signed": "6/14/2013",
		        "date_effective": "6/14/2013",
		        "status": "Signed into law",
		        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		        "primary_committee": 1,
		        "Description": "Relating to consent to the immunization of certain children.",
		        "votes": {1: "AYE",2: "NAY"}
		})
		headers = {"Content-Type": "application/json"}
		connection.request("PUT", "/api/bills/{id}", values)
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()


	def test_bills_id_delete(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("DELETE", "/api/bills/{id}")
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()

	def test_bills_id_senators(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/bills/{id}/senators")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "Jane Nelson",
		        "party": "Republican",
		        "occupation": "Businesswoman, former teacher",
		        "legistlative_experience": "Disaster Relief",
		        "district": "12",
		        "twitter": "https://twitter.com/SenJaneNelson",
		        "facebook": "https://www.facebook.com/SenatorJaneNelson",
		        "picture": "none",
		        "committees": [1,2]
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()

	def test_bills_id_authors(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/bills/{id}/authors")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "Jane Nelson",
		        "party": "Republican",
		        "occupation": "Businesswoman, former teacher",
		        "legistlative_experience": "Disaster Relief",
		        "district": "12",
		        "twitter": "https://twitter.com/SenJaneNelson",
		        "facebook": "https://www.facebook.com/SenatorJaneNelson",
		        "picture": "none",
		        "committees": [1,2]
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()












	"""
	Tests for the committees class
	"""
	def test_committees_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/committees")
		response = connection.getresponse()
		desired_body = [
		    {
		        "id": 1,
		        "name": "Health & Human Services",
		        "chair": 1,
		        "vice_chair": [2],
		        "description": "NONE",
		        "appointment_Date": "2013-01-08",
		        "senators": [1]
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_committees_post(self) : 
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps({
	        "name": "Health & Human Services",
	        "chair": 1,
	        "vice_chair": [2],
	        "description": "NONE",
	        "appointment_Date": "2013-01-08",
	        "senators": [1]
		})
		headers = {"Content-Type": "application/json"}
		connection.request("POST", "/api/committees", values, headers)
		response = connection.getresponse()
		desired_body = {"id": 1 }

		self.assertTrue(response.status == 201)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_committees_id_get(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/committees/{id}")
		response = connection.getresponse()
		desired_body = {
		    "id": 1,
		    "name": "Health & Human Services",
		    "chair": 1,
		    "vice_chair": [2],
		    "description": "NONE",
		    "appointment_Date": "2013-01-08",
		    "senators": [1]
		}	
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_committees_id_put(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = json.dumps({
		    "id": 1,
		    "name": "Health & Human Services",
		    "chair": 1,
		    "vice_chair": [2],
		    "description": "NONE",
		    "appointment_Date": "2013-01-08",
		    "senators": [1]
		})
		headers = {"Content-Type": "application/json"}
		connection.request("PUT", "/api/committees/{id}", values)
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()


	def test_committees_id_delete(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("DELETE", "/api/committees/{id}")
		response = connection.getresponse()
		
		self.assertTrue(response.status == 204)
		connection.close()

	def test_committees_id_senators(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/committees/{id}/senators")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "Jane Nelson",
		        "party": "Republican",
		        "occupation": "Businesswoman, former teacher",
		        "legistlative_experience": "Disaster Relief",
		        "district": "12",
		        "twitter": "https://twitter.com/SenJaneNelson",
		        "facebook": "https://www.facebook.com/SenatorJaneNelson",
		        "picture": "none",
		        "committees": [1,2]
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()


	def test_committees_id_bills(self) :
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		connection.request("GET", "/api/committees/{id}/bills")
		response = connection.getresponse()

		desired_body = [
		    {
		        "id": 1,
		        "name": "SB 63",
		        "author": [1],
		        "legislative_session": "83(R)",
		        "date_proposed": "11/12/2012",
		        "date_signed": "6/14/2013",
		        "date_effective": "6/14/2013",
		        "status": "Signed into law",
		        "url": "http://www.legis.state.tx.us/BillLookup/History.aspx?LegSess=83R&Bill=SB63",
		        "primary_committee": 1,
		        "Description": "Relating to consent to the immunization of certain children.",
		        "votes": {"1": "AYE", "2": "NAY"}
		    }
		]
		self.assertTrue(response.status == 200)
		self.assertTrue(json.loads(response.read().decode("utf-8")) == desired_body)
		connection.close()







unittest.main()


