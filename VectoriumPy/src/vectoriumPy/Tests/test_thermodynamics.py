from vectoriumPy import first_law_thermodynamics,entropy,enthalpy,Gibbs_free_energy,Helmholtz_free_energy,ideal_gas_law
def test_first_law_thermodynamics():
    # Case 1: ΔU is unknown
    assert first_law_thermodynamics('?', 50, 20) == 30
    # Case 2: Q is unknown
    assert first_law_thermodynamics(100, '?', 20) == 120
    # Case 3: W is unknown
    assert first_law_thermodynamics(100, 50, '?') == -50 # THE SYSTEM IS BEING COMPRESSED
    # Case 4: More than one parameter is unknown
    try:
        first_law_thermodynamics('?', '?', 20)
        assert False
    except ValueError:
        pass

def test_entropy():
    # Case 1 ΔS is unknown
    assert entropy(100,50,'?') == 2
    # Case 2 Q is unknown
    assert entropy('?',50,2) == 100
    # Case 3 T is unknown
    assert entropy(100,'?',2) == 50
    # Case 4: Temperature is zero or negative
    try:
        entropy(100, 0, '?')
        assert False
    except ValueError:
        pass
    # Case 5: More than one parameter is unknown
    try:
        entropy('?', '?', 2)
        assert False   
    except ValueError:
        pass

def test_enthalpy():
    # Case 1 H is unknown
    assert enthalpy('?',100,50,2)== 200
    # Case 2 U is unknown
    assert enthalpy(200,'?',50,2)== 100
    # Case 3 P IS unknown
    assert enthalpy(200,100,'?',2)== 50
    # Case 4 V is unknown
    assert enthalpy(200,100,50,'?')== 2
    # Case 5: More than one parameter is unknown
    try:
        enthalpy('?', '?', 50, 2)
        assert False
    except ValueError:
        pass

def test_Gibbs_free_energy():
    # Case1 G is unknown
    assert Gibbs_free_energy('?',100,50,2) ==0
    # Case 2 H is unknown
    assert Gibbs_free_energy(0,'?',50,2)== 100
    # Case 3 T is unknown 
    assert Gibbs_free_energy(0,100,'?',2)== 50
    # Case 4 S is unknown
    assert Gibbs_free_energy(0,100,50,'?')==2
    # Case 5: Temperature is zero or negativete
    try:
        assert Gibbs_free_energy('?',100,0,2)
        assert False
    except ValueError:
        pass
    # Case 6: More than one parameter is unknown
    try:
        assert Gibbs_free_energy('?', '?',50,2)
        assert False
    except ValueError:
        pass

def test_Helmholtz_free_energy():
    # Case 1 A is unknown
    assert Helmholtz_free_energy('?',100,50,2) == 0
    # Case 2 U is unknown
    assert Helmholtz_free_energy(0,'?',50,2) == 100
    #Case 3 T is unknown 
    assert Helmholtz_free_energy(0,100,'?',2)== 50
    # Case 4 S is unknown
    assert Helmholtz_free_energy(0,100,50,'?')==2
    # Case 5: Temperature is zero or negative
    try:
        assert Helmholtz_free_energy('?',100,0,2)
        assert False
    except ValueError:
        pass
    # Case 6: More than one parameter is unknown
    try:
        assert Helmholtz_free_energy('?', '?',50,2)
        assert False
    except ValueError:
        pass

def test_ideal_gas_law():
    # Case 1 P is unknown
    assert ideal_gas_law('?',10,1,300,8.314) == 249.42
    # Case 2 V is unknown
    assert ideal_gas_law(2494.2,'?',1,300,8.314) == 1
    # Case 3 n is unknown
    assert ideal_gas_law(2494.2,10,'?',300,8.314) == 10
    # Case 4 T is unknown
    assert ideal_gas_law(2494.2,10,1,'?',8.314) == 3000
    # Case 5 R is unknown
    assert ideal_gas_law(2494.2,10,1,3000,'?') == 8.314
    # Case 6: More than one parameter is unknown
    try:
        assert ideal_gas_law('?', '?',1,300,8.314)
        assert False
    except ValueError:
        pass


