#filename:classes.py
#Author:Lim Ah Seng
#Centre no/Index no: 3024
#Description: Support classes for music library

''' Super Class Resource '''
class Resource:
    
    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType
        
    ''' Resource number accessor '''    
    def getResourceNo(self):
        return self.__ResourceNo
    
    ''' Title accessor '''    
    def getTitle(self):
        return self.__Title
    
    ''' Date Acquired accessor '''    
    def getDateAcquired(self):
        return self.__DateAcquired
    
    ''' Resource Type number accessor '''    
    def getResourceType(self):
        return self.__ResourceType

    ''' title modifier '''    
    def setTitle(self, newTitle):
        self.__Title = newTitle
        
    ''' date acquired modifier '''    
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired
        
    ''' ResourceType modifier '''    
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Display Helper Method'''
    def display(self):
        return "{0:6}{1:25s}{2:7s}{3:2}".format\
               (self.getResourceNo(),self.getTitle(),self.getDateAcquired(),self.getResourceType())

''' Sub Class Resource '''
class MusicCD(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)#calling superclass constuctor
        self.__Artist = Artist #subclass constructors 
        self.__NoOfTracks = NoOfTracks
        
    ''' Artist accessor '''    
    def getArtist(self):
        return self.__Artist
    
    ''' NoOfTracks accessor '''    
    def getNoOfTracks(self):
        return self.__NoOfTracks
    
    ''' Artist modifier '''    
    def setArtist(self, newArtist):
        self.__Artist = newArtist
        
    ''' NoOfTracks modifier '''    
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks
        
    ''' Display Helper Method'''
    def display(self):
        return "{0}{1:12}{2}".format(super().display(), self.getArtist(),self.getNoOfTracks())
        
    
''' Sub Class Resource '''
class FilmDVD(Resource):

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RuuningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RuuningTime = RuuningTime
        
    ''' Director accessor '''    
    def getDirector(self):
        return self.__Director
    
    ''' RuuningTime accessor '''    
    def getRuuningTime(self):
        return self.__RuuningTime
    
    ''' Director modifier '''    
    def setDirector(self, newDirector):
        self.__Director = newDirector
        
    ''' RuuningTime modifier '''    
    def setRuuningTime(self, newRuuningTime):
        self.__RuuningTime = newRuuningTime
        
    ''' Display Helper Method'''
    def display(self):
        return "{0}{1:12}{2}".format(super().display(), self.getDirector(),self.getRuuningTime())

#main
##r1 = Resource("00001","SHINEE WORLD","030307","C")
##print(r1.getResourceNo())
##r1.setTitle("Shinee 2011")
##print(r1.getTitle())
##print(r1.display())
##
##r2 = Resource("00002","Super Junior","012931","C")
##r2.setTitle("Super Junior World Tour")
##r2.setDateAcquired("010310")
##r2.setResourceType("C")
##
##print(r2.display())
#print(r2.__Title) #illegal, should not access private data directly, need to do it via public method
                   #data hiding (encapsulation)

##cd1 = MusicCD("00003","Sound Horizon", "070705","C","Revo",10)
##print(cd1.getResourceNo())#inherited method
##print(cd1.getArtist())#class method
##print(cd1.display())#overriding: look at subclass method first,then super class, then goes up the hiearchy
##
##dvd1 = FilmDVD("0004","ROTOTO", "020305","D","Andy Lao",120)
##print(dvd1.display())
##resource_list = []
##resource_list.append(cd1)
##resource_list.append(dvd1)
##
##print(resource_list)

for item in resource_list:
    item.display()         #polymorphism it'll automatically call the methods of that class, don't need to check/define
