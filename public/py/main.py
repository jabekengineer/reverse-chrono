def getBoardChecklists(_cardID, KEY, TOKEN):
    """get checklists from card of card"""
    import requests
    url = "https://api.trello.com/1/cards/"+_cardID+"/checklists"
    query = {
        'key': KEY, 
        'token': TOKEN
    }
    response = requests.request(
        "GET", 
        url,
        params=query
    )
    return response

def getBoardNamesAndIDs(KEY, TOKEN):
    """get boards assigned to user who owns key"""
    import requests
    urlBase = "https://api.trello.com/1/members/me/boards?fields=name,id" 
    headers = {
        "Accept": "application/json"
    }
    
    query = {
        "key": KEY, 
        'token': TOKEN
    }
    
    response = requests.request(
        "GET", 
        urlBase, 
        headers=headers, 
        params=query
    )
    return response

def getCards(boardID, KEY, TOKEN):
    """don't use get helper for some reason, probably scope or import issues"""
    import requests
    url = "https://api.trello.com/1/boards/"+boardID+"/cards"
    query = {
        "key": KEY, 
        'token': TOKEN
    }
    
    response = requests.request(
        "GET", 
        url,  
        params=query
    )
    return response

def displayResponse(response):
    """ apply standard formatting to view JSON response"""
    import json
    try: json.loads(response.text)
    except AttributeError:
        print('response was empty or not a valid curl response')
        return
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=3, separators=(",",": ")))
    return

def is_date(string):
    from dateutil.parser import parse
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    # Milestone notation M1 is ambiguous
    try: 
        parse(string, fuzzy=True)
        return True

    except:
        return False

def parseIdByName(response, name):
    """get id of top level response element matching name"""
    import json
    # is the response valid
    try:
        resp = json.loads(response.text)
    except AttributeError:
        print('response was empty or not a valid curl response')
        _elementID = None
        return _elementID
    except json.decoder.JSONDecodeError:
        print('your API KEY or TOKEN values were invalid.')
        _elementID = None
        return _elementID
    # is name a string?
    if(isinstance(name, str)):
        for element in resp:
            if element['name'] == name:
                _elementID = element['id']
                return _elementID
    else:
        _elementID = None

    return _elementID

def parseMilestoneDate(milestone):
    _parts = milestone.split('|')
    for _substring in _parts:
        if(is_date(_substring.strip()) and (_substring.find('M') == -1)):
            return _substring.strip()
    return

def putChecklistToCardTop(checklistID, KEY, TOKEN):
    """provide checklistID and move it to bottom"""
    import requests
    url = "https://api.trello.com/1/checklists/"+checklistID
    query = {
        'key': KEY, 
        'token': TOKEN,
        'pos': 'top'
    }
    response = requests.request(
        "PUT", 
        url, 
        params=query
    )
    return

def sortChecklistsByDate(response):
    """take card checklists names, extract name dates, and reorder the IDs"""
    import json
    from collections import OrderedDict
    import datetime
    # is the response valid
    try:
        resp = json.loads(response.text)
    except AttributeError:
        print('response was empty or not a valid curl response')
        sorted = None
        return sorted
    except json.decoder.JSONDecodeError:
        print('your API KEY or TOKEN values were invalid.')
        sorted = None
        return sorted
    # look through each json object in response array
    checklists = {}
    for obj in resp:
        try:
            _date = parseMilestoneDate(obj['name'])
        except AttributeError:
            print('json did not have key: "name"')
            return 
        if(_date):
            try:
                if not _date in checklists:
                    checklists[_date] = obj['id']
            except AttributeError:
                print('json did not have key: id')
                return
    # sort the date keys and reorder the dictionary
    listDates = checklists.keys()
    # sort my dates
    dates = [datetime.datetime.strptime(_date, "%m/%d/%Y") for _date in listDates]
    dates.sort()
    sortedDates = [datetime.datetime.strftime(_date, "%m/%d/%Y") for _date in dates]
    sortedChecklists = OrderedDict()
    for _date in sortedDates:
        sortedChecklists[_date] = checklists[_date]
    return sortedChecklists

def main():
    """make connection to my trello API"""
    from decouple import config,UndefinedValueError
    import sys
    
    
    try:
      cardID_p, boardID_p = sys.argv[1], sys.argv[2]
    except:
      print('system arguments are not here')      
    
    # retrieve environment constants
    try: 
        KEY = config('TRELLO_KEY')
        TOKEN = config('TRELLO_TOKEN')
    except UndefinedValueError:
        print('key and token string inputs to config their reference names in .env file, request not made!')
        return

    # get my boards
    response = getBoardNamesAndIDs(KEY, TOKEN)
    # extract Weekly Meetings Board
    # boardID = parseIdByName(response, 'JSPM')
    # Get the checklist ID
    if(boardID_p):
        # get cards of board
        response = getCards(boardID_p, KEY, TOKEN)
        # get weekly meeting card
        # cardID = parseIdByName(response, 'Trello-Side Features')
        # get card checklists and sort them
        response = getBoardChecklists(cardID_p, KEY, TOKEN)
        sortedChecklists = sortChecklistsByDate(response)
    # update the checklist
        for checklistID in sortedChecklists.values():
            putChecklistToCardTop(checklistID, KEY, TOKEN)
    return
  
if __name__ == "__main__":
    try: 
      main()
      print('Enjoy your checklists now sorted in reverse date order! -JS')
    except:
      print("Your data is safe! This is Jason's powerup to sort his meeting agenda checklists by date so you don't have to drag the newest one all the way to the top. If you want this or other trello card/board organization utilities to make your life easier, you can hit me up.")
    