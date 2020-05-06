import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

ORIGIN_URL = 'http://golfnationwide.com'

# initializing the columns of csv
CourseName_list = []
Street_list = []
City_list = []
State_list = []
County_list = []
ZipCode_list = []
Website_list = []
Email_list = []
Phone_list = []
GreenFeesWeekend_list = []
GreenFeesWeekday_list = []
YearBuilt_list = []
AnnualRounds_list = []
Manager_list = []
ClubPro_list = []
Superintendant_list = []
GuestPolicy_list = []
Holes_list = []

# Getting all States 
first_page = urlopen(ORIGIN_URL)
bsObj_1 = BeautifulSoup(first_page.read())
state_list = [ORIGIN_URL + i.find('a').get('href') for i in bsObj_1.findAll('td')]

# the function to get the detailed data from the course URL
def GetCourseInfo(course):
    course_page = urlopen(course)
    bsObj = BeautifulSoup(course_page.read())
    Basic_info = bsObj.find('span', attrs = {'id': 'Block'}).findAll('dd')
    Detail_info_1 = bsObj.find('div', attrs = {'id': 'DetailedBox'}).find('span', attrs = {'id': 'BlockOne'}).findAll('dd')
    Detail_info_2 = bsObj.find('div', attrs = {'id': 'DetailedBox'}).find('span', attrs = {'id': 'BlockTwo'}).findAll('dd')
    Course_info = bsObj.find('div', attrs = {'id': 'GreensBox'}).find('span', attrs = {'id': 'BlockOne'}).findAll('dd')
    CourseName = Basic_info[0].text
    Street = Basic_info[1].text.replace('\xa0', '')
    City = Basic_info[2].findAll('span')[0].text.replace('\xa0', '')
    State = Basic_info[2].findAll('span')[1].text.replace('\xa0', '')
    ZipCode = Basic_info[3].text.replace('\xa0', '')
    County = Basic_info[4].text.replace('\xa0', '')
    Email = Basic_info[5].text.replace('\xa0', '')
    Website = Basic_info[6].text.replace('\xa0', '')
    Phone = Basic_info[7].text.replace('\xa0', '')
    GreenFeesWeekend = Detail_info_2[0].text.replace('\xa0', '')
    GreenFeesWeekday = Detail_info_2[1].text.replace('\xa0', '')
    YearBuilt = Detail_info_1[1].text.replace('\xa0', '')
    AnnualRounds = Detail_info_1[2].text.replace('\xa0', '')
    Manager = Detail_info_1[4].text.replace('\xa0', '')
    ClubPro = Detail_info_1[5].text.replace('\xa0', '')
    Superintendant = Detail_info_1[6].text.replace('\xa0', '')
    GuestPolicy = Detail_info_1[7].text.replace('\xa0', '')
    Holes = Course_info[0].text.replace('\xa0', '')
    return CourseName,Street,City,State,ZipCode,County,Email,Website,Phone,GreenFeesWeekend,GreenFeesWeekday,YearBuilt,AnnualRounds,Manager,ClubPro,Superintendant,GuestPolicy,Holes

# print(GetCourseInfo(COURSE))
# Getting URLs of all courses
course_list = [] 
for state in state_list:
    stage_page = urlopen(state)
    bsObj_2 = BeautifulSoup(stage_page.read())
    
    cand_list = bsObj_2.findAll('td')
    for ind in range(len(cand_list)):
        if (ind % 2 == 0):
            course_list.append(ORIGIN_URL + cand_list[ind].find('a').get('href'))
    #print(course_list)
    
# Getting Data in each course
for course in course_list:
    print('-----',course, '-----')
    CourseName,Street,City,State,County,ZipCode,Website,Email,Phone,GreenFeesWeekend,GreenFeesWeekday,YearBuilt,AnnualRounds,Manager,ClubPro,Superintendant,GuestPolicy,Holes = GetCourseInfo(course)
    print(CourseName,Street,City,State,County,ZipCode,Website,Email,Phone,GreenFeesWeekend,GreenFeesWeekday,YearBuilt,AnnualRounds,Manager,ClubPro,Superintendant,GuestPolicy,Holes)
    CourseName_list.append(CourseName)
    Street_list.append(Street)
    City_list.append(City)
    State_list.append(State)
    County_list.append(County)
    ZipCode_list.append(ZipCode)
    Website_list.append(Website)
    Email_list.append(Email)
    Phone_list.append(Phone)
    GreenFeesWeekend_list.append(GreenFeesWeekend)
    GreenFeesWeekday_list.append(GreenFeesWeekday)
    YearBuilt_list.append(YearBuilt)
    AnnualRounds_list.append(AnnualRounds)
    Manager_list.append(Manager)
    ClubPro_list.append(ClubPro)
    Superintendant_list.append(Superintendant)
    GuestPolicy_list.append(GuestPolicy)
    Holes_list.append(Holes)
    time.sleep(3)

# Writing the data to the csv file
dict = {'Course Name':CourseName_list,'State':State_list,'County':County_list,'City':City_list,'Street':Street_list,'Zip Code':ZipCode_list,'Website':Website_link,'Email':Email_list,'Phone':Phone_list,'Green Fees Weekend':GreenFeesWeekend_list,'Green Fees Weekday':GreenFeesWeekday_list,'Year Built':YearBuilt_list,'Annual Rounds':AnnualRounds_list,'Manager':Manager_list,'Club Pro':ClubPro_list,'Superintendant':Superintendant_list,'Guest Policy':GuestPolicy_list,'Holes':Holes_list}
df = pd.DataFrame(dict)
df.to_csv('result.csv')