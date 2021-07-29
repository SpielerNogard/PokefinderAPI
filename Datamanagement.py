
from Database_watcher import Database_Watcher
import config

class Datamanagement(object):
    def __init__(self):
        self.KEVIN = Database_Watcher()
        self.pokemon = []
        self.pokestops = []
        self.quests = []
        self.raids = []
        self.gyms = []
        self.gymdetails = []

    def get_all_data(self):

        #MAD Data
        SQL = "Select * from pokemon where DATE_ADD(disappear_time, INTERVAL 2 HOUR) > NOW();"  
        self.pokemon = self.KEVIN.read_data(SQL,config.MAD)
        SQL = "Select * from pokestop;"  
        self.pokestops = self.KEVIN.read_data(SQL,config.MAD)
        SQL = "Select * from trs_quest;"
        self.quests = self.KEVIN.read_data(SQL,config.MAD)  
        SQL = "Select * from raid where DATE_ADD(end, INTERVAL 2 HOUR) > NOW();" 
        self.raids = self.KEVIN.read_data(SQL,config.MAD) 
        SQL = "Select * from gym;"
        self.gyms = self.KEVIN.read_data(SQL,config.MAD)  
        SQL = "Select * from gymdetails;"
        self.gymdetails = self.KEVIN.read_data(SQL,config.MAD) 

        #Pokefinder Data
        


if __name__ == "__main__":
    DIALGA = Datamanagement()
    DIALGA.get_all_data()