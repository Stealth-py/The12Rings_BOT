import requests
from bs4 import BeautifulSoup

link_cr = 'https://www.the12rings.com'


def lead_webcr(usr_id):
    page = '/login'
    url = link_cr + page
    credentials = {                                                              # enter your credentials, which you are going to push to the site to get to the leaderboard
        'email': '<username>',                           # enter username
        'password': '<password>'                                  # enter password
    }
    text = ''
    res = []
    lvl = 0
    with requests.Session() as s:                                 # create a session using "requests"
        p = s.post(url, data=credentials)                         # push the "credentials" to the login page
        source = s.get(link_cr + '/leaderboard')                  # go to the leaderboard
        plaintext = source.text                                   # extract the source code of that page
        bsoup = BeautifulSoup(plaintext, features="html.parser")       # this object represents the parsed plaintext as html
        f = open("bruh.txt", "w")                                 # open a text file, where the program will save the data about the user's lvl
        for data_lead in bsoup.findAll(attrs={'id': 'tableData'}):         # find the leaderboard data from the source code 
            text += str(data_lead)
        text = text.replace('<div id="tableData" style="display:none;">[', '')       # removing the unnecessary commands from the text
        text = text.replace(']</div>', '')
        f.write(text)                                                           # write the data to the file
        f.close()                                                               # close the file
        temp = ''
        for i in range(len(text)):                                             # split the table data into multiple dictionaries and store them as list
            if text[i] == '{':                                  # example: '{<something here>: <something else here>}`
                temp += text[i]
            elif text[i] == '}':
                temp += text[i]
                res.append(temp)
                temp = ''
            if '{' in temp and text[i] != '{':
                temp += text[i]

        flag = False
        for i in res:
            x = eval(i)                                                # use the string as a dictionary using eval() function of python
            if x["id"] == usr_id:                              # if the id from the table matches the entered user id
                print("The Level of {} is {}".format(usr_id, x["in_level"]))            # print the level to the IDE
                flag = True
                lvl = x["in_level"]
                break
        if not flag:                                                  # if the id is not in the leaderboard, then it doesn't exist
            print("The 12r id {} doesn't exist".format(usr_id))
    return lvl
