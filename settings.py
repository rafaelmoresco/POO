class Settings():
    def __init__(self):
        #Inicia as configurações do jogo
        self.__fps = 60
        self.__fpsFactor = 8
        self.__screenWidth = 960
        self.__screenHeight = 720
        self.__bgColour = (104,104,104)
        self.__playerSpeed = 0.8*self.__fpsFactor
        self.__playerSpeed2 = 0.3*self.__fpsFactor
        self.__pBulletSpeed = 2*self.__fpsFactor
        self.__pBulletSpeed_Slow = 4*self.__fpsFactor
        self.__pFireDelay = 80/self.__fpsFactor
        self.__enemySpeed = 0.35*self.__fpsFactor
        self.__enemyFDelay = 1000/self.__fpsFactor
        self.__enemyBSpeed = 0.55*self.__fpsFactor
        self.__tInv = 30/self.__fpsFactor

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
    def getFPS(self):
        return self.__fps
    def getTInv(self):
        return self.__tInv
