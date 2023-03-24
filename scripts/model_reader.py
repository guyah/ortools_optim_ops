# -*- coding: utf-8 -*-
"""Read an OR model."""
from google.protobuf import text_format
from ortools.linear_solver import linear_solver_pb2, pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

# Read the model from file
model_file = "models/test_or_proto.txt"

with open(model_file, "rb") as f:

    ##########################
    ##########################
    # SECTION - Read Old Model
    ##########################
    ##########################

    # read the model proto in txt
    model_proto_txt = f.read()

    # Generate the model placeholder
    old_model_proto = linear_solver_pb2.MPModelProto()
    text_format.Merge(model_proto_txt, old_model_proto)

    # Load the model from the proto
    # model now lives in the solver (changes only appear in the solver)
    # if we need to access the model we need to export it again
    # No changes will be written to old_proto_model
    errors = solver.LoadModelFromProto(old_model_proto)

    #####################################################
    #####################################################
    # SECTION - Adding variables and constraints to model
    #####################################################
    #####################################################

    # Define infinity
    infinity = solver.infinity()

    # x and y are integer non-negative variables.
    a = solver.IntVar(0.0, infinity, "a")
    b = solver.NumVar(0.0, infinity, "b")

    c3 = solver.Add(a - b <= 10)
    c4 = solver.Add(b + a >= 9)

    # The new model will hold old and new variables and constraints
    new_model = linear_solver_pb2.MPModelProto()
    solver.ExportModelToProto(new_model)
    print(new_model)
