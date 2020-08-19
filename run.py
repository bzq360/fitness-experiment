import analyze
import setup
import fix
import integrate_analysis
from time import perf_counter

# 1. setup resources
setup.copy_resources()
# 2. execute
t1_start = perf_counter()
fix.run_fix_cmds()
t1_stop = perf_counter()
print("Time elapsed: ", t1_stop - t1_start)
# 3. analyze data
analyze.analyze()
# TODO: Merge this integrate into analyze
integrate_analysis.compute_average()
