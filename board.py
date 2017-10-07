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
		self.piece_board = [[' ', ' ', ' ', 'r', 'r', 'r', 'r', 'r', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'r', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['r', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ', ' ', 'r'],
['r', ' ', ' ', ' ', 'g', 'g', 'g', ' ', ' ', ' ', 'r'],
['r', 'r', ' ', 'g', 'g', 'G', 'g', 'g', ' ', 'r', 'r'],
['r', ' ', ' ', ' ', 'g', 'g', 'g', ' ', ' ', ' ', 'r'],
['r', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ', ' ', 'r'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'r', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'r', 'r', 'r', 'r', 'r', ' ', ' ', ' ']]

		self.BOARD_SIZE = 11

	def is_red (self, x, y):
		return self.under_board[x][y] == 'r'

	def is_green (self, x, y):
		return self.under_board[x][y] == 'G' or self.under_board[x][y] == 'g'

	def is_capping (self, x, y, dx, dy):
		if (self.is_red(x, y) and self.is_red(x+dx,y+dx)):
			print("red cant cap red")
			return 0		

		if (self.is_green(x, y) and self.is_green(x+dx,y+dx)):
			print("green cant cap green")
			return 0		


		if (self.is_red(x, y) and self.is_red(x+2*dx, y+2*dy)):
			print ("sandwiched by red")
			return 1
		
		if (self.is_green(x, y) and self.is_green(x+2*dx, y+2*dy)):
			print ("sandwiched by green")
			return 1
		
		if ('x' == self.under_board[x+2*dx][y+2*dy]):
			print ("sandwiched by x space")
			return 1
		
		print("no cap")
		return 0	

	def win (self, is_green):
		print(("red", "green")[is_green] + " wins")

	def is_x_space (self, x, y):
		return self.under_board[x][y] == 'y' or self.under_board[x][y] == 'x'

	def move (self, xi, yi, xf, yf):
		if (xf < 0 or xf >= self.BOARD_SIZE or yf < 0 or yf >= self.BOARD_SIZE):
			print("out of bounds move")
			return 0

		if (xi != xf and yi != yf):
			print("not along a row or column")
			return 0

		if (self.piece_board[xi][yi] != 'G' and self.is_x_space(xf, yf)):
			print("moving to an x space not as king")
			return 0


		if (xi == xf):
			for i in range (yf, yi, (1,-1)[bool(yf-yi)]):
				if (self.piece_board[xi][i] != ' '):
					print("piece in the way at", xi, i)
					return 0
		if (yi == yf):
			for i in range (xf, xi, (1,-1)[bool(xf-xi)]):
				if (self.piece_board[i][yi] != ' '):
					print("piece in the way at", i, yi)
					return 0
		
		self.piece_board[xf][yf] = self.piece_board[xi][yi]

		if (self.piece_board[xi][yi] == 'G' and self.under_board[xf][yf] == 'x'):
			self.win(1)
			return 1

		if (xf + 2 < self.BOARD_SIZE):
			if (self.is_capping(xf, yf, 1, 0)):
				if (self.piece_board[xf+1][yf] == 'G'):
					self.win(0)
				self.piece_board[xf+1][yf] = ' '
		if (xf - 2 >= 0):
			if (self.is_capping(xf, yf, -1, 0)):
				if (self.piece_board[xf-1][yf] == 'G'):
					self.win(0)
				self.piece_board[xf-1][yf] = ' '
		if (yf + 2 < self.BOARD_SIZE):
			if (self.is_capping(xf, yf, 0, 1)):
				if (self.piece_board[xf][yf+1] == 'G'):
					self.win(0)
				self.piece_board[xf][yf+1] = ' '
		if (yf - 2 >= 0):
			if (self.is_capping(xf, yf, 0, -1)):
				if (self.piece_board[xf][yf-1] == 'G'):
					self.win(0)
				self.piece_board[xf][yf-1] = ' '
		
		self.piece_board[xi][yi] = '0'
		
		return 1
