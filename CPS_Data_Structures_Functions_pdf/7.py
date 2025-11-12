size = 10
moves = [3, 2,-1, 5,-8, 2]

def simulate_movement(size,moves):
    c=0
    while c<size:
        for i in moves:
            c+=i
            if c<0:
                c=0
                return c
        if c>size:
            c=size-1
            return c
        return c

print(simulate_movement(size,moves))