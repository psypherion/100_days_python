def prime_checker(n):
  count = 1
  s = 0
  for i in range (1,n-1):
    count += 1
    if n%count == 0 :
      s += 1
  if s == 0:
    print("Prime Number")
  else :
    print("Composite Number")
ip = int(input("Enter A no. To Check : "))
prime_checker(ip)
