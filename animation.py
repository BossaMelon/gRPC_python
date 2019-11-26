import time


def waiting_animation(n):
    animation = "|/-\\"
    idx = 0
    while True:
        print('\r', animation[idx % len(animation)], end='')
        idx += 1
        time.sleep(n)


if __name__ == '__main__':
    waiting_animation(0.5)
