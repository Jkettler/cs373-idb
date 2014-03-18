#!/usr/bin/env python3

import unittest
import http.client

connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
class tests (unittest.TestCase) : 

	"""
	Tests for the Senator class
	"""
	def test_senators_get(self) :
		connection.request("GET", "/api/senators")
		response = connection.getresponse()
		desired_body = '''[\n    {\n        "id": 1,\n        "name": "Jane Nelson",\n        "party": "Republican",\n        "occupation": "Businesswoman, former teacher",\n        "legistlative_experience": "Disaster Relief",\n        "district": "12",\n        "twitter": "https://twitter.com/SenJaneNelson",\n        "facebook": "https://www.facebook.com/SenatorJaneNelson",\n        "picture": "none",\n        "committees": [1,2]\n    }\n]'''

		self.assertTrue(response.status == 200)
		self.assertTrue(response.read().decode("utf-8") == desired_body)
		connection.close()


"""
	def test_senators_post(self) : 
		connection = http.client.HTTPConnection("cs373idb2.apiary-mock.com")
		values = urllib.parse.urlencode([
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
		desired_body = '''{ 
												"id": 1 
											}'''
		self.assertTrue(response.status == 201)
		self.assertTrue(response.read().decode("utf-8") == desired_body)
		connection.close()
"""

unittest.main()
