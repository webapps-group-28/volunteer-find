import pgeocode
nomi = pgeocode.Nominatim("gb")
nomi.query_postal_code("sm1 1rl")
print(nomi.query_postal_code("sm1 1rl")["longitude"])
