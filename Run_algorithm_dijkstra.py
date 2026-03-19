start_city = "Delhi"
result = dijkstra(graph, start_city)

for city, dist in result.items():
    print(f"{start_city} -> {city} = {dist} km")
