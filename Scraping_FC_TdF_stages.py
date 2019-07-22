#!/usr/bin/env python
# coding: utf-8


# Importing libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Loop over all the TdF stages

for stage in range(1,15):
    if stage <=9 and stage!=2:
        # Send request to the page to scrap
        website_url = requests.get('https://firstcycling.com/race.php?r=17&y=2019&k=stages&e=0'+str(stage)).text

        # Parsing page
        soup = BeautifulSoup(website_url,'lxml')

        # Extract the table from the page
        My_table = soup.find('table',{'class':'sortTabell tablesorter'})

        # Find the rows where the cyclists' names and teams are, as well as the arrival times
        rider_names_team = My_table.find_all('a')
        times = My_table.find_all('span')

        # Extract the cyclists' names, teams, and time of arrival from the information obtained above
        Cyclists_team = []
        for a in rider_names_team:
            Cyclists_team.append(a.get('title'))
    
        time_arrival = []
        for b in times:    
            time_arrival.append(str(b.text))
    
        # Store everything into a pandas dataframe
        results_frame = pd.DataFrame()
        results_frame["Cyclist"] = Cyclists_team[0::2]
        results_frame["Team"] = Cyclists_team[1::2]
        results_frame["Time"] = time_arrival

        # Standardizing time delays
        for k in range(1,len(results_frame["Time"])):
            if len(results_frame["Time"][k])<=4:
                results_frame["Time"][k] = '+ 00:'+ results_frame["Time"][k][len(results_frame["Time"][k])-2:len(results_frame["Time"][k])]

        # Print the frame for check
        # print(results_frame)
        
        # Save everything into an excel file
        results_frame.to_excel(r'C:\Users\i.dalbo\Desktop\Data_Science\Cycling\results_stage_0'+str(stage)+'.xlsx')
        del results_frame, website_url, soup, My_table, rider_names_team, times, Cyclists_team, time_arrival
        
    elif stage == 2:    
        # Send request to the page to scrap
        website_url = requests.get('https://firstcycling.com/race.php?r=17&y=2019&k=stages&e=0'+str(stage)).text

        # Parsing page
        soup = BeautifulSoup(website_url,'lxml')

        # Extract the table from the page
        My_table = soup.find('table',{'class':'sortTabell tablesorter'})

        # Find the rows where the cyclists' names and teams are, as well as the arrival times
        rider_names_team = My_table.find_all('a')
        times = My_table.find_all('span')

        # Find the rows where the cyclists' names and teams are, as well as the arrival times
        rider_names_team = My_table.find_all('a')
        times = My_table.find_all('td')

       # Extract the cyclists' names, teams, and time of arrival from the information obtained above
        Cyclists_team = []
        for a in rider_names_team:
            Cyclists_team.append(a.get('title'))
        Cyclists_team = Cyclists_team[0::9]  
            
        times = times[2::5]    
        time_arrival = []
        for b in times:    
            time_arrival.append(str(b.text)) 
    
        # Store everything into a pandas dataframe
        results_frame = pd.DataFrame()
        results_frame["Team"] = Cyclists_team
        results_frame["Time"] = time_arrival

        # Standardizing time delays
        for k in range(1,len(results_frame["Time"])):
            if len(results_frame["Time"][k])<=4:
                results_frame["Time"][k] = '+ 00:'+ results_frame["Time"][k][len(results_frame["Time"][k])-2:len(results_frame["Time"][k])]

        # Print the frame for check
        # print(results_frame)
        
        # Save everything into an excel file
        results_frame.to_excel(r'C:\Users\i.dalbo\Desktop\Data_Science\Cycling\results_stage_0'+str(stage)+'.xlsx')
        del results_frame, website_url, soup, My_table, rider_names_team, times, Cyclists_team, time_arrival
    
    else:

        # Send request to the page to scrap
        website_url = requests.get('https://firstcycling.com/race.php?r=17&y=2019&k=stages&e='+str(stage)).text

        # Parsing page
        soup = BeautifulSoup(website_url,'lxml')

        # Extract the table from the page
        My_table = soup.find('table',{'class':'sortTabell tablesorter'})

        # Find the rows where the cyclists' names and teams are, as well as the arrival times
        rider_names_team = My_table.find_all('a')
        times = My_table.find_all('span')

        # Extract the cyclists' names, teams, and time of arrival from the information obtained above
        Cyclists_team = []
        for a in rider_names_team:
            Cyclists_team.append(a.get('title'))
    
        time_arrival = []
        for b in times:    
            time_arrival.append(str(b.text))
    
        # Store everything into a pandas dataframe
        results_frame = pd.DataFrame()
        results_frame["Cyclist"] = Cyclists_team[0::2]
        results_frame["Team"] = Cyclists_team[1::2]
        results_frame["Time"] = time_arrival

        # Standardizing time delays
        for k in range(1,len(results_frame["Time"])):
            if len(results_frame["Time"][k])<=4:
                results_frame["Time"][k] = '+ 00:'+ results_frame["Time"][k][len(results_frame["Time"][k])-2:len(results_frame["Time"][k])]

        # Print the frame for check
        # print(results_frame)
        
        # Save everything into an excel file
        results_frame.to_excel(r'C:\Users\i.dalbo\Desktop\Data_Science\Cycling\results_stage_'+str(stage)+'.xlsx')
        del results_frame, website_url, soup, My_table, rider_names_team, times, Cyclists_team, time_arrival

		
		