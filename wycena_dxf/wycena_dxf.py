# -*- coding: utf-8 -*-

import ezdxf
from math import sqrt, pi

def calculate_perimeter(entity):
    """
    Funkcja oblicza obw�d dla r�nych typ�w geometrii.
    """
    if entity.dxftype() == 'LINE':
        return entity.length
    elif entity.dxftype() == 'CIRCLE':
        return 2 * pi * entity.dxf.radius
    elif entity.dxftype() == 'ARC':
        return 2 * pi * entity.dxf.radius  # Przyk�adowe obliczenie dla �uk�w pe�nych
    elif entity.dxftype() == 'LWPOLYLINE':
        return calculate_lwpolyline_length(entity)
    elif entity.dxftype() == 'SPLINE':
        return "Nieobs�ugiwane"
    else:
        return "Nieznany kszta�t"

def calculate_area(entity):
    """
    Funkcja oblicza pole dla r�nych typ�w geometrii.
    """
    if entity.dxftype() == 'CIRCLE':
        return pi * entity.dxf.radius**2
    elif entity.dxftype() == 'LWPOLYLINE':
        if hasattr(entity, 'get_points'):
            points = entity.get_points()
            area = 0.0
            for i in range(len(points) - 1):
                x1, y1 = points[i][:2]
                x2, y2 = points[i + 1][:2]
                area += (x2 - x1) * (y1 + y2) / 2.0
            return abs(area)
        else:
            return "B��d: brakuje punkt�w"
    elif entity.dxftype() == 'SPLINE':
        return "Nieobs�ugiwane"
    else:
        return "Nieznany kszta�t"

def calculate_lwpolyline_length(lwpolyline):
    """
    Funkcja oblicza d�ugo�� wieloboku.
    """
    length = 0.0
    points = lwpolyline.get_points()
    for i in range(len(points) - 1):
        x1, y1 = points[i][:2]
        x2, y2 = points[i + 1][:2]
        segment_length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        length += round(segment_length, 1)
    if lwpolyline.closed:
        x1, y1 = points[-1][:2]
        x2, y2 = points[0][:2]
        segment_length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        length += round(segment_length, 1)
    return length

def analyze_dxf(file_path):
    """
    Funkcja analizuje plik DXF i oblicza obw�d i pole dla r�nych typ�w geometrii.
    """
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    total_perimeter = 0.0
    total_area = 0.0

    for entity in msp.query('*'):
        perimeter = calculate_perimeter(entity)
        if perimeter != "Nieobs�ugiwane":
            total_perimeter += perimeter
        area = calculate_area(entity)
        if area != "Nieobs�ugiwane" and area != "B��d: brakuje punkt�w":
            total_area += area

    return total_perimeter, total_area
