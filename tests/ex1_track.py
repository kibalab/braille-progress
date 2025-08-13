import time
from braille_progress import Progress

def main():
    data = range(100)

    # label_from 로 각 아이템 라벨 지정 가능
    prog = Progress(force_tty=True, force_color=True)  # 자동 컬러/브라유/레이아웃 적용
    for i in prog.track(data, description="download", label_from=lambda x: f"item_{x:03d}"):
        # 실제 작업
        time.sleep(0.02)

    prog.close()

if __name__ == "__main__":
    main()
