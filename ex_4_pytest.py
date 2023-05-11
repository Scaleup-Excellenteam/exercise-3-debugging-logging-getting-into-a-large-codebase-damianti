from Piece import King, Queen, Knight, Rook, Bishop, Pawn
import pytest
from enums import Player
from ai_engine import chess_ai
from chess_engine import game_state

BOARD_SIZE = 8

""" --- Unit Test 1 - Black Knight at position 1, 2. Board as described below (without main character Knight): --- """
"""
    * 0 1 2 3 4 5 6 7
    0 - - - - - - - -
    1 - - - - - - - -
    2 - - - - P - - -
    3 - - - - - - - -
    4 - - - - - - - -
    5 - - - - - - - -
    6 - - - - - - - -
    7 - - - - - - - -
"""


@pytest.fixture
def knight_1():
    """
    This fixture sets up a black Knight at position (1, 2)
    Returns:
        Knight: A Knight instance in the specified position.
    """
    return Knight('n', 1, 2, Player.PLAYER_2)


""" -------------------------------------------- """


@pytest.fixture
def game_1():
    """
    This fixture sets up a game state with an empty board except a white Pawn at position (2, 4).
    Returns:
        game_state: A game state instance with the specified board.
    """
    game = game_state()

    # emptying the board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            game.board[row][col] = Player.EMPTY

    game.board[2][4] = Pawn('p', 2, 4, Player.PLAYER_1)

    return game


""" -------------------------------------------- """


def test_1_get_valid_piece_takes(knight_1, game_1):
    """
    This test verifies that the Knight correctly identifies valid piece takes.
    Arguments:
        knight_1 : A Knight instance.
        game_1 : A game state instance.
    """
    actual_takes = knight_1.get_valid_piece_takes(game_1)

    expected_takes = [(2, 4)]

    # check if expected = actual
    assert set(actual_takes) == set(expected_takes)


""" -------------------------------------------- """


def test_1_get_valid_peaceful_moves(knight_1, game_1):
    """
    This test verifies that the Knight correctly identifies valid peaceful moves.
    Arguments:
        knight_1 : A Knight instance.
        game_1 : A game state instance.
    """
    actual_moves = knight_1.get_valid_peaceful_moves(game_1)

    expected_moves = [(0, 0), (2, 0), (0, 4), (3, 1), (3, 3)]

    # check if expected = actual
    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """

""" --- Unit Test 2 - White Knight at position 5, 0. Board as described below (without main character Knight): --- """
"""
    * 0 1 2 3 4 5 6 7
    0 - - - - - - - -
    1 - - - - - - - -
    2 - - - - - - - -
    3 - P - - - - - -
    4 p r - - - - - -
    5 - b - - - - - -
    6 k n - - - - - -
    7 - - - - - - - -
"""


@pytest.fixture
def knight_2():
    """
    This fixture sets up a white Knight at position (5, 0)
    Returns:
        Knight: A Knight instance in the specified position.
    """
    return Knight('n', 5, 0, Player.PLAYER_1)


""" -------------------------------------------- """


@pytest.fixture
def game_2():
    """
    This fixture sets up a game state with a custom board.
    Returns:
        game_state: A game state instance with the specified board.
    """
    game = game_state()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            game.board[row][col] = Player.EMPTY

    game.board[4][0] = Pawn('p', 4, 0, Player.PLAYER_1)
    game.board[4][1] = Rook('r', 4, 1, Player.PLAYER_1)
    game.board[5][1] = Bishop('b', 5, 1, Player.PLAYER_1)
    game.board[6][1] = Knight('n', 6, 1, Player.PLAYER_1)
    game.board[6][0] = King('k', 6, 0, Player.PLAYER_1)
    game.board[4][2] = Queen('q', 4, 2, Player.PLAYER_1)

    game.board[3][1] = Pawn('p', 3, 1, Player.PLAYER_2)

    return game


""" -------------------------------------------- """


def test_2_get_valid_piece_takes(knight_2, game_2):
    """
    This test verifies that the Knight correctly identifies valid piece takes.
    Arguments:
        knight_2 : A Knight instance.
        game_2 : A game state instance.
    """
    actual_takes = knight_2.get_valid_piece_takes(game_2)

    expected_takes = [(3, 1)]
    assert set(actual_takes) == set(expected_takes)


""" -------------------------------------------- """


def test_2_get_valid_peaceful_moves(knight_2, game_2):
    """
    This test verifies that the Knight correctly identifies valid peaceful moves.
    Arguments:
        knight_2 : A Knight instance.
        game_2 : A game state instance.
    """

    actual_moves = knight_2.get_valid_peaceful_moves(game_2)

    expected_moves = [(6, 2), (7, 1)]

    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """

