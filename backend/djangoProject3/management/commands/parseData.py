from django.core.management.base import BaseCommand
from djangoProject3.models import Player_Status
from djangoProject3.models import Team_Status

import re
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        f= open("/home/riccardo-cecco/projects/CCBDA-Project/scrapy/transfermarkt.json")
        data= json.load(f)
        for i in data:
            #Team
            if(len(i) <7):
                nameTeam=i['squad_name']
                year=i['year']
                avgAge=i['avg_age']
                if(avgAge==-1):
                    print("avgAge")
                valueTeam = i['squad_value']
                numberPlayers = i['number_players']
                championship=i['championship']
                Team_Status.objects.create(nameTeam = nameTeam, nameLeague= championship, year = year,avgAge= avgAge,valueTeam = valueTeam, numberPlayers = numberPlayers)
            #Player
            elif (len(i) >9):
                namePlayer=i['name_player']
                age=i['age']
                role = i['role']
                year=i['year']
                valuePlayer = i['value_player']
                nameTeam = i['squad_name']
                games=i['games_played']
                minutes = i['minute_played']
                championship = i['championship']
                if(i['role']=="Goalkeeper"):
                    cleanSheets=i['clean_sheets']
                    goalsConceded = i['goals_conceded']
                    goals=0
                    assists=0
                else:
                    cleanSheets = 0
                    goalsConceded = 0
                    goals =i['goals']
                    assists = i['assists']
                Player_Status.objects.create(namePlayer = namePlayer,
                                            nameTeam = nameTeam,
                                            nameLeague= championship,
                                            age = age,
                                            year = year,
                                            valuePlayer = valuePlayer,
                                            role = role,
                                            games = games,
                                            goals = goals,
                                            assists = assists,
                                            minutes = minutes,
                                            goalsConceded = goalsConceded,
                                            cleanSheets = cleanSheets)

            # Closing file
        f.close()

