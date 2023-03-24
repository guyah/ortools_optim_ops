# -*- coding: utf-8 -*-
"""Model helper functions."""
import os

from ortools.linear_solver import linear_solver_pb2


def export_model_from_solver(solver, output_model_name):
    """Export the linear solver model to a protobuf file.

    Args:
        solver: The linear solver instance.
        output_model_name: The name of the output model file.
    
    Returns:
        None
    """
    # Prepare model to export using protobuf
    model = linear_solver_pb2.MPModelProto()
    solver.ExportModelToProto(model)

    # set the directory path
    directory = "models"

    # create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # specify the file path within the directory
    model_file_text_proto = os.path.join(directory, output_model_name)

    with open(model_file_text_proto, "w") as f_:
        f_.write(str(model))