""" --- Unit Test 3 - starting board with added white Knight at position 5, 5 --- """
"""
    * 0 1 2 3 4 5 6 7
    0 R N B Q K B N R
    1 P P P P P P P P
    2 - - - - - - - -
    3 - - - - - - - -
    4 - - - - - - - -
    5 - - - - - - - -
    6 p p p p p p p p
    7 r n b q k b n r
"""


@pytest.fixture
def knight_3():
    """
    This fixture sets up a white Knight at position 5, 5.
    Returns:
        Knight: A Knight instance in the specified position.
    """
    return Knight('n', 5, 5, Player.PLAYER_1)


""" -------------------------------------------- """


@pytest.fixture
def starting_game():
    """
   This fixture sets up a game state with the starting board.
   Returns:
       game_state: A game state instance with the starting board.
   """
    return game_state()


""" -------------------------------------------- """


def test_3_get_valid_piece_takes(knight_3, starting_game):
    """
    This test verifies that the Knight correctly identifies valid piece takes.
    Arguments:
        knight_3 : A Knight instance.
        starting_game : A game state instance.
    """
    actual_takes = knight_3.get_valid_piece_takes(starting_game)

    expected_takes = [(6, 3), (7, 4), (7, 6), (6, 7)]
    assert set(actual_takes) == set(expected_takes)


""" -------------------------------------------- """


def test_3_get_valid_peaceful_moves(knight_3, starting_game):
    """
      This test verifies that the Knight correctly identifies valid peaceful moves.
      Arguments:
          knight_3 : A Knight instance.
          starting_game : A game state instance.
    """
    actual_moves = knight_3.get_valid_peaceful_moves(starting_game)

    expected_moves = [(4, 3), (3, 4), (3, 6), (4, 7)]

    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """

""" --- Integration Tests --- """

""" --- testing three times get_valid_piece_moves --- """


def test_1_get_valid_piece_moves(knight_1, game_1):
    """
    This test verifies that the Knight correctly identifies valid piece moves (takes or peaceful).
    Arguments:
        knight_1 : A Knight instance.
        game_1 : A game state instance.
    """

    actual_moves = knight_1.get_valid_piece_moves(game_1)

    expected_moves = [(0, 0), (2, 0), (0, 4), (3, 1), (3, 3), (2, 4)]

    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """


def test_2_get_valid_piece_moves(knight_2, game_2):
    """
    This test verifies that the Knight correctly identifies valid piece moves (takes or peaceful).
    Arguments:
        knight_2 : A Knight instance.
        game_2 : A game state instance.
    """
    actual_moves = knight_2.get_valid_piece_moves(game_2)

    expected_moves = [(6, 2), (7, 1), (3, 1)]

    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """


def test_3_get_valid_piece_moves(knight_3, starting_game):
    """
    This test verifies that the Knight correctly identifies valid piece moves (takes or peaceful).
    Arguments:
        knight_3 : A Knight instance.
        starting_game : A game state instance.
    """
    actual_moves = knight_3.get_valid_piece_moves(starting_game)

    expected_moves = [(6, 3), (7, 4), (7, 6), (6, 7), (4, 3), (3, 4), (3, 6), (4, 7)]

    assert set(actual_moves) == set(expected_moves)


""" -------------------------------------------- """
""" --- testing evaluate board  from ai_engine"""
"""
    * 0 1 2 3 4 5 6 7
    0 - - - - R K - -
    1 P P P - - P P P
    2 - - - - - - - -
    3 - - - P - - - -
    4 - B - p - - - -
    5 - - - q - - - -
    6 p p p - - - - p
    7 r - b k - - n -
