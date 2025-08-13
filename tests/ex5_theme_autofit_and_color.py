import time, os
from braille_progress import Progress, ProgressTheme


def main():
    theme = ProgressTheme.auto_fit()

    prog = Progress(force_tty=True, force_color=True, theme=theme)

    with prog.task("auto-fit demo", total=50) as t:
        for i in range(50):
            time.sleep(0.02)
            t.advance(stage="writing", label=f"row_{i:03d}")

    prog.close()

if __name__ == "__main__":
    main()
