import random
cards=['Ace' , 'two' , 'three' , 'four' , 'five' , 'six', 'seven', 'eight' , 'nine' , 'ten' , 'jack' , 'queen' , 'king' ]
class Player():
    def __init__(self,name,balance,cards):
        self.balance = balance
        self.name = name
        self.cards = cards
    def make_bet(self,bet):
        while True:
            if(balance<bet):
                print('insufficient fund , please make lower amount  bet')
                return 'Again'
            else:
                print('bet added succefully')
                return'ok'
    def print_cards(self):
        print(self.cards)

    def sums(self):
        sums = 0
        for value , card in enumerate(cards):
            
            if(card in self.cards and card!='Ace' and card!='jack' and card!='queen' and card!='king'):

                for _ in range(self.cards.count(card)):
                    sums+=value+1
            if(card in self.cards and(card=='jack' or card=='queen' or card=='king')):
                for _ in range(self.cards.count(card)):
                    sums+=10

        if('Ace' in self.cards):
            for _ in range(self.cards.count('Ace')):
                if(sums+11<=21):
                    sums+=11
                else:
                    sums+=1
        return sums

class Moves():

    def move_done(self,move):
        if(move=='Hit'):
            return Deck_of_cards().get_card()
        else:
            return False


class Deck_of_cards():
    
    def get_2cards(self):
        i = random.randint(0,12)
        j = random.randint(0,12)
        return [cards[i] , cards[j]]
    
    def get_card(self):
        no = random.randint(0,12)
        return cards[no]
    
class Dealer():
    def __init__(self,cards):
        self.cards = cards
        
    def first_print_card(self):
        print(self.cards[1])
        
    def print_cards(self):
        print(self.cards)
        
    def sums(self):
        sums = 0
        for value , card in enumerate(cards):
            
            if(card in self.cards and card!='Ace' and card!='jack' and card!='queen' and card!='king'):
                for _ in range(self.cards.count(card)):
                    sums+=value+1
            if(card in self.cards and(card=='jack' or card=='queen' or card=='king')):
                for _ in range(self.cards.count(card)):
                    sums+=10
        if('Ace' in self.cards):
            for _ in range(self.cards.count('Ace')):
                if(sums+11<=21):
                    sums+=11
                else:
                    sums+=1
        return sums
print('Welcome to The exclusive game of BlackJack with casino Python')
print('*********************')
name = input('May i know your name: ')
balance = int(input('What is your total balance: '))
raw_balance = balance
print('*********************')
while True:
    flag=True
    cards_of_player = Deck_of_cards().get_2cards()
    player = Player(name,balance,cards_of_player)
    cards_of_dealer = Deck_of_cards().get_2cards()
    dealer = Dealer(cards_of_dealer)
    print('Your current balance is : ', player.balance)
    ins = input('To start serving your cards press enter')
    print('*********************')
    print('Your cards :')
    player.print_cards()
    print('sum of your cards = ',player.sums())
    print('*********************')
    ins = input('Now to know my cards press enter')
    print('one of my cards is Hidden :')
    print('< Hidden > ,',end=' ')
    dealer.first_print_card()
    print('*********************')
    bet = int(input('Make a bet: '))
    while(player.make_bet(bet)=='Again'):
        bet = int(input('Make a bet: '))
    print('*********************')
    
    if(player.sums()==21):
        print('Congratulations you got Black jack')
        print('You will get 3 for 2')
        print('*********************')
        balance+=1.5*bet
        quest = input('Would you like to play one more match(yes or no): ')
        print('*********************')
        if(quest.lower()=='yes'):
            continue
        if(quest.lower()=='no'):
            print('You earned = ' , balance-raw_balance)
            print('Thank you for playing will meet you next time')
            print('*********************')
            break
    
        
        
    while True :
        move = input('Would you like to Hit or Stay: ')
        if(Moves().move_done(move)==False):
            print('You choose to stay')
            print('*********************')
            break
        if(Moves().move_done(move)!=False):
            player.cards.append(Moves().move_done(move))
            player.print_cards()
            print('sum = ',player.sums())
            print('*********************')
        if(player.sums()>21):
            break
            
    if(player.sums()==21):
        print(player.name,' won the match')
        #print('You will get 3 for 2')
        print('*********************')
        balance+=bet
        quest = input('Would you like to play one more match(yes or no): ')
        print('*********************')
        if(quest.lower()=='yes'):
            continue
        if(quest.lower()=='no'):
            print('You earned = ' , balance-raw_balance)
            print('Thank you for playing will meet you next time')
            print('*********************')
            break
    while(player.sums()<21 and dealer.sums()<=17 and dealer.sums()<player.sums() ):
        flag=False
        ins = input('dealer is going to hit,press enter')
        print('*********************')
        print('Dealers card: ')
        dealer.cards.append(Moves().move_done('Hit'))
        dealer.print_cards()
        print('sum = ',dealer.sums())
        print('*********************')

    if(player.sums()>21):
        print(player.name,' lost the match')
        print('*********************')
        balance-=bet
    if(dealer.sums()==player.sums() and player.sums()<=21):
        if(flag):
            print('Dealers card: ')
            dealer.print_cards()
            print('sum = ',dealer.sums())
        print('Match is Drawn')
        print('*********************')
    if(dealer.sums()>21 and player.sums()<=21):
        if(flag):
            print('Dealers card: ')
            dealer.print_cards()
            print('sum = ',dealer.sums())
        print(player.name ,' won the match')
        print('*********************')
        balance+=bet
        #balance+=2*bet
    if(dealer.sums()>player.sums() and dealer.sums()<=21):
        if(flag):
            print('Dealers card: ')
            dealer.print_cards()
            print('sum = ',dealer.sums())
        print(player.name , ' lost the match')
        print('*********************')
        balance-=bet
    if(player.sums()>dealer.sums() and player.sums()<21):
        if(flag):
            print('Dealers card: ')
            dealer.print_cards()
            print('sum = ',dealer.sums())
        print(player.name , ' won the match')
        print('*********************')
        balance+=bet
        
    if(balance==0):
        print('You went Bankrupt OK BYE :(')
        break
    quest = input('Would you like to play one more match(yes or no): ')
    print('*********************')
    if(quest.lower()=='yes'):
        continue
    if(quest.lower()=='no'):
        print('You earned = ' , balance-raw_balance)
        print('Thank you for playing will meet you next time')
        break
    print('*********************')

