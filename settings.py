class Settings():
    def __init__(self):
        #Initialise game settings
        self.__screenWidth = 960
        self.__screenHeight = 720
        self.__bgColour = (104,104,104)
        self.__playerSpeed = 1
        self.__playerSpeed2 = 0.35
        self.__pBulletSpeed = 2
    
    def getWidth(self):
        return self.__screenWidth
    def getHight(self):
        return self.__screenHeight
    def getBgColour(self):
        return self.__bgColour
    def getPSpeed(self):
        return self.__playerSpeed
    def getPSpeed2(self):
        return self.__playerSpeed2
    def getPBulletS(self):
        return self.__pBulletSpeed

    


