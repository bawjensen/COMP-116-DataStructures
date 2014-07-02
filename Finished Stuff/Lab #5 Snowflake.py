import turtle

def turtleSnowflake(recurDepth):
	wn = turtle.Screen()
	T = turtle.Turtle()

	length = 81
	depth = recurDepth

	recursion(T, length, depth)
	T.right(120)
	recursion(T, length, depth)
	T.right(120)
	recursion(T, length, depth)

	turtle.mainloop()

def recursion(T, length, depth):
	if depth == 0:
		T.forward(length)
		T.left(60)
		T.forward(length)
		T.right(120)
		T.forward(length)
		T.left(60)
		T.forward(length)

	if depth > 0:
		recursion(T, length/3, depth-1)
		T.left(60)
		recursion(T, length/3, depth-1)
		T.right(120)
		recursion(T, length/3, depth-1)
		T.left(60)
		recursion(T, length/3, depth-1)


def main():
	turtleSnowflake(3)

if __name__ == "__main__":
	main()