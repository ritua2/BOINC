#!/usr/bin/env python3

"""
BASICS

Creates organization wide tokens, to be used when organization users apply for a token
"""


import hashlib
import redis
import random
import sys



r = redis.Redis(host = '0.0.0.0', port = 6389, db = 3)

# Each organization requires the following data
# Name: Name of the organization, same as the key by default
# No. Users: Total number of users
# Data Plans: Max number of GB allowed per user
# Allowed users: Maximum number of authorized users from this address
# Token: Actual token
# Users: A dictionary with all the current users {Name, Last name, Email}
# Email_Term: All the allowed email terminations

Org_Name = str(input("Organization name: "))

if Org_Name == "ORGS":
	print("Cannot name an organization 'ORGS', it is already a system inner index")
	sys.exit()



Data_Plan = str(input("Max. allowed storage for each user: "))
if float(Data_Plan) < 0:
    print("Invalid, users cannot have negative allocations")
    raise SyntaxError

Allowed_Users = str(input("Max. number of users allowed for this organization: "))
given_password = str(input("Enter org password to add users: "))
orgtok = hashlib.sha256(given_password.encode('UTF-8')).hexdigest()


ORG_DATA = {'Name':Org_Name, 'No. Users':'0', 'Data Plan':Data_Plan, 'Allowed Users':Allowed_Users,
           'Organization Token':orgtok, 'Users':'{}'}


print("New organization created: "+str(Org_Name))
r.hmset(Org_Name, ORG_DATA)
# Organizes them as ORG: Org. token
r.hset("ORGS", Org_Name, orgtok)
