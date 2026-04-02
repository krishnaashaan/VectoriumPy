"""
Thermodynamics module for VectoriumPy.

This module provides functions and classes for thermodynamics calculations, including:
- First Law of Thermodynamics
- Entropy
- Enthalpy
- Gibbs free energy
- Helmholtz Free Energy 
- Ideal Gas Law
"""
def first_law_thermodynamics(U,Q,W):
 """
 Calculates the change in internal energy (ΔU) using the first law of thermodynamics.
    Parameters:
    U (float): Initial internal energy (in joules).
    Q (float): Heat added to the system (in joules).
    W (float): Work done by the system (in joules).
    Returns:
    float: Change in internal energy (ΔU) in joules.
    equation: ΔU = Q-W
  """
 known = [U,Q,W].count(None)
 if known > 1:
  raise ValueError("At least two parameters must be provided.")

 elif U is None: 
  U = Q-W
  return U
 elif Q is None:
  Q = U+W
  return Q
 elif W is None:
  W = Q-U
  return W
 
def entropy(Q,T,ΔS):
    """
    Calculates the change in entropy (ΔS) using the formula ΔS = Q/T.
        Parameters:
        Q (float): Heat added to the system (in joules).
        T (float): Absolute temperature (in kelvin).
        Returns:
        float: Change in entropy (ΔS) in joules per kelvin.
    """
    known_missing = [Q, T, ΔS].count(None)
    if known_missing > 1:
     raise ValueError("At least two parameters must be provided.")

    if T is not None and T <= 0:
     raise ValueError("Temperature must be greater than zero.")

    if ΔS is None:
     ΔS = Q / T
     return ΔS
    if Q is None:
     Q = ΔS * T
     return Q
    if T is None:
     T = Q / ΔS
     return T

def enthalpy(H,U,P,V):
 """
 Calculates the enthalpy (H) using H = U + PV.
    parameters:
    H (float): Enthalpy (in joules).
    U (float): Internal energy (in joules).
    P (float): Pressure (in pascals).
    V (float): Volume (in cubic meters).
 """
 known = [H,U,P,V].count(None)
 if known > 1:
  raise ValueError("At least two parameters must be provided.")
 elif H is None:
  H = U + P*V
  return H
 elif U is None:
  U = H - P*V
  return U
 elif P is None:
  P = (H-U)/V
  return P
 elif V is None:
  V = (H-U)/P
  return V
 
def Gibbs_free_energy(G,H,T,S):
  """
  Calculates the Gibbs free energy (G) using G = H - TS.
    Parameters:
    G (float): Gibbs free energy (in joules).
    H (float): Enthalpy (in joules).
    T (float): Absolute temperature (in kelvin).
    S (float): Entropy (in joules per kelvin).
  """
  known = [G,H,T,S].count(None)
  if known > 1:
   raise ValueError("At least two parameters must be provided.")
  elif T is not None and T <= 0:
    raise ValueError("Temperature must be greater than zero.")
  
  elif G is None:
   G = H - T*S
   return G
  elif H is None:
   H = G + T*S
   return H
  elif T is None:
   T = (H-G)/S
   return T
  elif S is None:
   S = (H-G)/T
   return S

def Helmholtz_free_energy(A,U,T,S):
    """
    Calculates the Helmholtz free energy (A) using A = U - TS.
        Parameters:
        A (float): Helmholtz free energy (in joules).
        U (float): Internal energy (in joules).
        T (float): Absolute temperature (in kelvin).
        S (float): Entropy (in joules per kelvin).
    """
    known = [A,U,T,S].count(None)
    if known > 1:
     raise ValueError("At least two parameters must be provided.")
    elif T is not None and T <= 0:
        raise ValueError("Temperature must be greater than zero.")
    
    elif A is None:
     A = U - T*S
     return A
    elif U is None:
     U = A + T*S
     return U
    elif T is None:
     T = (U-A)/S
     return T
    elif S is None:
     S = (U-A)/T
     return S

def ideal_gas_law(P,V,n,T,R):
 """
    Calculates the pressure (P) of an ideal gas using the ideal gas law PV = nRT.
    Parameters:
     P (float): Pressure (in pascals).
     V (float): Volume (in cubic meters).
     n (float): Number of moles.
     T (float): Absolute temperature (in kelvin).
     R (float): Universal gas constant(Often 0.0821 L·atm/mol·K OR 8.314 J/mol·K) (in joules per mole per kelvin).
     Returns:
     float: Pressure (in pascals).
    """
 known = [P,V,n,T,R].count(None)
 if known > 1:
  raise ValueError("At least two parameters must be provided.")
 
 if T is not None and T <= 0:
        raise ValueError("Temperature must be greater than zero.")
 
 elif P is None:
    P = n*R*T/V
    return P
 elif V is None:
    V = n*R*T/P
    return V
 elif n is None:
    n = P*V/(R*T)
    return n
 elif R is None:
    R = P*V/(n*T)
    return R
 elif T is None:
    T = P*V/(n*R)
    return T
# More functions will be added in the future.