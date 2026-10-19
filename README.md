# Practical Work 2: Unit and Mutation Testing

## Overview
This module demonstrates practical skills in unit testing and mutation testing methodologies. Four Python modules were developed, each containing a deliberately injected defect. Cross-testing was performed by teammates to identify, report, and fix these defects, followed by rigorous mutation analysis using MutPy to validate the effectiveness of the test suite.

## Objectives
- Develop Python modules adhering to PEP 8 standards
- Design unit tests using pytest to achieve high statement and branch coverage
- Identify and document defects via formal bug reports
- Apply mutation testing using MutPy to evaluate and improve test suite quality
- Achieve 100% mutation score through iterative test improvement

## Tech Stack
- Language: Python 3.11
- Testing Framework: pytest 7.4
- Mutation Testing: MutPy 0.6.1
- Coverage Analysis: coverage.py 7.3
- IDE: PyCharm

## Modules
1. **TaskManager** (Nikishin M.A.) - Task list management with add, complete, filter, and clear operations
2. **BankAccount** (Kashayev P.A.) - Banking operations simulator with deposit, withdraw, and transfer
3. **Library** (Podlesny S.V.) - Book lending system with availability tracking
4. **Gradebook** (Dolgov R.A.) - Student grade journal with statistics calculation

## Key Achievements
- Achieved 100% Statement Coverage across all modules after defect resolution
- Improved Mutation Score from approximately 72% to 100%
- Successfully identified and fixed 4 injected defects:
  1. Gradebook: ZeroDivisionError when calculating average for a student with no grades
  2. BankAccount: Atomicity violation in fund transfers (money created out of thin air)
  3. Library: Data integrity breach allowing return of unborrowed books
  4. TaskManager: Index shift bug when removing consecutive completed tasks during iteration

## How to Run

```bash
# Install dependencies
pip install pytest pytest-cov mutpy

# Run unit tests with coverage
pytest tests/ --cov=src --cov-report=term-missing

# Run mutation testing (example for task_manager)
mutpy --target src.task_manager --unit-test tests.test_task_manager --runner pytest
