# Nombrando una variable

# Snake Case
# nombre_y_apellido

# Pascal Case
# NombreApellido

# Constant Case
# NOMBRE_APELLIDO


backwards = input("Enter your palindrome:")

if backwards == backwards[::-1]:
    print("is a palindrome")
else:
    print("is not a palindrome")