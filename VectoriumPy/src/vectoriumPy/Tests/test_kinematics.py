from vectoriumPy.Kinematics import motion,avg_velocity,angular_velocity,angular_acceleration,momentum,impulse,Tangential_velocity
import pytest
def test_motion():
    # Test case 1: Calculate final velocity given initial velocity, acceleration, and time
    assert motion(0, None, 2, 5,0) == 10

    # Test case 2: Calculate initial velocity given final velocity, acceleration, and time
    assert motion(None, 10, 2, 5,0) == 0

    # Test case 3: Calculate acceleration given initial velocity, final velocity, and time
    assert motion(0, 10, None, 5,0) == 2

    # Test case 4: Calculate time given initial velocity, final velocity, and acceleration
    assert motion(0, 10, 2, None,0) == 5

    # Test case 5: Calculate displacement given initial velocity, acceleration, and time
    assert motion(10,0,5,6,None) == 150

    # Test case 6: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        motion(None, None, 2, 5,0)
def test_avg_velocity():
    # Test case 1: Calculate average velocity given initial and final velocities
    assert avg_velocity(0, 10) == 5

    # Test case 2: Raise ValueError when either initial or final velocity is None
    with pytest.raises(ValueError):
        avg_velocity(None, 10)
    with pytest.raises(ValueError):
        avg_velocity(0, None)
def test_angular_velocity():
    # Test case 1: Calculate angular velocity given angular displacement and time
    assert angular_velocity(90, 2, None) == 45

    # Test case 2: Calculate angular displacement given angular velocity and time
    assert angular_velocity(None, 2, 45) == 90

    # Test case 3: Calculate time given angular displacement and angular velocity
    assert angular_velocity(90, None, 45) == 2

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        angular_velocity(None, None, 45)
def test_angular_acceleration():
    # Test case 1: Calculate angular acceleration given angular velocity and time
    assert angular_acceleration(45, 2, None) == 22.5

    # Test case 2: Calculate angular velocity given angular acceleration and time
    assert angular_acceleration(None, 2, 22.5) == 45

    # Test case 3: Calculate time given angular velocity and angular acceleration
    assert angular_acceleration(45, None, 22.5) == 2

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        angular_acceleration(None, None, 22.5)

def test_momentum():
    # Test case 1: Calculate momentum given mass and velocity
    assert momentum(10,10,None)==100

    # Test case 2: Calculate mass given momentum and velocity
    assert momentum(None,20,200) == 10

    # Test case 3: Calculate velocity given momentum and mass
    assert momentum(50,None,1000) == 20

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        momentum(None, None, 22.5)

def test_impulse():
 # Test case 1: Calculate impulse given Force and time
    assert impulse(100,10,None) == 1000

    # Test case 2: Calculate force given impulse and time
    assert impulse(None,20,200) == 10

    # Test case 3: Calculate time given impulse and force
    assert impulse(100,None,1000) == 10
    
    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        impulse(None, None, 22.5)
def test_Tangential_velocity():
    # Test case 1: Calculate tangential velocity given angular velocity and radius of curvature
    assert Tangential_velocity(None, 2, 10) == 20

    # Test case 2: Calculate angular velocity given tangential velocity and radius of curvature
    assert Tangential_velocity(20, 2, None) == 10

    # Test case 3: Calculate radius of curvature given tangential velocity and angular velocity
    assert Tangential_velocity(20, None, 10) == 2

    # Test case 4: Raise ValueError when more than one parameter is None
    with pytest.raises(ValueError):
        Tangential_velocity(None, None, 10)

        