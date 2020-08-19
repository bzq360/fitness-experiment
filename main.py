import analyze
import setup
import fix
import integrate
from time import perf_counter

# 1. setup resources
setup.copy_resources()

# 2. execute
fix.run_fix_cmds()

# 3. analyze data
analyze.analyze()

# 4. compute average value of data
integrate.compute_average()
