### Write test functions here ###
import pytest
from optimize import Optimize

class TestClass():
    def test_known_solution(self):
        f = lambda z: -1;
        df = lambda z: 0;
        alpha = 0;
        beta = 1;
        tolerance = 1e-12; N = 50;
        fixed = Optimize();
        x,z = fixed.fixedpointODE(f,alpha,beta,N, tolerance);
        newt = Optimize();
        xN,zN = newt.newtonODE(f, df, alpha, beta, N, tolerance);

        # Analytical
        ana = lambda x: 0.5*x*(3-x);
        assert pytest.approx(ana(x), abs = tolerance) == z
        assert pytest.approx(ana(xN), abs = tolerance) == zN
