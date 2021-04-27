import arcade


def main(y):
    arcade.open_window(800, 800, "checkers")
    arcade.start_render()
    all_rows(y)
    arcade.finish_render()
    arcade.run()


def all_rows(y):
    #draws all of the rows. I know, it's clunky, but it works.
    print("main first call", y)
    checkers_red(50, y)
    checkers_white(150, y)
    checkers_red(250, y)
    checkers_white(350, y)
    checkers_red(450, y)
    checkers_white(550, y)
    checkers_red(650, y)
    checkers_white(750, y)
    y += 100
    checkers_white(50, y)
    checkers_red(150, y)
    checkers_white(250, y)
    checkers_red(350, y)
    checkers_white(450, y)
    checkers_red(550, y)
    checkers_white(650, y)
    checkers_red(750, y)
    print("main second call", y)
    y += 100
    print("main third call", y)
    checkers_red(50, y)
    checkers_white(150, y)
    checkers_red(250, y)
    checkers_white(350, y)
    checkers_red(450, y)
    checkers_white(550, y)
    checkers_red(650, y)
    checkers_white(750, y)
    y = y + 100
    checkers_white(50, y)
    checkers_red(150, y)
    checkers_white(250, y)
    checkers_red(350, y)
    checkers_white(450, y)
    checkers_red(550, y)
    checkers_white(650, y)
    checkers_red(750, y)
    print("main fourth", y)
    y += 100
    print("main fifth call", y)
    checkers_red(50, y)
    checkers_white(150, y)
    checkers_red(250, y)
    checkers_white(350, y)
    checkers_red(450, y)
    checkers_white(550, y)
    checkers_red(650, y)
    checkers_white(750, y)
    y += 100
    checkers_white(50, y)
    checkers_red(150, y)
    checkers_white(250, y)
    checkers_red(350, y)
    checkers_white(450, y)
    checkers_red(550, y)
    checkers_white(650, y)
    checkers_red(750, y)
    print("main sixth call", y)
    y += 100
    print("main seventh call", y)
    checkers_red(50, y)
    checkers_white(150, y)
    checkers_red(250, y)
    checkers_white(350, y)
    checkers_red(450, y)
    checkers_white(550, y)
    checkers_red(650, y)
    checkers_white(750, y)
    y += 100
    checkers_white(50, y)
    checkers_red(150, y)
    checkers_white(250, y)
    checkers_red(350, y)
    checkers_white(450, y)
    checkers_red(550, y)
    checkers_white(650, y)
    checkers_red(750, y)
    print("main eight call", y)

    return y


def checkers_red(x, y):
    # Draws one red box
    arcade.draw_rectangle_filled(x, y, 100, 100, arcade.csscolor.MAROON)


def checkers_white(x, y):
    # Draws one white box
    arcade.draw_rectangle_filled(x, y, 100, 100, arcade.csscolor.IVORY)

# def y_add(y): this was a discarded function to add Y to it every time,
# so we could just call main and it would automatically do one row, then another, etc.
# print("y add start",y)
# y += y + 100
# print("y add 2",y)
# return y

x = 0
y = 50
main(y)
