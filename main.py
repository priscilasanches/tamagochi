from start import Start
from menu import Menus

start = Start()
name = start.presentation()
menus = Menus(name)
end = False
menus.main_menu()
