# -*- coding: utf-8 -*-
"""Read an OR model."""

import os

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")
infinity = solver.infinity()

# Read the MPS file.
directory = "models_mps"
model_file = os.path.join(directory, "test_or.mps")
solver.ReadMps(model_file, True)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("\n\nSolution:")
    print("Objective value =", solver.Objective().Value())
    for variable in solver.variables():
        print(f"{variable.name()} = {variable.solution_value()}")
else:
    print("The problem does not have an optimal solution.")
