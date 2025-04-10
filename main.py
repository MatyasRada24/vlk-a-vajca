def on_button_pressed_a():
    global x, enemy_x, enemy_y
    x += -1
    if x < 0:
        x += 5
    basic.pause(10)
    if enemy_x < 0:
        enemy_x += -1
    if enemy_y > 4:
        enemy_y = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x, enemy_x, enemy_y
    x += 1
    if x > 4:
        x += -5
    basic.pause(10)
    if enemy_x < 0:
        enemy_x += 1
    if enemy_y > 4:
        enemy_y = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

enemy_y = 0
enemy_x = 0
x = 0
x = 2
y = 4
enemy_x = randint(0, 4)
enemy_y = 4

def on_every_interval():
    global enemy_y, enemy_x
    enemy_y += 1
    led.plot(enemy_x, enemy_y)
    if enemy_x == x and enemy_y == y:
        music.play(music.tone_playable(698, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    if enemy_y == 4:
        basic.pause(100)
        enemy_x = randint(-1, -1)
loops.every_interval(1000, on_every_interval)

def on_forever():
    basic.clear_screen()
    led.plot_brightness(x, 4, 150)
    led.plot(enemy_x, enemy_y)
    basic.pause(50)
basic.forever(on_forever)
