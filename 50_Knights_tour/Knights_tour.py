w = int(input("Board width: "))
h = int(input("Board height: "))

s1 = int(input("starting width: "))
s2 = int(input("starting height: "))

#I'm intentionally leaving out smaller boards because that's not the objective
#of this program. It's about Warndorf's rule.

if w < 5:
    print("Let's make things less complicated and up that to 5, shall we?")
    w = 5

if h < 5:
    print("Let's make things less complicated and up that to 5, shall we?")
    h = 5

matrix = [[0 for x in range(w)] for y in range(h)]

