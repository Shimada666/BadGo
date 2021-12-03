import random
from nonebot import on_regex, on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

poker_name = ['♦️10', '♦️2', '♦️3', '♦️4', '♦️5', '♦️6', '♦️7', '♦️8', '♦️9', '♦️A', '♦️J', '♦️K', '♦️Q',
              '♣️10', '♣️2', '♣️3', '♣️4', '♣️5', '♣️6', '♣️7', '♣️8', '♣️9', '♣️A', '♣️J', '♣️K', '♣️Q',
              '♥️10', '♥️2', '♥️3', '♥️4', '♥️5', '♥️6', '♥️7', '♥️8', '♥️9', '♥️A', '♥️J', '♥️K', '♥️Q',
              '♠️10', '♠️2', '♠️3', '♠️4', '♠️5', '♠️6', '♠️7', '♠️8', '♠️9', '♠️A', '♠️J', '♠️K', '♠️Q']
# 牌堆用一个列表来表示

poker_value = {'♣️A': 1, '♥️A': 1, '♠️A': 1, '♦️A': 1, '♦️10': 10, '♦️2': 2, '♦️3': 3, '♦️4': 4, '♦️5': 5, '♦️6': 6,
               '♦️7': 7,
               '♦️8': 8, '♦️9': 9, '♦️J': 10, '♦️K': 10, '♦️Q': 10,
               '♣️10': 10, '♣️2': 2, '♣️3': 3, '♣️4': 4, '♣️5': 5, '♣️6': 6, '♣️7': 7, '♣️8': 8, '♣️9': 9, '♣️J': 10,
               '♣️K': 10,
               '♣️Q': 10,
               '♥️10': 10, '♥️2': 2, '♥️3': 3, '♥️4': 4, '♥️5': 5, '♥️6': 6, '♥️7': 7, '♥️8': 8, '♥️9': 9, '♥️J': 10,
               '♥️K': 10,
               '♥️Q': 10,
               '♠️10': 10, '♠️2': 2, '♠️3': 3, '♠️4': 4, '♠️5': 5, '♠️6': 6, '♠️7': 7, '♠️8': 8, '♠️9': 9, '♠️J': 10,
               '♠️K': 10,
               '♠️Q': 10}
# 根据牌堆里面的名称，设置每张牌对应的分值

Ace = {'♣️A', '♥️A', '♠️A', '♦️A'}  # 用于判断手牌中是否有A，根据分数来选择A牌的分值是0还是1

blackjack = on_command("blackjack")


