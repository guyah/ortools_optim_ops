# -*- coding: utf-8 -*-
"""Read an OR model."""
from ortools.linear_solver import linear_solver_pb2, pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

# Read the model from file
model_file = "models_mps/test_or.proto"

# Load the model into the solver
with open(model_file, "rb") as f:
    proto = f.read()
    model = linear_solver_pb2.MPModelProto()

    model.FromString(proto)

    solver.LoadModelFromProto(model)

    infinity = solver.infinity()

    x = solver.IntVar(0.0, infinity, "x")
    z = solver.NumVar(0.0, infinity, "z")

    solver.Maximize(3 * x + 2 * z)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("\n\nSolution:")
        print("Objective value =", solver.Objective().Value())
