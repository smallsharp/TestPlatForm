import time


def cgTimestamp2yy(intTime):
    return time.strftime("%Y-%m-%d", time.localtime(intTime))


if __name__ == '__main__':
    cgTimestamp2yy()
