import ui
import itemhelpers

ui.autoinit()

c = ui.pygame.time.Clock()
while True:
	try:
		u = ui.UI()
		u.add(ui.Header("Market"))
		u.add(ui.Text(f"You have ${itemhelpers.getMoney()}"))
		sellfunc = lambda mat: (lambda: itemhelpers.loseItem(mat) or itemhelpers.setMoney(itemhelpers.getMoney() + 1))
		for mat in [["Wood", "wood"], ["Leaves", "leaves"], ["Blossoms", "blossom"], ["Apples", "apple"], ["Berries", "berry"]]:
			if itemhelpers.getItems()[mat[1]] > 0:
				u.add(ui.Button(f"Sell {mat[0]} (you have {itemhelpers.getItem(mat[1])})").addclick(sellfunc(mat[1])))
		ui.render_ui(u)
	except Exception as e:
		u = ui.UI()
		u.add(ui.Header("Market - Error"))
		u.add(ui.Text(f"Error: {e}"))
		ui.render_ui(u)
	c.tick(10)
