import ui
import itemhelpers

ui.autoinit()

c = ui.pygame.time.Clock()
while True:
	try:
		u = ui.UI()
		u.add(ui.Header("Market"))
		u.add(ui.Text(f"You have ${itemhelpers.getMoney()}"))
		# Selling
		sellfunc = lambda mat: (lambda: itemhelpers.loseItem(mat) or itemhelpers.setMoney(itemhelpers.getMoney() + 1))
		for mat in [["Wood", "wood"], ["Leaves", "leaves"], ["Blossoms", "blossom"], ["Apples", "apple"], ["Berries", "berry"]]:
			matKey = mat[1]
			displayName = mat[0]
			if itemhelpers.getItems()[matKey] > 0:
				u.add(ui.Button(f"Sell {displayName} (you have {itemhelpers.getItem(matKey)})").addclick(sellfunc(matKey)))
		# Buying
		buyfunc = lambda mat: (lambda: itemhelpers.setMoney(itemhelpers.getMoney() - 1) or itemhelpers.gainItem(mat))
		for mat in [["Wood", "wood"], ["Leaves", "leaves"], ["Apples", "apple"], ["Berries", "berry"]]:
			matKey = mat[1]
			displayName = mat[0]
			if itemhelpers.getMoney() >= 1:
				u.add(ui.Button(f"Buy {displayName} (you have {itemhelpers.getItem(matKey)})").addclick(buyfunc(matKey)))
		ui.render_ui(u)
	except Exception as e:
		u = ui.UI()
		u.add(ui.Header("Market - Error"))
		u.add(ui.Text(f"Error: {e}"))
		ui.render_ui(u)
	c.tick(10)
