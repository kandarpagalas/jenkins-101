import fire
import os


def hello(name="World"):
    params = os.environ
    for param in params:
        print(f"param: {param}")

    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire(hello)
