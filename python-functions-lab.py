#Challenge 1
def sum_to(n):
  i = 0
  sum = 0
  while(i < n):
    i += 1
    sum += i
  print(sum)

sum_to(6)

##Challenge 2
def largest(args):
  print('This is the largest number: ' + str(max(args)))

largest([1, 230, 35, 41, 5])

#Challenge 3
def occurances(word,letter):
  points=0
  if len(letter)==1:
    for l in word:
      if l == letter:
        points+=1
      else:
        points+=0
    print(points)
  else:
    x = word.split(letter)
  print(len(x)-1)  
  


occurances('hello','hl')
