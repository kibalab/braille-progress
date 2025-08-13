import time
from braille_progress import Progress

def main():
    prog = Progress(force_tty=True, force_color=True)

    with prog.task("indexing", total=42) as t:
        for i in range(42):
            time.sleep(0.03)
            t.advance(1, stage="writing", label=f"doc_{i:04d}")

    prog.close()

if __name__ == "__main__":
    main()
