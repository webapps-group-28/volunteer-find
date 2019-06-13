import postcodes_io_api

def lat_long_from_postcode(postcode):
    api  = postcodes_io_api.Api(debug_http=True)
    data = api.get_postcode(postcode)['result']
    lat = data['latitude']
    lng = data['longitude']
    return lat, lng
