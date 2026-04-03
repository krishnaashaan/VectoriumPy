from vectoriumPy.Optics import  mirror_formula,lens_formula

def test_mirror_formula():
    assert mirror_formula('?',10,10) == 5
    assert mirror_formula(5,10,'?') ==10
    assert mirror_formula(5,'?',10)==10
    try:
        mirror_formula("?","?",10)
        assert False
    except ValueError:
      assert True
       
def test_lens_formula():
    assert lens_formula("?",10,20) == 20
    assert lens_formula(20,"?",10) == 20
    assert lens_formula(20,10,"?") == 20

    try:
        lens_formula("?","?",10)
        assert False
    except ValueError:
        assert True

