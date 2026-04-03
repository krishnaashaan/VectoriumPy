"""
Tis module contains the force calculation functions for vectoriumPy.
"""
import math

import numpy as np

def electrostatic_force(q1, q2, r, F):
    '''
    This function calculates the electrostatic force between two charges (q1 and q2) separated by a distance (r).
    F = k * (q1 * q2) / r^2
    parameters:
    q1(float):Charge of the first object (C)
    q2(float):Charge of the second object (C)
    r(float):Distance between q1 and q2 (m)
    F(float):Electrostatic force between q1 and q2 (N)
    '''
    k = 8.9875517923e9  # Coulomb's constant
    values = [q1, q2, r, F].count("?")
    if values > 1:
        raise ValueError("Please provide values for all but one parameter (q1, q2, r, F).")
    if q1 == "?":
        return F * r**2 / (k * q2)
    elif q2 == "?":
        return F * r**2 / (k * q1)
    elif r == "?":
        return (k * q1 * q2 / F) ** 0.5
    elif F == "?":
        return k * q1 * q2 / r**2
       
def Torque(τ,F,r,θ):
    '''
    This function calculates the torque (τ) produced by a force (F) applied at a distance (r) from the pivot point and at an angle (θ).
    τ = F * r * sin(θ)
    paramenters:
    τ(float):Torque(Nm)
    F(float):Force applied (N)
    r(float):Distance from the pivot point (m)
    θ(float):Angle between the force and the line from the pivot to the point of application (degrees)
    '''
    values = [F, r, θ, τ].count("?")
    if values > 1:
        raise ValueError("Please provide values for the force (F), distance (r), and angle (θ).")
    if τ == "?":
        return F * r * np.sin(np.radians(θ))
    elif F == "?":
        return τ / (r * np.sin(np.radians(θ)))
    elif r == "?":
        return τ / (F * np.sin(np.radians(θ)))
    elif θ == "?":
        return np.arcsin(τ / (F * r))
    
def Frictional_force(F,μ,N):
    """
    This function calculates frictional force (F) given the coefficient of friction (μ) and the normal force (N).
    F = μ * N
    parameters:
    F(float):Frictional force (N)
    μ(float):Coefficient of friction
    N(float):Normal force (N)
    """
    values = [F, μ, N].count("?")
    if values>1:
        raise ValueError('Please provide values for both the coefficient of friction(μ) and the normal force(N).')
    if F == "?":
        return μ*N
    elif μ == "?":
        return F/N
    elif N == "?":
        return F/μ
    
def centripetal_force(m,v,r,F):
    """
    This function calculates the centripetal force (F) acting on an object of mass (m) moving with velocity (v) in a circular path of radius (r).
    F = m * v^2 / r
    parameters:
    F(float):Centripetal force (N) 
    m(float):Mass of oject (kg)
    v(float):Velocity of object (m/s)
    r(float):Radius of circular path (m)
    """
    values = [m, v, r, F].count("?")
    if values > 1:
        raise ValueError("Please provide values for the mass (m), velocity (v), and radius (r).")
    if F == "?":
        return m * v**2 / r
    elif m == "?":
        return F * r / v**2
    elif v == "?":
        return (F * r / m) ** 0.5
    elif r == "?":
        return m * v**2 / F
    
def Hookes_law(F,k,x):
    """
     This function calculates the force(F) needed to extend or compress a spring by some distance (X)given the spring constant (k)
     F = -k *x

     parameters:
     F(float):the restoring force exerted by the spring.
     k(float):the spring constant, representing stiffness.
     x(float):the displacement from the equilibrium position (m).
    """
    none_count = [F, k, x].count("?")
    if none_count > 1:
        raise ValueError("Please provide values for the force (F), spring constant (k), and displacement (x).")
    if F == "?":
        return -k * x
    if k == "?":
        if x == 0:
            raise ZeroDivisionError("Displacement x cannot be zero when calculating spring constant k.")
        return -F / x
    if x == "?":
        if k == 0:
            raise ZeroDivisionError("Spring constant k cannot be zero when calculating displacement x.")
        return -F / k

def buoyant_force(F,ρ,V,g):
    """
    This function calculates the buoyant force (F) acting on an object submerged in a fluid, given the fluid density (ρ), volume of the displaced fluid (V), and acceleration due to gravity (g).
    F = ρ * V * g
    parameters:
    F(float):Buoyant force (N)
    ρ(float):Density of the fluid (kg/m^3)
    V(float):Volume of the displaced fluid (m^3)
    g(float):Acceleration due to gravity (m/s^2)
    """
    values = [F,ρ,V,g].count("?")
    if values > 1:
        raise ValueError("Please provide values for the fluid density (ρ), volume of the displaced fluid (V), and acceleration due to gravity (g).")
    if F == "?":
     F = ρ*V*g
     return F
    elif ρ == "?":
        ρ =(V*g)/F
        return ρ
    elif V == "?":
        V = (ρ*g)/F
        return V
    elif g == "?":
        g = F/(ρ*V)
        return g

