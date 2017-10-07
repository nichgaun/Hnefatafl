#returns 1 on a successful move, 0 on unsuccessful
def is_red (x, y):
	return board[x][y] == 'r'

def is_green (x, y):
	return board[x][y] == 'G' or board[x][y] == 'g'

def is_capping (xi, yi, xf, yf):
	if (is_red(xi, yi) != is_red(xf, yf) and under_board[xf][yf] != 'x'):
		return 0

	if (is_green(xi, yi) != is_green(xf, yf) and under_board[xf][yf] != 'x'):
		return 0

	return 1	

def is_x_space (x, y):
	return under_board[x][y] == 'y' or under_board[x][y] == 'x'

def move (xi, yi, xf, yf):
	if (xi != xf or yi != yf):
		return 0

	if (board[xi][yi] != 'G' and is_x_space(xf, yf)):
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
		if (i != pi or (board[pi][i] != ' ' and isx) or (board[i][pi] != ' ' and not isx)):
			return 0
	
	board[xf][yf] = board[xi][yf]

	if (side == 'k' and under_board[xf][yf] == 'x'):
		win()
		return 1

	if (xf + 2 < BOARDSIZE):
		if (is_capping(xf, yf, xf+2, yf)):
			board[xf+1][yf] = ' '
	if (xf - 2 >= 0):
		if (is_capping(xf, yf, xf-2, yf)):
			board[xf-1][yf] = ' '
	if (yf + 2 < BOARDSIZE):
		if (is_capping(xf, yf, xf, yf+2)):
			board[xf][yf+1] = ' '
	if (yf - 2 >= 0):
		if (is_capping(xf, yf, xf, yf-2)):
			board[xf][yf-1] = ' '
	
	board[xi][yi] = ' '
	
	return 1
			
			
		
			
				
