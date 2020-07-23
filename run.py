import execute
import analyze_each_run
import integrate_analysis


if __name__ == '__main__':
    execute.exec_all_fix()
    analyze_each_run.analyze()
    integrate_analysis.compute_average()