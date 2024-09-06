class Cell:  # Клетка
    id = 1

    def __init__(self):
        self._status = False
        self.__id = Cell.id
        Cell.id += 1
        self.simbol = None

    def set_simbol(self, value):  # cross - крестик, zero - нолик
        if value == None:
            self.simbol = value
            self._status = False if self.simbol is None else True
        else:
            if not self._status:
                self.simbol = value
                self._status = True
            else:
                print("Клетка уже занята")

    def get_status(self):
        return self._status

    def __str__(self):
        sim = "Свободно" if self.simbol is None else self.simbol
        return f'Клетка#{self.__id}-{"Свободно" if not self._status else {sim} }'


class Board:
    def __init__(self):
        self.field = [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]  # поле

    def set_cell(self, number_cell, player):
        """Метод получает номер клетки и, если клетка не занята,
         меняет её состояние. Если состояние удалось изменить,
          метод возвращает True, иначе возвращается False."""
        if not self.field[number_cell - 1].get_status():
            self.field[number_cell - 1].set_simbol(player)
            return True
        return False

    def check_win(self):
        """Метод не получает входящих данных, но возвращает
         True/False. True — если один из игроков победил,
          False — если победителя нет"""
        win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)]
        for i in win_positions:
            if (self.field[i[0]].simbol != None) and (self.field[i[0]].simbol == self.field[i[1]].simbol == self.field[i[2]].simbol):
                return True
        return False

    def reset_board(self):
        for cell in self.field:
            cell.set_simbol(None)

    def show_field(self):
        for i in range(1, 10):
            if not i % 3 == 0:
                print(self.field[i - 1], end=' | ')
            else:
                print(self.field[i - 1])
                print('-' * 58)


class Player:
    def __init__(self, name, simbol):
        self.name = name
        self.simbol = simbol
        self.number_wins = 0

    def make_to_move(self):
        """Сделать ход"""
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки для вашего хода(1 - 9): "))
                if move < 1 or move > 9:
                    raise ValueError
                return move
            except ValueError:
                print("Неправильный ввод. Пожалуйста, введите число от 1 до 9")

    def __repr__(self):
        return f"Player('{self.name}', '{self.simbol}')"


class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.list_player = [player_one, player_two]
        self.board = Board()

    def launch_move(self, player: Player):
        while True:
            self.board.show_field() # Выводит доску
            cell_number = player.make_to_move() # возвращает число пользователя
            if self.board.set_cell(cell_number, player.simbol): # Устанавливает на клетку символ
                if self.board.check_win(): # Проверяет победителя
                    return True
                else:
                    return False
            print("Клетка занята сделайте другой ход")

    def play_one_game(self):
        """Проводит одну игру до победы одного из игроков или ничьи."""
        print("Игра началась!")
        while True:
            for player in self.list_player:
                if self.launch_move(player): # Возвращает True или False если кто победил
                    self.board.show_field() # Возвращает доску
                    print(f"Поздравляем, {player.name}! Вы выиграли!")
                    player.number_wins += 1
                    return
                if all(cell.get_status() for cell in self.board.field):
                    self.board.show_field()
                    print("Ничья")
                    return

    def start_games(self):
        """Запускает серию игр с возможностью перезапуска."""
        print("Добро пожаловать в игру Крестики-Нолики!")
        while True:
            self.board.reset_board()  # Сбрасываем доску для новой игры
            self.play_one_game()
            print(
                f"Счет: {self.list_player[0].name} - {self.list_player[0].number_wins}, {self.list_player[1].name} - {self.list_player[1].number_wins}")
            again = input("Хотите продолжить игру? (да/нет): ")
            if again.lower() != 'да':
                print("Спасибо за игру!")
                break


if __name__ == "__main__":
    player1 = Player("Misha", "X")
    player2 = Player("Alex", "O")
    game = Game(player1, player2)
    game.start_games()


