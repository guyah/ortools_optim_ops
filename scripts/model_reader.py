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
    print(vars(model))
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("\n\nSolution:")
        print("Objective value =", solver.Objective().Value())
        # print("x =", x.solution_value())
        # print("z =", z.solution_value())
        # print("c1 dual =", c1.dual_value())
        # print("c2 dual =", c2.dual_value())
    else:
        print("The problem does not have an optimal solution.")


# # Define new variables and constraints
# x = solver.NumVar(0.0, solver.infinity(), "x")
# y = solver.NumVar(0.0, solver.infinity(), "y")
# c1 = solver.Add(x + y <= 10)
# c2 = solver.Add(2 * x + y >= 8)

# # Set the objective function
# solver.Maximize(3 * x + 4 * y)

# # Solve the problem
# status = solver.Solve()

# # Print the solution
# if status == pywraplp.Solver.OPTIMAL:
#     print("Solution:")
#     print("Objective value =", solver.Objective().Value())
#     print("x =", x.solution_value())
#     print("y =", y.solution_value())
#     print("c1 dual =", c1.dual_value())
#     print("c2 dual =", c2.dual_value())
# else:
#     print("The problem does not have an optimal solution.")
