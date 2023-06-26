import fire

def hello(name="World"):
  print(f"Hello {name}!")
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)