a=30
b=9

# arithmetic operators

# addition
print("Addition for two operators is: ", a+b)

# subtraction
print("Subtraction for two operators is: ", a-b)

# multiplication
print("Multiplication for two operators is: ", a*b)

# division
print("Division for two operators is: ", a/b)

# modulus or remainder
print("Modulus for two operators is: ", a%b)
print("Remainder for two operators is: ", a%b)

# exponentiation
print("Exponentiation for two operators is: ", a**b)

# floor division
print("Floor division for two operators is: ", a//b)

# comparison operators

c=50
d=12

# greater than
#print("Greater than operator is: ", c>d)
print(f"{c} is greater than {d}: {c>d}")


# less than
#print("Less than operator is: ", c<d)
print(f"{c} is less than {d}: {c<d}")

# greater than or equal to
#print("Greater than or equal to operator is: ", c>=d)
print(f"{c} is greater than or equal to {d}: {c>=d}")

# less than or equal to
#print("Less than or equal to operator is: ", c<=d)
print(f"{c} is less than or equal to {d}: {c<=d}")

# equal to
#print("Equal to operator is: ", c==d)
print(f"{c} and {d} are equal: {c==d}")

# not equal to
#print("Not equal to operator is: ", c!=d)
print(f"{c} and {d} are not equal: {c!=d}")

# logical operators

e=10
print(f"Is this statement true: {e>5 and e<10}")
print(f"Is this statement true: {e>5 or e<10}")
print("Each statement is true then return false and vice versa: ", (not(e>5 and e<10)))

#assignment operators

f=20
g=40

# addition assignment
f+=g
print("Addition assignment is: ", f)

# subtraction assignment
f-=g
print("Subtraction assignment is: ", f)

# multiplication assignment
f*=g
print("Multiplication assignment is: ", f)

# division assignment
f/=g
print("Division assignment is: ", f)

# modulus assignment
f%=g
print("Modulus assignment is: ", f)

# exponentiation assignment
f**=g
print("Exponentiation assignment is: ", f)

# floor division assignment
f//=g
print("Floor division assignment is: ", f)

# bitwise operators

h=10
i=4

# bitwise AND
print("Bitwise AND is: ", h&i)

# bitwise OR
print("Bitwise OR is: ", h|i)

# bitwise XOR
print("Bitwise XOR is: ", h^i)

# bitwise NOT
print("Bitwise NOT is: ", ~h)

# bitwise left shift
print("Bitwise left shift is: ", h<<i)

# bitwise right shift
print("Bitwise right shift is: ", h>>i)

# membership operators

j=[1,2,3,4,5]

# in operator
print("In operator is: ", 3 in j)

# not in operator
print("Not in operator is: ", 6 not in j)

# identity operators

k=10
l=10

# is operator
print("Is operator is: ", k is l)

# is not operator
print("Is not operator is: ", k is not l)

# operator precedence

m=10
n=20
o=30
p=40

# precedence of operators
print("Precedence of operators is: ", m+n*o/p)

# grouping of operators
print("Grouping of operators is: ", (m+n)*(o/p))

# comparison of operators
print("Comparison of operators is: ", m==n)

# logical operators
print("Logical operators is: ", m<n and n<o)

# identity operators
print("Identity operators is: ", m is n)

# membership operators
print("Membership operators is: ", m in j)

# bitwise operators
print("Bitwise operators is: ", m&n)

# arithmetic operators
print("Arithmetic operators is: ", m+n)
