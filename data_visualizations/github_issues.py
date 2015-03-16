import requests
import json

OWNER = 'glass-bead-labs'
REPO = 'sensor-group'


parameters = {'state': 'all', 'per_page': 100}
request = requests.get('https://api.github.com/repos/' + OWNER + '/' + REPO + '/issues', params=parameters).json()

# request is a list filled with dictionaries that represent each issue
# listed in the order seen on github repo

def getIndex(title):
    for i in range(len(request) - 1):
        if title == getTitle(i):
            return i
    


def getState(i):
    return str(request[i]['state'])

def getCreator(i):
    return str(request[i]['user']['login'])

def getTitle(i):
    return str(request[i]['title'])

def getLabels(i):
    if request[i]['labels'] != []:
        return str(request[i]['labels']['name'])


def getDateCreated(i):
    time = request[i]['created_at']
    if (time != None):
        timeStamp = str(time)
        month = int(timeStamp[5:7])
        day = int(timeStamp[8:10])
        return str(month) + '/' + str(day)

def getDateClosed(i):
    time = request[i]['closed_at']
    if (time != None):
        timeStamp = str(time)
        month = int(timeStamp[5:7])
        day = int(timeStamp[8:10])
        return str(month) + '/' + str(day)

def getDateUpdated(i):
    time = request[i]['updated_at']
    if (time != None):
        timeStamp = str(time)
        month = int(timeStamp[5:7])
        day = int(timeStamp[8:10])
        return str(month) + '/' + str(day)


def getNumComments(i):
    return int(request[i]['comments'])

    #color coded by creator, as time goes by put the issue on time line where num of comments on y 
    #axis , and if its open be like more prominent color but if not be more opaque
    #the title can be shown visible 

startDate = getDateCreated(len(request) - 1)
endDate = getDateCreated(0)

def totalComments():
    numComments = []
    comments = 0
    for i in range(len(request) - 1):
        comments += getNumComments(i)
        if (i != 0 and i%5 == 0):
            numComments.append(comments)
            comments = 0
    if (len(request) % 5 != 0):
        numComments.append(comments)
    return numComments

def datesOfIssues():
    dates = [getDateCreated(0)]
    for i in range(1, len(request) - 1):
        if (getDateCreated(i) not in dates):
            dates.append(getDateCreated(i))
    return dates[::-1]

def commentsPerDay():
    numComments = []
    comments = 0
    for k in range(len(datesOfIssues())):
        for i in range(len(request) - 1):
            if (getDateCreated(i) == datesOfIssues()[k]):
                comments += getNumComments(i)
        numComments.append(comments)
        comments = 0
    return numComments







data = []
for i in range(len(request) - 1):
    data.append({'issue': i, 'creator': getCreator(i), 'title': getTitle(i), 'dateCreated': getDateCreated(i), 'dateClosed': getDateClosed(i), 'dateUpdated': getDateUpdated(i), 'comments': getNumComments(i)})


with open ('github_issues.json', 'w') as outfile:
    json.dump(data, outfile, indent = 4)


data = []
data.append({'datesOfIssues': datesOfIssues() , 'numComments': commentsPerDay()})

for i in range(len(datesOfIssues()) - 1):
    data.append({datesOfIssues()[i]: commentsPerDay()[i]})


with open ('mydata.json', 'w') as outfile:
    json.dump(data, outfile, indent = 4)



    