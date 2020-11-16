# Test cases here
import pytest
import numpy as np
from ode import ODE_Solver


class TestClass():
    def test_known_solution(self):
        x0 = 1.0;
        T = 2.0;
        lambda_ = -5;


        # not impressive tolerance lol
        tolerance = 1e-3; N = 100000; n = 1;
        solve = ODE_Solver(lambda_,x0, T, N,n);
        t,y = solve.explicit_euler();
        t1,y1 = solve.implicit_eluer();

        # Analytical
        ana = lambda t: x0*np.exp(lambda_*t);
        assert pytest.approx(ana(t), abs = tolerance) == y;
        assert pytest.approx(ana(t1), abs = tolerance) == y1;
