"""This is a simple Python script that demonstrates a basic greet function 
and some intentional errors for testing purposes."""

def greet(name):
    """Print a greeting message for the given name."""
    print("Hello, " + name)

greet("Alice")
greet("Bob")

# Intentional errors below

print(greet("Charlie")) # Missing closing parenthesis

X = 10
Y = 20
RESULT = X + Y  # Trying to add a string and integer
print(RESULT)
