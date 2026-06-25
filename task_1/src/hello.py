import requests

def greet(name="World"):
    print(f"Hello, {name}!")
    print("Python virtual environment is working correctly.")
    print(f"requests library version: {requests.__version__}")

if __name__ == "__main__":
    greet("Synergy_TP")