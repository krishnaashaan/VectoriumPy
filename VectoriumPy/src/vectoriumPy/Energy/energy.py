"""
This module contains funtions for energy calculations in vectoriumPy.
"""
import numpy as np

def Kinetic_energy(KE,m,v):
    '''
    This function calculates the kinetic energy (KE) of an object given its mass (m) and velocity (v).
    KE = 0.5 * m * v^2
    parameters:
    KE(float):Kinetic energy (J)
    m(float):Mass of the object (kg)
    v(float):Velocity of the object (m/s)
    '''
    values = [KE,m,v].count("?")
    if values > 1:
        raise ValueError("Please provide values for both mass (m) and velocity (v).")
    if KE == "?":
        KE = 0.5 * m * v**2
        return KE
    elif m == "?":
        m = 2 * KE / v**2
        return m
    elif v == "?":
        v = (2 * KE / m)**0.5
        return v
    
def Potential_energy(PE,m,g,h):
    """
    this function calculates the potential energy (PE) of an object given its mass (m), gravitational acceleration (g), and height (h).
    PE = m * g * h
    parameters:
    PE(float):Potential energy (J)
    m(float):Mass of the object (kg)
    g(float):Gravitational acceleration (m/s^2)
    h(float):Height of the object (m)
    """
    values = [PE,m,g,h].count("?")
    g = 9.8 
    if values > 1:
        raise ValueError("Please provide values for all parameters.")
    if PE == "?":
        PE = m * g * h
        return PE
    elif m == "?":
        m = PE / (g * h)
        return m
    elif g == "?":
        g = PE / (m * h)
        return g
    elif h == "?":
        h = PE / (m * g)
        return h
    
def Mechanical_energy(ME,KE,PE):
    """
    This function calculates the mechanical energy (ME) of an object given its kinetic energy (KE) and potential energy (PE).
    ME = KE + PE
    parameters:
    ME(float):Mechanical energy (J)
    KE(float):Kinetic energy (J)
    PE(float):Potential energy (J)
    """
    values = [ME,KE,PE].count("?")
    if values > 1:
        raise ValueError("Please provide values for both kinetic energy (KE) and potential energy (PE).")
    if ME == "?":
        ME = KE + PE
        return ME
    elif KE == "?":
        KE = ME - PE
        return KE
    elif PE == "?":
        PE = ME - KE
        return PE
    
def Work(F,d,θ,W):
    """
    This function calculates work done (W) using Force(F), displacement(d) and angle of application(θ).
    W = F * d * cos(θ)"""
    
    values = [F,d,θ,W].count("?")
    if values > 1:
        raise ValueError("Please provide values for force (F), displacement (d), and angle of application (θ).")
    if W == "?":
        W = F * d*np.cos(np.radians(θ))
        return W
    elif F == "?":
        F = W/(d * np.cos(np.radians(θ)))
        return F
    elif d == "?":
        d = W/(F * np.cos(np.radians(θ)))
        return d
    elif θ == "?":
        θ = np.degrees(np.arccos(W/(F * d)))
        return θ
        
def Power(P,W,t):
    """
    This function calculates power (P) given work done (W) and time taken (t).
    P = W/t
    parameters:
    P(float):Power (W)
    W(float):Work done (J)
    t(float):Time taken (s)
    """
    values = [P,W,t].count("?")
    if values > 1:
        raise ValueError("Please provide values for both work done (W) and time taken (t).")
    if P == "?":
        P = W/t
        return P
    elif W == "?":
        W = P*t
        return W
    elif t == "?":
        t = W/P
        return t

## More functions will be added in future updates.
