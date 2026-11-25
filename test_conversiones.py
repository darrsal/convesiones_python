import pytest
import Conversion as con

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == 2
    assert con.pulgadasAcentímetros(2) == 5.08
