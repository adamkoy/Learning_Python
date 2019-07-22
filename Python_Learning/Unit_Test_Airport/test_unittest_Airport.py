from HW_Airports import *
from HW_Aircrafts import *
from HW_People import *

import pytest


# Test if all instance variables passed are correct for Airplane:

def test_get_airplane_num_passengers():
    assert (airplane1.num_passengers)
    return "300"

def test_get_airplane_airline():
    assert (airplane1.brand)
    return "Easy Jet"


def test_get_airplane_company():
    assert (airplane1.brand), "RR"

# # Wrong situation to use this assert function
# def test_correct_gender():
#     if Dani.gender != "M " or "F":
#         raise ValueError('gender has an error')
#     return True
#

def test_passenger_name():
    assert Dani.firstname == "Dani "

def test_staff_id():
    assert staff1.id,"01"

def test_Dani_details():
    assert Dani.get_details() == "Dani ,pegg ,4/1/1987,M,GB,01"








