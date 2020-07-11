size = 5

diagonals = 16

grid = [[0 for i in range(size)] for j in range(size)]

def gg(i, j):
	global grid
	if i<0 or j<0 or i>=size or j>=size:
		return 0
	return grid[i][j]

def check(i, j, k):
	if k == 1:
		return(gg(i, j-1) != 2 and gg(i, j+1) != 2 and
			   gg(i-1, j) != 2 and gg(i+1, j) != 2 and
			   gg(i-1, j-1) != 1 and gg(i+1, j+1) != 1)

	else:
		return(gg(i, j-1) != 1 and gg(i, j+1) != 1 and
			   gg(i-1, j) != 1 and gg(i+1, j) != 1 and
			   gg(i-1, j+1) != 2 and gg(i+1, j-1) != 2)

def next_pass(i, j, d):
	j += 1
	if j>=size:
		j = 0
		i += 1

	solve(i, j, d)

def solve(i, j, d):
	global grid
	if d == 0:
		print()
		for row in grid:
			for j in row:
				if j == 0:
					print("_", end = " ")
				elif j == 1:
					print("\\", end = " ")
				else:
					print("/", end = " ")
			print()
		exit()
		return
	if i<0 or i>=size or (size**2 - (size * i) + j + 1) < d:
		return

	for k in [2, 1, 0]:
		if k != 0:
			if(check(i, j, k)):
				grid[i][j] = k
				next_pass(i, j, d-1)

		else:
			grid[i][j] = 0
			next_pass(i, j, d)
	grid[i][j] = 0

solve(0, 0, diagonals)
