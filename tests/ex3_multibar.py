import time
from braille_progress import Progress

def main():
    prog = Progress(force_tty=True, force_color=True)

    a = prog.add("aa.zip", total=26)
    b = prog.add("bb.zip", total=14)
    c = prog.add("cc.zip", total=20)

    i = j = k = 0
    while not prog.all_finished():
        if i < 26:
            a.advance(1, stage="writing", label=f"case_{i:02d}")
            i += 1
        if j < 14:
            b.advance(1, stage="writing", label=f"unit_{j:02d}")
            j += 1
        if k < 20:
            c.advance(1, stage="writing", label=f"task_{k:02d}")
            k += 1

        time.sleep(0.03)

        if i == 26 and j == 14 and k == 20:
            prog.done(a); prog.done(b); prog.done(c)

    prog.close()

if __name__ == "__main__":
    main()
