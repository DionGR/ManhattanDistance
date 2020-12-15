def mandist(lat_from, lon_from, lat_to, lon_to):
    from math import cos
    phi_m = 3.141592653589793/180 * (lat_from + lat_to) / 2
    lat_k = 111.13209 - 0.56605 * cos(2 * phi_m) + 0.00120 * cos(4 * phi_m)
    lon_k = 111.41513 * cos(phi_m) - 0.0945 * cos(3 * phi_m) + 0.00012*cos(5 * phi_m)
    fin_lat = (lat_from - lat_to) * lat_k
    fin_lon = (lon_from - lon_to) * lon_k
    return abs(fin_lon) + abs(fin_lat)