def Tension(T,m,g,θ):
    """
    This function calculates the tension (T) in a rope or cable supporting a mass (m) under the influence of gravity (g).
    T = m * g * cos(θ)
    parameters:
    T(float):Tension in the rope (N)
    m(float):Mass being supported (kg)
    g(float):Acceleration due to gravity (m/s^2)
    θ(float):Angle of the rope with respect to the vertical (radians)
    """
    values = [T,m,g,θ].count("?")
    if values > 1:
        raise ValueError("Please provide values for the mass (m) and acceleration due to gravity (g).")
    if T == "?":
        return m * g * np.cos(θ)
    elif m == "?":
        return T / (g * np.cos(θ))
    elif g == "?":
        return T / (m * np.cos(θ))
    elif θ == "?":
        if m == 0 or g == 0:
            raise ZeroDivisionError("Mass (m) and acceleration due to gravity (g) cannot be zero when calculating the angle (θ).")
        θ = math.acos(T / (m * g))
        return θ

def Stress(σ,F,A):
   """
   This function calculates stress(σ) given force(F) & area(A).
    σ = F /A 
    note: Stress is defined as the force applied per unit area same as pressure but in the context of solids
    parameters:
    σ(float):Stress (Pa)
    F(float):Force applied (N)
    A(float):Area over which the force is applied (m^2)
    returns:
    σ(float):Stress (Pa)
   """
   knowns=[σ,F,A].count("?")
   if knowns > 1:
       raise ValueError("Please provide values for the force (F) and area (A).")
   if σ == "?":
       σ = F/A
       return σ
   elif F == "?":
       F = σ * A
       return F
   elif A == "?":
       A = F/σ
       return A

def Archimedes_principle(F,m,g):
    """
    This function calculates the buoyant force (F) acting on an object submerged in a fluid, given the mass of the displaced fluid (m) and acceleration due to gravity (g).
    F = m * g
    parameters:
    F(float):Buoyant force (N)
    m(float):Mass of the displaced fluid (kg)
    g(float):Acceleration due to gravity (m/s^2)
    """
    values = [F,m,g].count("?")
    if values > 1:
        raise ValueError("Please provide values for the mass of the displaced fluid (m) and acceleration due to gravity (g).")
    if F == "?":
        return m * g
    elif m == "?":
        return F / g
    elif g == "?":
        return F / m
    
def Lorentz_force(F,q,v,E,B):
    """
    This function calculates the Lorentz force acting on a charged particle moving in an electromagnetic field, given the charge (q), velocity (v), electric field (E), and magnetic field (B).
     F= q( E+  v * B)
    parameters:
        F(float):Lorentz force (N)
        q(float):Charge of the particle (C)
        v(float):Velocity of the particle (m/s)
        E(float):Electric field strength (V/m)
        B(float):Magnetic field strength (T)
    returns:
        F(float):Lorentz force (N)
    """
    known = [F,q,v,E,B].count("?")
    if known > 1:
        raise ValueError("Please provide values for the charge (q), velocity (v), electric field (E), and magnetic field (B).")
    if F == "?":
        F = q*(E+v*B)
        return F
    elif q == "?":
        q=F/(E+v*B)
        q = np.round(q,6)
        return q
    elif v == "?":
        v = (F/q - E) / B
        v= np.round(v,6)
        return v
    elif E == "?":
        E = F/q - v*B
        E = np.round(E,6)
        return E
    elif B == "?":
        B = (F/q - E) / v
        B = np.round(B,6)
        return B
def Lift(L,ρ,v,S,C_l):
    """
    This function calculates the lift force (L) acting on an object moving through a fluid, given the fluid density (ρ), velocity of the object (v), reference area (S), and lift coefficient (C_l).
    L = ½ * p*v**2*S*C_l
    parameters:
    L(float):Lift force (N)
    ρ(float):Density of  the fluid (kg/m^3)
    v(float):Velocity of the object (m/s)
    S(float):Reference area (m²)
    C_l(float): Lift coefficient (dimensionless)
    returns:
    L(float):Lift force (N)
    """
    known =[L,ρ,v,S,C_l].count("?")
    if known > 1:
        raise ValueError("Please provide values for the fluid density (ρ), velocity of the object (v), reference area (S), and lift coefficient (C_l).")
    if L == "?":
        L = 0.5 * ρ*v**2*S*C_l
        return L
    elif ρ == "?":
        ρ = (2*L)/(v**2*S*C_l)
        return ρ
    elif v == "?":
        v = ((2*L)/(ρ*S*C_l))**0.5
        return v
    elif S == "?":
        S = (2*L)/(ρ*v**2*C_l)
        S = np.ceil(S)
        return S
    elif C_l == "?":
        C_l = (2*L)/(ρ*v**2*S)
        return C_l
    
## More functions will be added in future updates.
        