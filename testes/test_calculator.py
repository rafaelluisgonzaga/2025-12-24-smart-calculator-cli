from app.calculator import calcular

def test_calcular():
    r = calcular(10, 5)
    assert r["soma"] == 15
    assert r["subtracao"] == 5
    assert r["multiplicacao"] == 50
    assert r["divisao"] == 2

