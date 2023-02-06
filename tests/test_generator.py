from datetime import datetime
import os

from wodpy import wod
from wodpy.extra import WODFile, WODGenerator

def test_file():
    WOD = WODFile("tests/testData/classic.dat")


def test_iter():
    WOD = WODGenerator("tests/testData/classic.dat")
    profiles = [p for p in WOD]
    assert len(profiles) == 2


def test_map():
    WOD = WODGenerator("tests/testData/classic.dat")
    uids = [p for p in WOD.map(lambda x: x.uid())]
    assert uids == [67064, 15556443]


def test_pmap():
    try:
        import loky
    except:
        # No fallback alternative for loky at this point
        return
    WOD = WODGenerator("tests/testData/classic.dat")
    uids = [p for p in WOD.pmap(lambda x: x.uid())]
    assert uids == [67064, 15556443]
