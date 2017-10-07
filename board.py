# For printing double sub arrays nicely
def print_board(b):
	for x in range(len(b)):
		print(b[x])

class game_board:
	def __init__(self):
		# Setting up underlying board
		spaces = [' ']*9
		row_edge = ['x'] + spaces + ['x']
		blank_row = [' ']*11
		blank_rows = [blank_row]*4
		middle_row = [' ']*5 + ['y'] + [' ']*5

		# Setting up starting positions of pieces
		b3 = [' ']*3
		b4 = [' ']*4
		b5 = [' ']*5
		b11 = [' ']*11
		row1 = b3 + ['r']*5 + b3

		self.under_board = [row_edge] + blank_rows + [middle_row] + blank_rows + [row_edge]
		self.piece_board = [row1] + [b5+['r']+b5] + [b11] + [['r']+b4+['g']+b4+['r']] + [['r']+b3+['g']*3+b3+['r']] + [['r']*2+[' ']+['g']*2+['G']+['g']*2+[' ']+['r']*2] + [['r']+b3+['g']*3+b3+['r']] + [['r']+b4+['g']+b4+['r']] + [b11] + [b5+['r']+b5] + [row1]
		self.BOARD_SIZE = 11