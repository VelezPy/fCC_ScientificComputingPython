'''
The counter variable counts how many times we execute
a loop. It starts at zero and we add one to it each
time through the loop. 
'''

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