"""


@pytest.fixture
def game():
    """
    This fixture creates a game state with specific attributes and piece placements.
    Returns:
        game_state: A game state instance with a specific board setup.
    """
    game = game_state()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            game.board[row][col] = Player.EMPTY

    game.board[0][4] = Rook('r', 0, 4, Player.PLAYER_1)
    game.board[0][5] = King('k', 0, 5, Player.PLAYER_1)
    game.board[1][0] = Pawn('p', 1, 0, Player.PLAYER_1)
    game.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
    game.board[1][2] = Pawn('p', 1, 2, Player.PLAYER_1)
    game.board[1][5] = Pawn('p', 1, 5, Player.PLAYER_1)
    game.board[1][6] = Pawn('p', 1, 6, Player.PLAYER_1)
    game.board[1][7] = Pawn('p', 1, 7, Player.PLAYER_1)
    game.board[3][3] = Pawn('p', 3, 3, Player.PLAYER_1)
    game.board[4][1] = Bishop('p', 4, 1, Player.PLAYER_1)

    game.board[4][3] = Pawn('p', 4, 3, Player.PLAYER_2)
    game.board[5][3] = Queen('q', 5, 3, Player.PLAYER_2)
    game.board[6][0] = Pawn('p', 6, 0, Player.PLAYER_2)
    game.board[6][1] = Pawn('p', 6, 1, Player.PLAYER_2)
    game.board[6][2] = Pawn('p', 6, 2, Player.PLAYER_2)
    game.board[6][7] = Pawn('p', 6, 7, Player.PLAYER_2)
    game.board[7][0] = Rook('r', 7, 0, Player.PLAYER_2)
    game.board[7][2] = Bishop('b', 7, 2, Player.PLAYER_2)
    game.board[7][3] = King('k', 7, 3, Player.PLAYER_2)
    game.board[7][6] = Knight('n', 7, 6, Player.PLAYER_2)

    return game


""" -------------------------------------------- """


@pytest.fixture
def ai():
    return chess_ai()


def test_evaluate_board(ai, game):
    """
   This test checks the evaluate_board function of the chess AI.
   It first evaluates the board for Player 1 and then for Player 2, checking if the returned evaluation matches the expected one.
   Arguments:
       ai: An instance of the chess AI.
       game: An instance of the game state with a specific board setup.
   """
    actual_evaluation = ai.evaluate_board(game, Player.PLAYER_1)

    expected_evaluation = 130

    assert actual_evaluation == expected_evaluation

    actual_evaluation = ai.evaluate_board(game, Player.PLAYER_2)

    expected_evaluation = -130

    assert actual_evaluation == expected_evaluation


""" --- System Tests --- """


def test_fulls_mate(starting_game):
    """
    This test verifies that the system correctly identifies the checkmate stalemate situation.
    It moves pieces on the board to a state where the king is in checkmate and then checks the output of
    the checkmate_stalemate_checker function.
    Arguments:
        starting_game: A game state instance at the start of the game.
    """
    starting_game.move_piece((1, 2), (2, 2), False)
    starting_game.move_piece((6, 3), (5, 3), False)
    starting_game.move_piece((1, 1), (3, 1), False)
    starting_game.move_piece((7, 4), (3, 0), False)

    actual_checkmate = starting_game.checkmate_stalemate_checker()

    expected_checkmate = 0

    assert actual_checkmate == expected_checkmate
