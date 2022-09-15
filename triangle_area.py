# Created by    : magngul@math.uio.no
# Created date  : 11. sep 2022
# Course        : UiO IN1900
# Excercise     : 4.4 triangle_area.py
# ---------------------------------------------------------------------------
# Defines function tbat calculates area of triangle
# ---------------------------------------------------------------------------

def triangle_area(vertices):
    """Returns float with area of triangle. Input is nested list with 3 vertices."""
    #Unpack vertices into x & y coordinates
    x1, x2, x3 = vertices[0][0], vertices[1][0], vertices[2][0]
    y1, y2, y3 = vertices[0][1], vertices[1][1], vertices[2][1]

    #Calcualte area
    A = 0.5*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A


def test_triangle_area():
    """Verify the area of a triangle with vertices (0,0), (1,0), and (0,2)."""
    v1 = [0,0];  v2 = [1,0];  v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

"""
Example:
>>>pytest triangle_area.py
============================= test session starts ==============================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/IN1900
collected 1 item

triangle_area.py .                                                       [100%]

============================== 1 passed in 0.01s ===============================
"""
