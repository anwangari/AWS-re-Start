# define a variable to store prime numbers
prime_numbers = []

for i in range(2,250):
  # append all numbers not divisible by 2 in the prime_numbers variable
  if i % 2 != 0 or i / 2 == 1:
    prime_numbers.append(i)

  """
  remove all numbers which are divisible by any number from prime_number:
  This leaves prime_numbers with numbers which cannot be divided by other
  numbers other than themselves
  """
  for x in prime_numbers:
    if i > x and i in prime_numbers and i % x == 0:
      prime_numbers.remove(i)

# confirm length of prime_numbers is 53
print(len(prime_numbers))

# write prime_numbers in a .txt file
with open("prime-numbers.txt", 'w') as f:
  for i in prime_numbers:
    f.write(f", {str(i)}")
f.close()
