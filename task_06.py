class WrongNumberOfPlayersError(Exception):
    ''' класс исключения для количества игроков '''
class NoSuchStrategyError(Exception):
    ''' класс исключения для не правильно заданых данных хода '''
class ExpectedTwoValuesError(Exception):
    ''' класс искючения если подаётся более двух аргументов в внутреннем списке '''
def rps_game_winner(players: list):
    if len(players) >= 3:
        raise WrongNumberOfPlayersError('Number of players > 2')
    else:
        new_list = []
        for i in players:
            if len(i) >= 3:
                raise ExpectedTwoValuesError('more than two arguments of the players moves are given')
        for j in players:
            new_list += j
            if j[1] == 'P' or j[1] == 'S' or j[1] == 'R':
                continue
            else:
                raise NoSuchStrategyError('Player moves are different R, P, S')
        if new_list[1] == new_list[3]:
            return 'player1 %s' % new_list[1]
        else:
            if new_list[1] == 'P' and new_list[3] == 'R' or new_list[1] == 'S' and new_list[
                3] == 'P' or new_list == 'R' and new_list == 'S':
                return 'player1 %s' % new_list[1]
            else:
                return 'player2 %s' % new_list[3]

players_1 = [['player1', 'P'], ['player2', 'P'], ['player3', 'S']]
rps_game_winner(players_1)  # --> WrongNumberOfPlayersError
players_1 = [['player1', 'P'], ['player2', 'A']]
rps_game_winner(players_1)  # --> NoSuchStrategyError
players_1 = [['player1', 'P'], ['player2', 'S']]
rps_game_winner(players_1) # --> player2 S
players_1 = [['player1', 'P'], ['player2', 'P']]
rps_game_winner(players_1) # --> player1 P
players_1 = [['player1','P','S'], ['player2','P']]
rps_game_winner(players_1)  # --> ExpectedTwoValuesError
