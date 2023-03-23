# -*- coding: utf-8 -*-
"""Build an OR model."""
import os

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()
# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, "x")
z = solver.NumVar(0.0, infinity, "z")

c1 = solver.Add(x - z <= 5)
c2 = solver.Add(x + z <= 9)

solver.Maximize(3 * x + 2 * z)

# options = pywraplp.ModelExportOptions()
str1 = solver.ExportModelAsLpFormat(False)
str2 = solver.ExportModelAsMpsFormat(True, False)

# set the directory path
directory = "models_mps"

# create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# specify the file path within the directory
model_file = os.path.join(directory, "test_or.mps")

with open(model_file, "w") as f_:
    f_.write(str2)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("\n\nSolution:")
    print("Objective value =", solver.Objective().Value())
    print("x =", x.solution_value())
    print("z =", z.solution_value())
    print("c1 dual =", c1.dual_value())
    print("c2 dual =", c2.dual_value())
else:
    print("The problem does not have an optimal solution.")
