def is_valid_point(data, lat, lon, anomalia):
  return data.iloc[lat, lon] != 0

def is_anomaly_point(data, lat, lon, anomalia):
  return  abs(anomalia) <= abs(data.iloc[lat, lon])

def regionQuery(data, lat, lon, search_space, anomalia):
  movement_search_space = search_space % 8 + 1
  range_search = [i for i in range(-1*movement_search_space, 1*movement_search_space + 1, 1)]
  points = [(lat, lon)]
  for i in range_search:
    for j in range_search:
      
      if(not (i == 0 and j == 0)):
        new_lat = lat + i
        new_lon = lon + j

        if(new_lat < 0):
          new_lat = new_lat  + data.shape[0]
          
        if(new_lon < 0):
          new_lon = new_lon  + data.shape[1]
        new_lat = new_lat % data.shape[0]
        new_lon = new_lon % data.shape[1]
        if(is_anomaly_point(data, new_lat, new_lon, anomalia)):
          points.append((new_lat, new_lon))

  return points


def expand_cluster(data, lat, lon, search_space, anomalia, min_neighboard, visited_neighboards, visited_point, point_cluster, id_cluster, clusters_points):
  all_neighboards = visited_neighboards
  
  for neighboard_i, neighboard_j in all_neighboards:

    if(not visited_point[neighboard_i, neighboard_j]):
      visited_point[neighboard_i, neighboard_j] = True
      neighboards = regionQuery(data= data, lat= neighboard_i, lon= neighboard_j, search_space = search_space, anomalia= anomalia,)
      
      if(min_neighboard < len(neighboards)):
        all_neighboards.pop()
        all_neighboards += neighboards
    
    if not (neighboard_i, neighboard_j) in clusters_points:
      point_cluster[neighboard_i, neighboard_j] = id_cluster
      clusters_points.add((neighboard_i, neighboard_j))


def cluster(data, anomalia, search_space, min_neighboard):
  visited_point = np.zeros(data.shape, dtype = bool)
  point_cluster = np.zeros(data.shape)
  clusters_points = set()
  id_cluster = 1

  for i in range(0, data.shape[0]):
    for j in range(0, data.shape[1]):
      if(not visited_point[i,j]):
        visited_point[i, j] = True

        if(is_valid_point(data, i, j, anomalia)):
          if(is_anomaly_point(data, i, j, anomalia)):
            neighboards = regionQuery(data= data, lat= i, lon= j, search_space = search_space, anomalia= anomalia)

            if(min_neighboard < len(neighboards)):
              expand_cluster(data= data, lat= i, lon= j, search_space = search_space, anomalia= anomalia, min_neighboard = min_neighboard, visited_neighboards = neighboards, visited_point = visited_point, point_cluster = point_cluster, id_cluster = id_cluster, clusters_points = clusters_points)
              id_cluster += 1
              
            else:
              point_cluster[i, j] = 0

          else:
            point_cluster[i, j] = -1

  return point_cluster