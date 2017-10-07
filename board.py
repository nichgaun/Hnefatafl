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

	def is_red (self, x, y):
		return self.under_board[x][y] == 'r'

	def is_green (self, x, y):
		return self.under_board[x][y] == 'G' or self.under_board[x][y] == 'g'

	def is_capping (self, xi, yi, xf, yf):
		if (self.is_red(xi, yi) != self.is_red(xf, yf) and self.under_board[xf][yf] != 'x'):
			return 0

		if (self.is_green(xi, yi) != self.is_green(xf, yf) and self.under_board[xf][yf] != 'x'):
			return 0

		return 1	

	def is_x_space (self, x, y):
		return self.under_board[x][y] == 'y' or self.under_board[x][y] == 'x'

	def move (self, xi, yi, xf, yf):
		if (xi != xf or yi != yf):
			return 0

		if (self.piece_board[xi][yi] != 'G' and self.is_x_space(xf, yf)):
			return 0

		#swap with board variable
		pi, pf
		isx = 1

		if (xi == xf):
			pi = yi
			pf = yf
		else:	
			pi = xi
			pf = xf
			isx = 0

		for i in range (pi, pf):
			if (i != pi or (self.piece_board[pi][i] != ' ' and isx) or (self.piece_board[i][pi] != ' ' and not isx)):
				return 0
		
		self.piece_board[xf][yf] = self.piece_board[xi][yi]

		if (self.piece_board[xi][yi] == 'G' and self.under_board[xf][yf] == 'x'):
			#win()
			return 1

		if (xf + 2 < BOARDSIZE):
			if (is_capping(xf, yf, xf+2, yf)):
				self.piece_board[xf+1][yf] = ' '
		if (xf - 2 >= 0):
			if (is_capping(xf, yf, xf-2, yf)):
				self.piece_board[xf-1][yf] = ' '
		if (yf + 2 < BOARDSIZE):
			if (is_capping(xf, yf, xf, yf+2)):
				self.piece_board[xf][yf+1] = ' '
		if (yf - 2 >= 0):
			if (is_capping(xf, yf, xf, yf-2)):
				self.piece_board[xf][yf-1] = ' '
		
		self.piece_board[xi][yi] = ' '
		
		return 1