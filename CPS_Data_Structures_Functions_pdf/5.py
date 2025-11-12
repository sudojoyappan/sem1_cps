visited = set(['http://example.com', 'http://google.com', 'http://test.com'])
new_links = ['http://google.com', 
             'http://python.org', 
             'http://example.com/about',
             'http://test.com']

def update_visited_links(visited, newlinks):
    newlinks=set(newlinks)
    return visited.union(newlinks)

print(update_visited_links(visited,new_links))