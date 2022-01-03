class WrongNumberOfPlayersError(Exception):
    '''класс исключения для количества игроков'''
class NoSuchStrategyError(Exception):
    '''класс исключения для не правильно заданых данных хода'''
class ExpectedTwoValuesError(Exception):
    '''класс искючения если подаётся более двух аргументов в внутреннем списке '''
def rps_game_winner(players: list):
    if len(players) >= 3:
        raise WrongNumberOfPlayersError
    else:
        st = "'"
        new_list = []
        for i in players:
            if len(i) >= 3:
                raise ExpectedTwoValuesError
        for j in players:
            new_list+=j
            if j[1] == 'P' or j[1] == 'S'or j[1] == 'R':
                continue
            else:
                raise NoSuchStrategyError
        if new_list[1] == new_list[3]:
            return st + 'player1 %s' % new_list[1] + st
        else:
            if new_list[1] == 'P' and new_list[3] == 'R' or new_list[1] == 'S' and new_list[3] == 'P' or new_list == 'R' and new_list == 'S':
                return st + 'player1 %s' % new_list[1] + st
            else:
                return st + 'player2 %s' % new_list[3] + st

players_1=[['player1', 'P'], ['player2', 'P'], ['player3', 'S']]
rps_game_winner(players_1)  #--> WrongNumberOfPlayersError
players_1=[['player1', 'P'], ['player2', 'A']]
rps_game_winner(players_1)  #--> NoSuchStrategyError
players_1=[['player1', 'P'], ['player2', 'S ']]
rps_game_winner(players_1)  #--> 'player2 S'
players_1=[['player1', 'P'], ['player2', 'P']]
rps_game_winner(players_1)  #--> 'player1 P'






