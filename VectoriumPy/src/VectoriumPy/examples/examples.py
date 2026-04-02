from VectoriumPy import motion,momentum,impulse,Kinetic_energy,Potential_energy,Mechanical_energy

# Example of motion function
print("Motion Example:")
solver = motion(10,None,5,1,0)
print(f'Final velocity: {solver:.2f} m/s')

print("\nMomentum Example:")
# Example of momentum function
solver_momentum = momentum(20,5,None)
print(f'Momentum: {solver_momentum:.2f} kg*m/s')

print("\nImpulse Example:")
# Example of impulse function
solver_impulse = impulse(20,5,None)
print(f'Impulse: {solver_impulse:.2f} N*s')

print("\nKinetic Energy Example:")
# Example of Energy  related function
solver_kinetic = Kinetic_energy(None,50,10)
print(f'Kinetic Energy: {solver_kinetic:.2f} J')

print("\nPotential Energy Example:")
solver_potential = Potential_energy(None,50,9.8,10)
print(f'Potential Energy: {solver_potential:.2f} J')

print("\nMechanical Energy Example:")
solver_mechanical = Mechanical_energy(None,solver_kinetic,solver_potential)
print(f'Mechanical Energy: {solver_mechanical:.2f} J')

