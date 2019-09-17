import json
from library import ordenar

def test_case1():
    fixture = json.load(open("fixture/case1.json", "r"))
    sort_direction = json.load(open("case1.json", "r"))
    result = ordenar(sort_direction)
    assert fixture == result

def test_case2():
    fixture = json.load(open("fixture/case2.json", "r"))
    sort_direction = json.load(open("case2.json", "r"))
    result = ordenar(sort_direction)
    assert fixture == result

def test_case3():
    fixture = json.load(open("fixture/case3.json", "r"))
    sort_direction = json.load(open("case3.json", "r"))
    result = ordenar(sort_direction)
    assert fixture == result

def test_case4():
    result = ordenar(None)
    assert result == "Ordering Exception"

def test_case5():
    sort_direction = json.load(open("case5.json", "r"))
    result = ordenar(sort_direction)
    assert result == []
