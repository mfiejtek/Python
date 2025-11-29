import pytest
from points import Point
from rectangles import Rectangle

# --- Fixtury (opcjonalne, ale ułatwiają testy) ---
@pytest.fixture
def rect_unit():
    """Zwraca prostokąt [0, 0] -> [1, 1]"""
    return Rectangle(0, 0, 1, 1)

@pytest.fixture
def rect_large():
    """Zwraca prostokąt [0, 0] -> [10, 20]"""
    return Rectangle(0, 0, 10, 20)

def test_init_valid():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.pt1 == Point(0, 0)
    assert rect.pt2 == Point(4, 3)

def test_init_invalid_coordinates():
    with pytest.raises(ValueError, match="musi być większe"):
        Rectangle(5, 0, 5, 10)
    
    with pytest.raises(ValueError, match="musi być większe"):
        Rectangle(0, 5, 10, 4)

def test_from_points():
    p1 = Point(1, 1)
    p2 = Point(5, 5)
    
    rect = Rectangle.from_points((p1, p2))
    assert rect == Rectangle(1, 1, 5, 5)
    
    rect_list = Rectangle.from_points([p1, p2])
    assert rect_list == Rectangle(1, 1, 5, 5)

def test_from_points_invalid_input():
    p1 = Point(1, 1)
    with pytest.raises(ValueError):
        Rectangle.from_points((p1,)) # Za mało punktów


def test_str(rect_unit):
    assert str(rect_unit) == "[(0, 0), (1, 1)]"

def test_repr(rect_unit):
    assert repr(rect_unit) == "Rectangle(0, 0, 1, 1)"

def test_eq(rect_unit):
    r1 = Rectangle(0, 0, 1, 1)
    r2 = Rectangle(0, 0, 1, 1)
    r3 = Rectangle(1, 1, 2, 2)
    assert r1 == r2
    assert r1 == rect_unit
    assert r1 != r3


def test_dimensions_properties(rect_large):
    assert rect_large.width == 10
    assert rect_large.height == 20

def test_coordinates_properties(rect_large):
    assert rect_large.left == 0
    assert rect_large.right == 10
    assert rect_large.bottom == 0
    assert rect_large.top == 20

def test_points_properties(rect_large):
    assert rect_large.topleft == Point(0, 20)
    assert rect_large.bottomleft == Point(0, 0)
    assert rect_large.topright == Point(10, 20)
    assert rect_large.bottomright == Point(10, 0)

def test_center_property(rect_large):
    c = rect_large.center
    assert isinstance(c, Point)
    assert c == Point(5, 10)


def test_area(rect_large):
    assert rect_large.area() == 200

def test_move(rect_unit):
    rect_unit.move(2, 3)
    assert rect_unit == Rectangle(2, 3, 3, 4)
    assert rect_unit.width == 1
    assert rect_unit.height == 1

def test_intersection_overlap():
    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(2, 2, 6, 6)
    inter = r1.intersection(r2)
    assert inter == Rectangle(2, 2, 4, 4)

def test_intersection_disjoint():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(3, 3, 5, 5)
    assert r1.intersection(r2) is None

def test_intersection_touching_edge():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(2, 0, 4, 2)
    assert r1.intersection(r2) is None

def test_intersection_contained():
    outer = Rectangle(0, 0, 10, 10)
    inner = Rectangle(2, 2, 8, 8)
    assert outer.intersection(inner) == inner

def test_cover():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(4, 4, 6, 6)
    cover = r1.cover(r2)
    assert cover == Rectangle(0, 0, 6, 6)

def test_make4():
    r = Rectangle(0, 0, 4, 4)
    parts = r.make4()
    
    assert len(parts) == 4
    
    expected = [
        Rectangle(0, 0, 2, 2),
        Rectangle(2, 0, 4, 2),
        Rectangle(0, 2, 2, 4),
        Rectangle(2, 2, 4, 4)
    ]
    for p_result, p_expect in zip(parts, expected):
        assert p_result == p_expect

def test_method_type_validation():
    r = Rectangle(0,0,1,1)
    with pytest.raises(ValueError):
        r.intersection("not a rectangle")
    
    with pytest.raises(ValueError):
        r.cover("not a rectangle")