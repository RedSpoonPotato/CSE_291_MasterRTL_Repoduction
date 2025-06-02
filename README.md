An attempted reproduction of the MasterRTL paper. Repo of orignal paper: https://github.com/hkust-zhiyao/MasterRTL

Issues I am facing:

(1): Can't locate all the opensourced data mentioned in the paper. Can only find:

ISCAS'89 (s13207, s5378, s38584, s35932, s38417): https://github.com/santoshsmalagi/Benchmarks/tree/main
ITC'99 (b10-b22): https://github.com/ccsl-uaegean/ITC99-RTL-Verilog
(2): Following Steps layed out on original repo (look to original repo README as a guide):

step 1: using run.py to generate sog verilog representations fails on the ISCAS versions, leaving only the ITC files remaining
step 2: using modified auto_run.py from the original repo does work although the runtime for certain files, such as b17 and b19, are very long (> 30 min)
auto_run.py attempts to convert sog verilog representation into python graph version of sog --- have not tested beyond getting stuck at step 2-----
step 3:
preproc/timing/delay_propogation.py should work
tr_propogate.py requires modification of the design_hier.json file to run.
requires specifiying module hierarchy in original verilog implemtation
See the MasterRTL/example/verilog/TinyRocket/chipyard.TestHarness.TinyRocketConfig.top.v as an example
later steps: not fully implemented
