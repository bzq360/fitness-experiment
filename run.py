import execute
import analyze_each_run
import integrate_analysis
from time import perf_counter


if __name__ == '__main__':
    t1_start = perf_counter()
    execute.exec_all_fix()
    t1_stop = perf_counter()
    print("Time elapsed: ", t1_stop - t1_start)
    analyze_each_run.analyze()
    integrate_analysis.compute_average()