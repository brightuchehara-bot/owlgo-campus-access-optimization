"""
OwlGo Optimization Model
Campus access optimization using Google OR-Tools
"""

from ortools.linear_solver import pywraplp

def build_model():
    solver = pywraplp.Solver.CreateSolver("SCIP")
    return solver

if __name__ == "__main__":
    solver = build_model()
    print("Optimization model initialized.")
