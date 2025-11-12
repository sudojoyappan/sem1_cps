server_loads = [10, 5, 2, 8]
new_tasks = 5

def distribute_tasks(server_loads, new_tasks):
    while new_tasks!=0:
        x=min(server_loads)
        f=server_loads.index(x)
        server_loads[f]+=1
        new_tasks-=1
    return server_loads

print(distribute_tasks(server_loads,new_tasks))
