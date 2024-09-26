import time
import random

index = 0


def main():

    time.sleep(0.001)


    global index
    print(f"{index}")

    r = random.randrange(0, 10)

    if(r > 8):
        index += 1
    main()


main()