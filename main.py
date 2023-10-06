from bs4 import BeautifulSoup
import requests as rt
import pandas as pd

url = 'https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx'
params = {
    #"ctl00$ContentPlaceHolder1$ddlroundno": 
    "ctl00$ContentPlaceHolder1$ddlInstype": "ALL",
    "ctl00$ContentPlaceHolder1$ddlInstitute": "ALL",
    "ctl00$ContentPlaceHolder1$ddlBranch": "ALL",
    "ctl00$ContentPlaceHolder1$ddlSeatType": "ALL",
    "ctl00$ContentPlaceHolder1$btnSubmit": "Submit"
}

years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
rounds = ['1', '2', '3', '4', '5', '6', '7']

def scrape(Year, Round):   
    with rt.Session() as s:
        R = s.get(url)
        data = {}

        data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'lxml').select('input[name^=__]')})
        data["ctl00$ContentPlaceHolder1$ddlYear"] = Year
        R = s.post(url, data=data)

        data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'lxml').select('input[name^=__]')})
        data["ctl00$ContentPlaceHolder1$ddlroundno"] = Round
        R = s.post(url, data=data)

        for key, value in params.items():
            data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'lxml').select('input[name^=__]')})
            data[key] = value
            R = s.post(url, data=data)
        #print(R.text)
        #print(data)

    table = BeautifulSoup(R.text, 'lxml').find(id = 'ctl00_ContentPlaceHolder1_GridView1')
    df = pd.read_html(table.prettify())[0]
    df.dropna(inplace = True, how="all")
    
    df['Year'] = Year
    df['Round'] = Round
    #df['Opening Rank'] = df['Opening Rank'].astype(int)
    #df['Closing Rank'] = df['Closing Rank'].astype(int)
    
    return df

df = scrape('2020', '6')
#print(df)

open = df.loc[(df['Seat Type']=='OPEN')& (df['Gender']=='Gender-Neutral') & (df.Quota=='AI')]
open['Opening Rank'] = open['Opening Rank'].astype(int)
open['Closing Rank'] = open['Closing Rank'].astype(int)
#open

open = open.sort_values('Opening Rank')
print(open.head(40))