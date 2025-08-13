import time
import multiprocessing as mp
from braille_progress import Progress, progress_message


def worker(i: int, q: mp.Queue, name: str, total_cases: int = 24):
    q.put_nowait(progress_message(i, stage="OPENING"))
    time.sleep(0.05)
    q.put_nowait(progress_message(i, stage="SCANNING"))
    time.sleep(0.05)
    q.put_nowait(progress_message(i, stage="VALIDATED", total=total_cases))

    for k in range(1, total_cases + 1):
        time.sleep(0.03)
        label = f"{name}.test_{k:02d}"
        q.put_nowait(progress_message(i, stage="WRITING", done=k, total=total_cases, label=label))

    q.put_nowait(progress_message(i, stage="MD_ZIP"))
    time.sleep(0.02)
    q.put_nowait(progress_message(i, stage="MD_WRITTEN"))

    q.put_nowait(progress_message(i, final=True))

def main():
    mp.set_start_method("spawn", force=True)
    manager = mp.Manager()
    q = manager.Queue(maxsize=4096)

    names = ["aa.zip", "bb.zip", "cc.zip", "dd.zip"]
    procs = []

    prog = Progress()
    handles = [prog.add(n) for n in names]

    binder = prog.bind_queue(q)

    for i, n in enumerate(names):
        p = mp.Process(target=worker, args=(i, q, n))
        p.start()
        procs.append(p)

    while not prog.all_finished():
        changed = binder.drain()
        if changed:
            prog.render()
        time.sleep(0.02)

    for p in procs:
        p.join()

    prog.close()

if __name__ == "__main__":
    main()
