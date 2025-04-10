input.onButtonPressed(Button.A, function () {
    x += -1
    if (x < 0) {
        x += 5
    }
    basic.pause(10)
    if (enemy_x < 0) {
        enemy_x += -1
    }
    if (enemy_y > 4) {
        enemy_y = 0
    }
})
input.onButtonPressed(Button.B, function () {
    x += 1
    if (x > 4) {
        x += -5
    }
    basic.pause(10)
    if (enemy_x < 0) {
        enemy_x += 1
    }
    if (enemy_y > 4) {
        enemy_y = 0
    }
})
let enemy_y = 0
let enemy_x = 0
let x = 0
basic.clearScreen()
x = 2
let y = 4
enemy_x = randint(0, 4)
enemy_y = 4
loops.everyInterval(500, function () {
    enemy_y += 1
    led.plot(enemy_x, enemy_y)
    if (enemy_x == x && enemy_y == y) {
        music.play(music.tonePlayable(698, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    if (enemy_y == 4) {
        basic.pause(10)
        enemy_x = randint(-1, -1)
    }
})
basic.forever(function () {
    basic.clearScreen()
    led.plotBrightness(x, 4, 150)
    led.plot(enemy_x, enemy_y)
    basic.pause(50)
})
