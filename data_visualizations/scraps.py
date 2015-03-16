import requests
import json


# requests.get('https://api.github.com/repos/glass-bead-labs/sensor-group/issues').json()

# r is a list filled with dictionaries

timeCreated = r[0]['created_at']


# To get all the open and closed issues
myParams = {'state': 'all', 'per_page': 100}
r = requests.get('https://api.github.com/repos/glass-bead-labs/sensor-group/issues', params=myParams).json()


r[i]['user']['login'] #who created the issue


######### IMPORTANT #########
# who created issue
# closed and open ones
# number of comments
# people assigned?




###############################