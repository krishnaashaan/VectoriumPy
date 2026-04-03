"""
module for Mirror and lens related calculations
"""
def mirror_formula(f,u,v):
    """
    Calculates focal length(f) using object distance(u),image distance(v)
    1/f = 1/u + 1/v
    parameters:
    f(float):Focal length (Distance from the mirror/lens centre to the focal point)
    v(float): Image distance (Distance from the mirror/lens to the image)
    u(float): Object distance (Distance from the mirror/lens to the object)
    
    """
    known =[f,u,v].count("?")
    if known>1:
        raise ValueError('Provide at least 2 numerical values to solve.')
    if f == '?':
        f = (u * v) / (u + v)
        return round(f,2)
    elif u == '?':
        u = (f*v) / (v-f)
        return round(u,2)
    elif v == '?':
        if v == f: # Check if v - f would be 0
          return "Error: Image is at the focal point (u is at infinity)."
        v = (f*u) /(u-f)
        return round(v,2)

def lens_formula(f,v,u):
    """
    Calculates focal length(f) using object distance(u),image distance(v)
    1/f =1/v - 1/u
    parameters:
    f(float):Focal length (Distance from the mirror/lens centre to the focal point)
    v(float): Image distance (Distance from the mirror/lens to the image)
    u(float): Object distance (Distance from the mirror/lens to the object)
    """
    knowns = [f,v,u].count('?')
    if knowns >1:
        raise ValueError("Provide at least 2 numerical values to solve")
    elif f == "?":
        if (u == v): # Avoids division by zero (1/v - 1/v = 0)
           return "Error: f is at infinity (u and v are equal)"
        f = (v*u)/(u-v)
        return round(f,2)
    elif v == "?":
        if (u == -f): # Avoids division by zero (1/f + 1/-f = 0)
            return "Error: Image is at infinity (Object at focal point)."
        v = (f*u)/(f-u)
        return round(v,2)
    elif u == "?":
        if (v == f): # Avoids division by zero (1/v - 1/v = 0)
            return "Error: Object is at infinity."
        u = (f*v)/(f-v)
        return round(u,2)
    
   