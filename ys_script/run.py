import os
verilog_source = [

    "../MasterRTL/Benchmarks/ISCAS89/s13207.v",
    "../MasterRTL/Benchmarks/ISCAS89/s5378.v",
    "../MasterRTL/Benchmarks/ISCAS89/s38584.v",
    "../MasterRTL/Benchmarks/ISCAS89/s35932.v",
    "../MasterRTL/Benchmarks/ISCAS89/s38417.v",

    "../ITC99-RTL-Verilog/b10.v",
    "../ITC99-RTL-Verilog/b11.v",
    "../ITC99-RTL-Verilog/b12.v",
    "../ITC99-RTL-Verilog/b13.v",
    "../ITC99-RTL-Verilog/b14.v",
    "../ITC99-RTL-Verilog/b15.v",
    # "../ITC99-RTL-Verilog/b16.v",
    "../ITC99-RTL-Verilog/b17.v",
    "../ITC99-RTL-Verilog/b18.v",
    "../ITC99-RTL-Verilog/b19.v",
    "../ITC99-RTL-Verilog/b20.v",
    "../ITC99-RTL-Verilog/b21.v",
    "../ITC99-RTL-Verilog/b22.v",
]
top_modules = [
    "s13207",
    "s5378",
    "s38584",
    "s35932",
    "s38417",
    "b10",
    "b11",
    "b12",
    "b13",
    "b14",
    "b15",
    # "b16",
    "b17",
    "b18",
    "b19",
    "b20",
    "b21",
    "b22",
]
output_paths = [
    "../test/verilog/s13207_sog.v",
    "../test/verilog/s5378_sog.v",
    "../test/verilog/s38584_sog.v",
    "../test/verilog/s35932_sog.v",
    "../test/verilog/s38417_sog.v",
    "../test/verilog/b10_sog.v",
    "../test/verilog/b11_sog.v",
    "../test/verilog/b12_sog.v",
    "../test/verilog/b13_sog.v",
    "../test/verilog/b14_sog.v",
    "../test/verilog/b15_sog.v",
    # "../test/verilog/b16_sog.v",
    "../test/verilog/b17_sog.v",
    "../test/verilog/b18_sog.v",
    "../test/verilog/b19_sog.v",
    "../test/verilog/b20_sog.v",
    "../test/verilog/b21_sog.v",
    "../test/verilog/b22_sog.v",
]

for i in range(len(verilog_source)):
    file_list = os.popen(f"ls {verilog_source[i]}").read().split()
    output_path = output_paths[i]
    top = top_modules[i]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(f"run_{i}.ys", "w") as f:
        # f.write("read -verific\n")
        # for vfile in file_list:
        # for vfile in verilog_source:
        f.write(f"read_verilog {verilog_source[i]}\n")
        f.write(f"hierarchy -check -top {top}\n")
        f.write("proc; flatten; opt; fsm; opt; memory; opt;\n")
        f.write("techmap; opt;\n")
        f.write(f"write_verilog {output_path}\n")

    os.system(f"yosys run_{i}.ys")
