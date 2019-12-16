from puzzle import phases
import pytest

def test_phase1():
    ref = [int(x) for x in '24176176']
    sequence =  [int(x) for x in '80871224585914546619083218645595']

    res = phases(sequence)[:8]
    assert res == ref
