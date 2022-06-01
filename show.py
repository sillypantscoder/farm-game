import pygame
import random
import json
import sys
import itemhelpers

BOARDSIZE = [9, 9]
BOARD = [["air" for x in range(BOARDSIZE[0])] for y in range(BOARDSIZE[1])]
FILE = "tree"
if len(sys.argv) > 1: FILE = sys.argv[1]

screensize = [500, 500]
screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)

def insideBoard(x, y):
	return (x >= 0) and (x < BOARDSIZE[0]) and (y >= 0) and (y < BOARDSIZE[1])

def night_commands(commands: list, pos: "tuple[int, int]" = (0, 0)):
	for c in commands:
		if c["type"] == "repeat":
			# Repeat {commands} {len} times
			for i in range(c["len"]):
				pos = night_commands(c["commands"], pos)
		elif c["type"] == "getblock":
			# Get a random {block} block
			filledblocks = [[x, y] for y in range(BOARDSIZE[1]) for x in range(BOARDSIZE[0]) if BOARD[y][x] == c["block"]]
			if len(filledblocks): pos = random.choice(filledblocks)
			else: pos = None
		elif c["type"] == "growpos":
			# Go up and randomly left or right
			if pos == None:
				continue
			pos[1] -= 1
			pos[0] += random.choice([-1, 0, 1])
		elif c["type"] == "set":
			# Fill the block with {block}
			if pos == None:
				continue
			if not insideBoard(*pos):
				continue
			if (not c["force"]) and BOARD[pos[1]][pos[0]] != "air":
				continue
			BOARD[pos[1]][pos[0]] = c["block"]
		elif c["type"] == "half":
			# 1/2 chance of doing {commands}
			if random.randint(0, 1) == 0:
				pos = night_commands(c["commands"], pos)
		elif c["type"] == "foreach":
			# For each {block} run {commands}
			filledblocks = [[x, y] for y in range(BOARDSIZE[1]) for x in range(BOARDSIZE[0]) if BOARD[y][x] == c["block"]]
			for b in filledblocks:
				pos = night_commands(c["commands"], b)
		elif c["type"] == "move":
			# Move by {x} {y}
			if pos == None:
				continue
			pos[1] += c["y"]
			pos[0] += c["x"]
	return pos

def night_from_file():
	f = open("structures/" + FILE + ".json", "r")
	commands = json.load(f)
	f.close()
	night_commands(commands["night"])

def begin_from_file():
	f = open("structures/" + FILE + ".json", "r")
	commands = json.load(f)
	f.close()
	BOARD[BOARDSIZE[1] - 1][BOARDSIZE[0] // 2] = commands["start"]

begin_from_file()

c = pygame.time.Clock()
running = True
while running:
	scale = [screensize[0] // BOARDSIZE[0], screensize[1] // BOARDSIZE[1]]
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.VIDEORESIZE:
			screensize = event.size
			screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			pos = [pos[0] // scale[0], pos[1] // scale[1]]
			if insideBoard(*pos) and BOARD[pos[1]][pos[0]] != "air":
				itemhelpers.gainItem(BOARD[pos[1]][pos[0]])
				BOARD[pos[1]][pos[0]] = "air"
	screen.fill((255, 255, 255))
	for y in range(BOARDSIZE[1]):
		for x in range(BOARDSIZE[0]):
			cellrect = pygame.Rect(x * scale[0], y * scale[1], scale[0], scale[1])
			pygame.draw.rect(screen, (0, 0, 0), cellrect, 1)
			if BOARD[y][x] == "air": # AIR
				pass
			elif BOARD[y][x] == "wood": # WOOD
				pygame.draw.rect(screen, (60, 25, 0), cellrect)
			elif BOARD[y][x] == "leaves": # LEAVES
				pygame.draw.rect(screen, (0, 60, 0), cellrect)
			elif BOARD[y][x] == "blossom": # BLOSSOM
				pygame.draw.rect(screen, (110, 0, 110), cellrect)
			elif BOARD[y][x] == "apple": # APPLE
				pygame.draw.rect(screen, (200, 0, 0), cellrect)
			elif BOARD[y][x] == "berry": # BERRY
				pygame.draw.rect(screen, (50, 0, 50), cellrect)
			else:
				pygame.draw.rect(screen, (255, 0, 0), cellrect, 1)
	c.tick(60)
	pygame.display.flip()
	night_from_file()
