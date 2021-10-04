

class Marcador:

    def __init__(self):
        self.player1 = 0
        self.player2 = 0

    def anotar(self, player):
        if player == 1:
            if self.evaluar(self.player1) == 1:
                self.player1 += 15
            else:
                self.player1 += 10
        else:
            if self.evaluar(self.player2) == 1:
                self.player2 += 15
            else:
                self.player2 += 10

    def evaluar(self, player):
        if player < 30:
            return 1
        else:
            return 2

    def mayor(self):
        if self.player1 > self.player2:
            return 1
        elif self.player2 > self.player1:
            return 2
        else:
            return 0

    def mas_cuarenta(self):
        result = self.mayor()

        if(result == 1):
            if(self.player1 - self.player2 >= 20):
                return "P1 win"
            else:
                return "P1 Advantage"
        elif(result == 2):
            if(self.player2 - self.player1 >= 20):
                return "P2 win"
            else:
                return "P2 Advantage"
        else:
            return "Tie"

    def score(self):

        if self.player1 <= 40 and self.player2 <= 40:
            return "P1 {0}-{1} P2".format(self.player1, self.player2)
        else:
            return self.mas_cuarenta()
