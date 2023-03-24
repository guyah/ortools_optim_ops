# -*- coding: utf-8 -*-
"""Build an OR model."""
import os

from ortools.linear_solver import linear_solver_pb2, pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, "x")
z = solver.NumVar(0.0, infinity, "z")

# adding constraints
c1 = solver.Add(x - z <= 5)
c2 = solver.Add(x + z <= 9)

# Prepare model to export using protobuf
model = linear_solver_pb2.MPModelProto()
solver.ExportModelToProto(model)


# set the directory path
directory = "models"

# create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# specify the file path within the directory
model_file_text_proto = os.path.join(directory, "test_or_proto.txt")

with open(model_file_text_proto, "w") as f_:
    f_.write(str(model))
