from abc import ABCMeta, abstractclassmethod, abstractmethod
import random

class Person(metaclass = ABCMeta):
    def __init__(self):
        self.balance = 1000
        self.hp = 10
        self.shield = 0
        self.dice_deck = 15

    # @abstractmethod
    # def set_default(self):
    #     pass

class Player(Person):
    def __init__(self):
        super().__init__()

    def output(self):
        print(self.balance)
        print(self.hp)
        print(self.shield)
        print(self.dice_deck)
   
   
class Dealar(Person):
    def __init__(self):
        super().__init__()

    def output(self):
        print(self.balance)
        print(self.hp)
        print(self.shield)
        print(self.dice_deck)


class Dice:
    dice_list = ['1_D','1_D','4_A','4_A','2_S','3_K']
    def __init__(self):
        pass
    def roll_dice(self):
        self.result = []
        for _ in range(5):
            self.result.append(random.choice(Dice.dice_list))
        self.result = sorted(self.result)
        # print(dice1.result)
        return self.result

class Table():

    def __init__(self):
        pass
    # point = 1000
    def do_betting(self):
        user_bet = int(input('배팅금액 입력 : '))
        if user1.balance < user_bet:
            print('가지고 있는 포인트 너무 작음')
        else:
            user1.balance -= user_bet
            print(f'가지고 있는 포인트{user1.balance}')

    def u_distinc_dice(self):
        dice1.roll_dice()
        print(f'유저의 주사위 :{dice1.result}')
        # print(dice1.result)
        user1.dice_deck -= 5
        for shape in dice1.result:
            if shape == '1_D':
                user1.dice_deck +=1
            if shape == '2_S':
                if user1.shield >= 6:
                    return
                else:
                    user1.shield+=1
            if shape == '3_K':
                user1.hp -= 1
            if shape == '4_A':
                if dealar1.shield > 0:
                    dealar1.shield -= 1    
                dealar1.hp -= 1
        return self.d_distinc_dice()

    def d_distinc_dice(self):
        dice1.roll_dice()
        print(f'딜러의 주사위 :{dice1.result}')
        dealar1.dice_deck -= 5
        for shape in dice1.result:
            if shape == '1_D':
                dealar1.dice_deck +=1
            if shape == '2_S':
                if dealar1.shield >= 6:
                    return
                else:
                    dealar1.shield+=1
            if shape == '3_K':
                dealar1.hp -= 1
            if shape == '4_A':
                if user1.shield > 0:
                    user1.shield -= 1    
                user1.hp -= 1

        print(f'유저의 dice-deck : {user1.dice_deck}, 유저의 방패개수 : {user1.shield}, 유저의 체력 : {user1.hp}')
        print(f'딜러의 dice-deck : {dealar1.dice_deck}, 딜러의 방패개수 : {dealar1.shield}, 딜러의 체력 : {dealar1.hp}')





