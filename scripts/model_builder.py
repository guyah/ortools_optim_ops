# -*- coding: utf-8 -*-
"""Build an OR model."""

from ortools.linear_solver import pywraplp
from utils import export_model_from_solver

solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, "x")
z = solver.NumVar(0.0, infinity, "z")

# adding constraints
c1 = solver.Add(x - z <= 5)
c2 = solver.Add(x + z <= 9)

# Export model
export_model_from_solver(solver, "test_or_proto.txt")
