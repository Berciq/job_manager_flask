from geopy.geocoders import Nominatim

job1 = "Bieruńska 78, 43-200 Pszczyna"
job2 = "Stanisława Wyspiańskiego 5A, 43-300 Bielsko-Biała"
job3 = "Parkowa 24, 43-200 Pszczyna"
job4 = "Graniczna 2, 44-335 Jastrzębie-Zdrój"
job5 = "Leśna 9, 43-300 Bielsko-Biała"


def get_coords(address):
    geolocator = Nominatim(user_agent="test")
    location = geolocator.geocode(address)
    lat = location.latitude
    lon = location.longitude
    return lat, lon


cords1 = get_coords(job1)
cords2 = get_coords(job2)
cords3 = get_coords(job3)
cords4 = get_coords(job4)
cords5 = get_coords(job5)

print(cords1, cords2, cords3, cords4, cords5)
(49.99188045, 18.964938948006292)
(49.82095215, 19.036872725057876)
(49.9802218, 18.9515217)
(49.9536365, 18.615242002167193)
(49.811287449999995, 19.096390975771435)
