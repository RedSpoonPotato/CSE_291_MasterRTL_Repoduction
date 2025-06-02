import os, time, json
from multiprocessing import Pool


def convert_one_design(design, cmd, output_dir):
    # bench_path = f"../example/verilog/"
    bench_path = f"../test/verilog/"
    design_dir = bench_path + design + '_' + cmd + '.v'
    print('Current Design: ', design)
    print('Current CMD: ', cmd)
    os.system(f'python3 analyze.py {design_dir} -N {design} -C {cmd} -O {output_dir}')

    

if __name__ == '__main__':

    # design_name = "TinyRocket"
    top_modules = [
    # "s13207",
    # "s5378",
    # "s38584",
    # "s35932",
    # "s38417",
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
    
    # cmd = 'ast' ## for word-level
    for design_name in top_modules:
        cmd = 'sog' ## for bit-level
        output_dir = f'../example/{cmd}/'
        convert_one_design(design_name, cmd, output_dir)


