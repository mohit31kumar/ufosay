import sys
import time
import shutil
import signal
import random

from .bubble import make_bubble

UFO = [
    "        _.---._        ",
    "      .'       '.      ",
    "  _.-~===========~-._  ",
    " (___________________) ",
    "       \\_______/       ",
]
UFO_W = max(len(r) for r in UFO)
UFO_H = len(UFO)

WINDOW_ON = " (___O___O___O___O___) "

BEAM = [
    ["    |    ", "   /|\\   ", "  / | \\  "],
    ["   |||   ", "  //|\\\\  ", " // | \\\\ "],
    ["  |||||  ", " ///|\\\\\\ ", "/// | \\\\\\"],
    ["   |||   ", "  //|\\\\  ", " // | \\\\ "],
]
BEAM_W = 9
BEAM_H = 3

FLOAT = [0, -1, -2, -1, 0, 1, 2, 1]
STAR_CHARS = ["\u00b7", "*", ".", "+"]
N_STARS = 30
FPS = 60
FRAME_T = 1.0 / FPS
GROUND_PATTERN = ["~", "~", "~", "~", ",", ".", ",", "~", "~"]


def build_frame(cols, rows, ufo_x, ufo_y, win_on, beam_idx, stars, gy, bubble):
    buf = [[" "] * cols for _ in range(rows)]

    for sx, sy, sc in stars:
        if 0 <= sy < rows and 0 <= sx < cols:
            buf[sy][sx] = sc

    if bubble:
        bw = max(len(l) for l in bubble)
        bx = ufo_x + (UFO_W - bw) // 2
        by = ufo_y - len(bubble) - 1
        for i, line in enumerate(bubble):
            ry = by + i
            if 0 <= ry < rows:
                for j, ch in enumerate(line):
                    cx = bx + j
                    if 0 <= cx < cols and ch != " ":
                        buf[ry][cx] = ch

    for i, row in enumerate(UFO):
        ry = ufo_y + i
        if 0 <= ry < rows:
            r = WINDOW_ON if (win_on and i == 3) else row
            for j, ch in enumerate(r):
                cx = ufo_x + j
                if 0 <= cx < cols and ch != " ":
                    buf[ry][cx] = ch

    bx = ufo_x + (UFO_W - BEAM_W) // 2
    by = ufo_y + UFO_H
    beam = BEAM[beam_idx]
    for i, row in enumerate(beam):
        ry = by + i
        if ry < rows:
            for j, ch in enumerate(row):
                cx = bx + j
                if 0 <= cx < cols and ch != " ":
                    buf[ry][cx] = ch

    for c in range(cols):
        if 0 <= gy < rows:
            buf[gy][c] = GROUND_PATTERN[c % len(GROUND_PATTERN)]

    return "\033[H" + "\n".join("".join(r) for r in buf)


def animate_ufo(message=None):
    running = True

    def handler(sig, frame):
        nonlocal running
        running = False

    signal.signal(signal.SIGINT, handler)

    bubble_lines = make_bubble(message) if message else []

    cols, rows = shutil.get_terminal_size((80, 24))
    rows = min(rows, 60)

    star_max_y = max(1, rows // 2 - 2)
    stars = [
        (random.randint(0, cols - 1), random.randint(0, star_max_y), random.choice(STAR_CHARS))
        for _ in range(N_STARS)
    ]

    gy = rows - 2
    ufo_base_y = max(
        len(bubble_lines) + 2,
        (rows - UFO_H - BEAM_H - 2) // 3,
    )
    if ufo_base_y + UFO_H + BEAM_H >= gy:
        ufo_base_y = max(1, gy - UFO_H - BEAM_H - 2)

    ufo_x = cols
    center_x = (cols - UFO_W) // 2
    word_count = len(message.split()) if message else 0
    pause_duration = 0.5 * word_count
    stage = "entering"
    pause_t = 0.0
    pause_fl = 0
    float_counter = 0
    frame = 0

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while running:
            t0 = time.perf_counter()

            if stage == "entering" and ufo_x <= center_x:
                stage = "paused" if pause_duration > 0 else "exiting"
                pause_t = t0
                pause_fl = ufo_y - ufo_base_y if float_counter > 0 else 0

            if stage == "paused" and (t0 - pause_t) >= pause_duration:
                stage = "exiting"

            if stage == "paused":
                ufo_y = ufo_base_y + pause_fl
            else:
                fl = FLOAT[(float_counter // 6) % len(FLOAT)]
                ufo_y = ufo_base_y + fl
                float_counter += 1

            win_on = (frame // 20) % 2 == 0
            bi = (frame // 4) % len(BEAM)

            show_bubble = bubble_lines if stage == "paused" else None
            out = build_frame(cols, rows, ufo_x, ufo_y, win_on, bi, stars, gy, show_bubble)
            sys.stdout.write(out)
            sys.stdout.flush()

            if stage in ("entering", "exiting") and frame % 2 == 0:
                ufo_x -= 1
            frame += 1

            if ufo_x + UFO_W < 0:
                break

            elapsed = time.perf_counter() - t0
            st = FRAME_T - elapsed
            if st > 0:
                time.sleep(st)
    finally:
        sys.stdout.write("\033[?25h\033[0m")
        sys.stdout.flush()
