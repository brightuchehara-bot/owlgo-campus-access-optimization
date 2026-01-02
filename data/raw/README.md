# OwlGo: Optimizing Campus Class Access

## Overview
OwlGo is a data-driven optimization project developed to reduce excessive walking time between parking, classrooms, and academic buildings using applied operations research and Python-based analytics.

Students and faculty often experience 10–12 minute walks between classes and parking locations, reducing instructional efficiency and campus accessibility. OwlGo models campus movement as a constrained, multidimensional assignment problem, optimizing classroom assignments to minimize total walking time while respecting real-world capacity and scheduling constraints.

## Technical Stack
- Python
- Pandas
- Google OR-Tools
- Jupyter Notebook

## Data Model
- **Courses**: enrollment, department, schedule
- **Classrooms**: capacity, building
- **Distances**: walking time between campus locations

Data is processed through a structured analytics pipeline:

raw → processed → optimization → outputs

## Optimization Approach
- Binary decision variables assign courses to classrooms
- Capacity constraints ensure feasible assignments
- Objective function minimizes total walking time
- Penalty-based handling of infeasible assignments

## Results
- Reduced average parking-to-class travel time from 10–12 minutes to under 5 minutes
- Reduced travel time between major-related courses to under 2 minutes
- Generated data-backed infrastructure recommendations to improve pedestrian flow

## Outputs
- `outputs/optimized_assignments.csv`
- `outputs/summary.txt`

## Extensions
- Parking allocation optimization
- Scenario testing for peak congestion periods
- BI dashboards for decision support

## Author
Bright Uchehara  
Analytics & Optimization Engineering
