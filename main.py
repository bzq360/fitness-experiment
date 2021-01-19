import analyze
import setup
import fix
import integrate
from time import perf_counter

# 0. setup resources (comment it if keep resource the same)
# setup.copy_resources()

# 1. execute
fix.run_fix_cmds()

# 2. analyze data
analyze.analyze()

# 3. compute average value of data
integrate.compute_average()
