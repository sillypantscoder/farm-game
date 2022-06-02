import ui
import itemhelpers

ui.autoinit()
materials = [["Wood", "wood", 2], ["Leaves", "leaves", 0.5], ["Blossoms", "blossom", 0.5], ["Apples", "apple", 1], ["Berries", "berry", 1]]

c = ui.pygame.time.Clock()
while True:
	try:
		u = ui.UI()
		u.add(ui.Header("Market"))
		u.add(ui.Text(f"You have ${itemhelpers.getMoney()}"))
		# Selling
		sellfunc = lambda mat: (lambda: itemhelpers.loseItem(mat[1]) or itemhelpers.setMoney(itemhelpers.getMoney() + mat[2]))
		for mat in materials:
			matKey = mat[1]
			displayName = mat[0]
			price = mat[2]
			if itemhelpers.getItems()[matKey] > 0:
				u.add(ui.Button(f"Sell {displayName} for ${price} each (you have {itemhelpers.getItem(matKey)})").addclick(sellfunc(mat)))
		# Buying
		u.add(ui.Divider(25))
		buyfunc = lambda mat: (lambda: itemhelpers.setMoney(itemhelpers.getMoney() - mat[2]) or itemhelpers.gainItem(mat[1]))
		for mat in materials:
			matKey = mat[1]
			displayName = mat[0]
			price = mat[2]
			if itemhelpers.getMoney() >= price:
				u.add(ui.Button(f"Buy {displayName} for ${price} each").addclick(buyfunc(mat)))
		ui.render_ui(u)
	except Exception as e:
		u = ui.UI()
		u.add(ui.Header("Market - Error"))
		u.add(ui.Text(f"Error: {e}"))
		ui.render_ui(u)
	c.tick(10)
