import sys
import Image
def color2v(r, g, b):
    '''convert a color tuple to value v.
       If a color does not lie in the valid range,
       -1 is returned.
       0<=v<0.11, v only affects b.  r = g = 0, 127 <= b < 255
       0.11<=v<0.125, v affects nothing. r=g=0, b=255. 
       0.125 <=v < 0.34, r = 0, b=255, v affects only g,  
       0.34 <= v < 0.35, r = 0, v affects b and g
       0.35 <= v < 0.375, v affects r, g, and b, r < 127
       0.375 <= v < 0.64, g = 255, v affects r and b,
       0.64 <= v < 0.65,  v affects r, g, and b, r > 127
       0.65 <= v < 0.66,  b = 0, v affects r and g, g > 127
       0.66 <= v < 0.89,  b = 0, r = 255, v affects g
       0.89 <= v < 0.91,  b = 0, v affects r and g, g < 127
       0.91 <= v <= 1,    g = 0, b = 0, v affects r. 127 <= r <=255
    '''
    eps = 0.1
    v = -1
    if r == 0 and g == 0 and 127 <= b <= 255: 
        v = (b / 255.0 - 0.5) * 0.11 / 0.5
        if v < 0: v = 0
    elif r == 0 and b == 255: #0.125<= v < 0.34
        v = (g / 255.0 * 0.25) + 0.125
    elif r == 0: #0.34 <= v < 0.35
        v1 = (g / 255.0 * 0.25) + 0.125
        v2 = (1 - b / 255.0) * 0.31 + 0.34
        if abs(v1 - v2) > eps:
            v = -1
        else:
            v = v1
    elif g < 255 and r < 127: #0.35 <= v < 0.375

        v1 = (r / 255.0 * 0.31) + 0.35
        v2 = (g / 255.0 * 0.25) + 0.125
        v3 = (1 - b / 255.0) * 0.31 + 0.34
        if abs(v1 - v2) > eps or abs(v2 - v3) > eps or abs(v1 - v3) > eps:
            v = -1
        else:
            v = v1
    elif g == 255: #0.375 <= v < 0.64
        v1 = (r / 255.0 * 0.31) + 0.35
        v3 = (1 - b / 255.0) * 0.31 + 0.34
        if abs(v1 - v3) > eps:
            v = -1
        else:
            v = v1
    elif r >= 127 and b > 0: #0.64 <= v < 0.65
        v1 = (r / 255.0 * 0.31) + 0.35
        v2 = (1 - g / 255.0) * 0.27 + 0.64
        v3 = (1 - b / 255.0) * 0.31 + 0.34
        if abs(v1 - v2) > eps or abs(v2 - v3) > eps or abs(v1 - v3) > eps:
            v = -1
        else:
            v = v1
        
    elif b == 0 and r == 255: #ignore some invalid g values 0.66<=v<0.89
        v = ( 1 - g / 255.0) * 0.27 + 0.64
    elif b == 0 and g > 127: #0.65<=v<=0.66
        v1 = (r / 255.0 * 0.31) + 0.35
        v2 = ( 1 - g / 255.0) * 0.27 + 0.64
        if abs(v1 - v2) > eps:
            v = -1
        else:
            v = v1
    elif b == 0 and 0 < g < 127: #0.89 <=v < 0.91
        v1 = (1 - r / 255.0) * 0.22 + 0.89
        v2 = (1 - g / 255.0) * 0.27 + 0.64
        if abs(v1 - v2) > eps:
            v = -1
        else:
            v = v1
    elif b == 0 and g == 0 and 127 <= r <= 255: #v >= 0.89
        if r == 127: 
            v = 1
        else:
            v = ( 1 - r / 255.0) * 0.22 + 0.89
    if 0<=v<=1:
        return v
    else:
        return -1

def convertColor(color):
    if len(color) == 3:
        r, g, b = color
        a = 255
    else:
        r, g, b, a = color
    v = color2v(r, g, b)
    v = int(v*255)
    if v < 0:
        l = r * 299/1000 + g * 587/1000 + b * 114/1000
        color = (l, l, l, a)
    else:
        color = (v, v, v, a)
    return color
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage " + sys.argv[0] + " <input image file> <output image file>"
        sys.exit(1)
    im = Image.open(sys.argv[1])
    seq = list(im.getdata())
    for i in range(len(seq)):
        seq[i] = convertColor(seq[i])
    im.putdata(seq)
    im.save(sys.argv[2])


