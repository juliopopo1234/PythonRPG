class Character:

    def __init__(self,first,last,PV,ATQ,DEF,img):
        self.first = first
        self.last = last
        self.PV = PV
        self.ATQ = ATQ
        self.DEF = DEF
        self.img = img
        self.skills = skills

    def fullname(self,first):
        return '{} {}'.format(self.first, self.last)

    def get_PV(self):
        return self.PV

    def get_ATQ(self):
        return self.ATQ

    def get_DEF(self):
        return self.DEF

    def get_img(self):
        return self.img

    def damage(self,damage):
        if self.DEF > 0:
            self.DEF -= 1
        self.PV -= damage
        print("Vous venez de subir",damage,"dégats")

    def attack_player(self,target_player):
        target_player.damage(self.attack)