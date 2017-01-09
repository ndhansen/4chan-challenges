amount = int(input("How many pieces should be used? "))
stacks = {"s1": [x for x in range(amount, 0, -1)],
          "s2": [],
          "s3": []}

def movetower(stacks, pieces, sourcestack, deststack, altstack):
    if pieces == 1:
        stacks[deststack].append(stacks[sourcestack].pop())
    else:
        movetower(stacks, pieces - 1, sourcestack, altstack, deststack)
        stacks[deststack].append(stacks[sourcestack].pop())
        movetower(stacks, pieces - 1, altstack, deststack, sourcestack)
        
movetower(stacks, len(stacks["s1"]), "s1", "s3", "s2")
