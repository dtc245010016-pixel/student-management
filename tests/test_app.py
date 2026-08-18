import pytest
from app import get_students, get_student, search_students

def test_get_students():
    students = get_students()
    assert len(students) > 0

def test_get_student_found():
    student = get_student(1)
    assert student is not None
    assert student["name"] == "Nguyen Van A"

def test_get_student_not_found():
    student = get_student(999)
    assert student is None

def test_search_students():
    result = search_students("Nguyen")
    assert len(result) > 0
    assert result[0]["name"] == "Nguyen Van A"

def test_search_students_case_insensitive():
    result = search_students("nguyen")
    assert len(result) > 0
