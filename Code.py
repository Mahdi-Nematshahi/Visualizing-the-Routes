import osmnx as ox
import webbrowser

origin_pt = input("Please enter origin_coordinates in tuple form: ")
origin_pt = tuple(map(float, origin_pt.split(',')))
destination_pt = input("Please enter destination_coordinates in tuple form: ")
destination_pt = tuple(map(float, destination_pt.split(',')))

place = 'Stockholm, Sweden'
mode = 'drive'
optimizer = 'length'
graph = ox.graph_from_place(place, network_type=mode)
orig_node = ox.get_nearest_node(graph, origin_pt)
dest_node = ox.get_nearest_node(graph, destination_pt)
k_shortest_routes = ox.k_shortest_paths(graph, orig_node, dest_node, k=10, weight=optimizer)

final_route = []
for list_k_route in k_shortest_routes:
    final_route.append(list_k_route)

list_colors = ['black', 'brown', 'green', 'cyan', 'gold', 'pink', 'white', 'yellow', 'tan', 'olive']
for counter in range(len(final_route)):
    if counter == 0:
        shortest_route_map = ox.plot_route_folium(graph, final_route[0],
                                                  route_color=list_colors[0], tiles="cartodbpositron")
    else:
        shortest_route_map = ox.plot_route_folium(graph, final_route[counter], route_color=list_colors[counter],
                                                  route_map=shortest_route_map, tiles="cartodbpositron")


filepath = f"route1.html"
shortest_route_map.save(filepath)
webbrowser.open(f"route1.html")