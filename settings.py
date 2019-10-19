class Settings():
    def __init__(self):
        #Inicia as configurações do jogo
        self.__screenWidth = 960
        self.__screenHeight = 720
        self.__bgColour = (104,104,104)
        self.__playerSpeed = 0.8
        self.__playerSpeed2 = 0.3
        self.__pBulletSpeed = 2
        self.__pBulletSpeed_Slow = 4
        self.__pFireDelay = 80
        self.__enemySpeed = 0.35
        self.__enemyFDelay = 1500
        self.__enemyBSpeed = 0.5

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
    def getPBulletS_Slow(self):
        return self.__pBulletSpeed_Slow
    def getPFireDelay(self):
        return self.__pFireDelay
    def getESpeed(self):
        return self.__enemySpeed
    def getEFDelay(self):
        return self.__enemyFDelay
    def getEBSpeed(self):
        return self.__enemyBSpeed
