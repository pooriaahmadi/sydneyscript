from .main import *
import sys


def main():
    while True:
        if len(sys.argv) > 1:
            if sys.argv[1].split(".")[-1] != "syd":
                print("File not supported.")
                break
            result, error = run('<stdin>', f"UWU(\"{sys.argv[1]}\")")
            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
            break
        else:
            text = input('SydneyScript > ')
            if text.strip() == "":
                continue
            result, error = run('<stdin>', text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))


if __name__ == "__main__":
    main()
