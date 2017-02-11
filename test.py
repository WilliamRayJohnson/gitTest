from datetime import datetime

def test():
    print("This is a test.")
    print("Performed at {}".format(str(datetime.now())))

def main():
    test()

if __name__ == '__main__':
    main()
