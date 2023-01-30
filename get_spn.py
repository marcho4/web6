def get_spn(toponym):
    spn_get = toponym['boundedBy']['Envelope']
    l, b = spn_get['lowerCorner'].split(' ')
    r, u = spn_get['upperCorner'].split(' ')
    delta_x = str(abs(float(l) - float(r)))
    delta_y = str(abs(float(b) - float(u)))
    return delta_x, delta_y