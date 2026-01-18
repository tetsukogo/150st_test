print("hello world")

def greet():
    print("こんにちは")

greet()

def print_name(name):
    print(f"私の名前は{name}です")

print_name("田中")

def get_greet():
    return "おはようございます"

greeting = get_greet()
print(greeting)

def add(a, b):
    return a + b

result = add(3, 6)
print(result)