class BlackJack:
    def __init__(self):
        self.Round = 1
        self.total_score = [0, 0]  # 总分的计分器

        self.poker_deck = 1  # 一共是使用几副牌
        self.poker_database = poker_name * self.poker_deck  # 最终生成的牌堆

        self.your_hand_poker = []
        self.pc_hand_poker = []

        self.score = []

    def Dealing_Poker(self):
        # 发一张牌，并在牌堆中删除这张牌
        return self.poker_database.pop(random.randint(0, len(self.poker_database) - 1))

    def Score_Count(self, hand_poker):
        # 计算牌的点数
        Score = 0
        Have_Ace = False
        for k in hand_poker:
            Score += poker_value[k]
        for i in hand_poker:
            if i in Ace:
                Have_Ace = True
                break
            else:
                continue
        if Have_Ace == True:
            if Score + 10 <= 21:
                Score = Score + 10
        return Score

    async def Judgement(self, your_score, pc_score):
        # 结束要牌的时候，计算双方的点数，判断输赢
        if your_score > 21 and pc_score > 21:
            print('PUSH')
            await blackjack.finish(f'PUSH')
            # return np.array([0, 0])
        elif your_score > 21 and pc_score <= 21:
            print('YOU LOSE')
            await blackjack.finish(f'YOU LOSE')
            # return np.array([0, 1])
        elif your_score <= 21 and pc_score > 21:
            print('YOU WIN')
            await blackjack.finish(f'YOU WIN')
            # return np.array([1, 0])
        elif your_score <= 21 and pc_score <= 21:
            if your_score < pc_score:
                print('YOU LOSE')
                await blackjack.finish(f'YOU LOSE')
                # return np.array([0, 1])
            elif your_score > pc_score:
                print('YOU WIN')
                await blackjack.finish(f'YOU WIN')
                # return np.array([1, 0])
            else:
                print('PUSH')
                await blackjack.finish(f'PUSH')
                # return np.array([0, 0])
        else:
            await blackjack.reject('GO ON')

    # def Hit_or_Stand(self):
    #     # 玩家需要判断是否继续叫牌
    #     AskPoker = input('Would You Hit?(Y/N)>>:')
    #     if AskPoker.upper() == 'Y':
    #         return self.Dealing_Poker(poker_database)
    #     elif AskPoker.upper() == 'N':
    #         print('You stand')
    #         return False
    #     else:
    #         print('Wrong input, please input Y/y or N/n!>>')
    #         return self.Hit_or_Stand()

    # def Continue_Or_Quit(self):
    #     # 在每一轮结束后，判断是否继续下一轮的游戏。当牌堆里面牌的数目不足的时候，自动停止游戏
    #     NextRound = input('Would you like start next round?(Y/N)>>')
    #     if NextRound.upper() == 'Y':
    #         if len(poker_database) < 10:
    #             print('The left pokers is not enough')
    #             input('Game Over')
    #             exit(1)
    #         else:
    #             return True
    #     elif NextRound.upper() == 'N':
    #         input('Game Over')
    #         exit(1)
    #     else:
    #         print('Wrong Input, Please Try One More Time!')
    #         self.Continue_Or_Quit()

    def Start_Dealing(self, poker_database):
        # 开局的时候，自动给玩家和电脑发两张牌
        return [poker_database.pop(random.randint(0, len(poker_database) - 1)),
                poker_database.pop(random.randint(0, len(poker_database) - 1))]

    async def One_Round(self):
        # 一个回合的游戏
        you_get = self.Start_Dealing(self.poker_database)
        pc_get = self.Start_Dealing(self.poker_database)
        print(f'Your hand poker:{you_get[0]} , {you_get[1]}')
        await blackjack.send(f'Your hand poker:{you_get[0]} , {you_get[1]}')
        print(f'PC\'s hand poker:{pc_get[0]} , ?\n')
        await blackjack.send(f'PC\'s hand poker:{pc_get[0]} , ?\n')
        self.your_hand_poker.extend(you_get)
        self.pc_hand_poker.extend(pc_get)
        self.score = [self.Score_Count(self.your_hand_poker), self.Score_Count(self.pc_hand_poker)]
        if self.score[0] == 21 or self.score[1] == 21:
            print('BlackJack')
            await blackjack.finish(f'BlackJack')
            return self.Judgement(self.score[0], self.score[1])
        else:
            await blackjack.send('Would You Hit?(Y/N)>>:')
            return
            # while score[0] <= 21:
            #     Get_New_Poker = self.Hit_or_Stand()
            #     if Get_New_Poker != False:
            #         self.your_hand_poker.append(Get_New_Poker)
            #         print(f'You Hand Poker:{self.your_hand_poker}')
            #         score[0] = self.Score_Count(self.your_hand_poker)
            #         if score[0] > 21:
            #             print('You Bust')
            #             print(f'PC\'s Hand Poker:{self.pc_hand_poker}')
            #             return self.Judgement(score[0], score[1])
            #         else:
            #             continue
            #     elif Get_New_Poker == False:
            #         while score[1] < score[0]:
            #             PC_Ask_Poker = self.Dealing_Poker(poker_database)
            #             self.pc_hand_poker.append(PC_Ask_Poker)
            #             pc_score = self.Score_Count(self.pc_hand_poker)
            #             score[1] = pc_score
            #         print(f'PC final hand poker:{self.pc_hand_poker}')
            #         return self.Judgement(score[0], score[1])
            #     else:
            #         continue


@blackjack.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await blackjack.send('start')
    instance = BlackJack()
    await instance.One_Round()
    state['a'] = instance


@blackjack.receive()
async def receive(bot: Bot, event: Event, state: T_State):
    instance: BlackJack = state['a']
    from_msg = event.get_plaintext()
    if from_msg.lower() == 'y':
        Get_New_Poker = instance.Dealing_Poker()
        instance.your_hand_poker.append(Get_New_Poker)
        await blackjack.send(f'You Hand Poker:{instance.your_hand_poker}')
        instance.score[0] = instance.Score_Count(instance.your_hand_poker)
        if instance.score[0] > 21:
            await blackjack.send('You Bust')
            await blackjack.send(f'PC\'s Hand Poker:{instance.pc_hand_poker}')
            await instance.Judgement(instance.score[0], instance.score[1])
        else:
            await blackjack.reject('Would You Hit?(Y/N)>>:')
    elif from_msg.lower() == 'n':
        await blackjack.send('You stand')
        while instance.score[1] < instance.score[0]:
            PC_Ask_Poker = instance.Dealing_Poker()
            instance.pc_hand_poker.append(PC_Ask_Poker)
            pc_score = instance.Score_Count(instance.pc_hand_poker)
            instance.score[1] = pc_score
        await blackjack.send(f'PC final hand poker:{instance.pc_hand_poker}')
        await instance.Judgement(instance.score[0], instance.score[1])
    else:
        await blackjack.reject('Wrong Input, Please Try One More Time!')
    # s = 'pc:' + ','.join(instance.pc_hand_poker)
    # await blackjack.finish(s)
# if __name__ == '__main__':
#     # BlackJack().run()
#     BlackJack().One_Round(poker_database)
