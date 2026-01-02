# OwlGo – Optimizing Class Access

## Overview
OwlGo is a data-driven optimization project developed at Kennesaw State University to reduce excessive travel time between parking, classrooms, and departmental buildings using applied operations research and Python-based analytics.

Students and faculty frequently experienced 10–12 minute walks between classes and parking, reducing instructional time and operational efficiency. OwlGo models campus movement as a constrained, multidimensional assignment problem to minimize total travel time while respecting real-world constraints.

## Problem Definition
- Long walking distances between classes and parking
- Inefficient classroom and parking assignments
- Congestion during peak class times

## Technical Approach
- Modeled the problem as a multidimensional assignment and optimization problem
- Built a Python-based optimization model using Google OR-Tools
- Defined decision variables, objective functions, and constraints related to:
  - Classroom capacity
  - Course schedules
  - Departmental proximity
  - Parking availability
  - Infrastructure limitations

## Data Pipeline
- Input data structured in Excel
- Processed and transformed using Python
- Scenario testing performed through parameterized optimization runs

## Results
- Reduced average parking-to-class travel time from 10–12 minutes to under 5 minutes
- Reduced travel time between major-related classes to under 2 minutes
- Identified pedestrian bottlenecks and proposed data-backed infrastructure improvements (e.g., staircase from Lot 51)

## Tech Stack
- Python
- Google OR-Tools
- pandas, numpy
- Excel (data modeling)

## Notes
Data used in this repository is anonymized and/or simulated for demonstration purposes.

