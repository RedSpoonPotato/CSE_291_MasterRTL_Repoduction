import json, os, re, time

def vlg_clean(file):
    file_tmp = file + ".tmp"
    os.system("cp {0} ./{1}".format(file, file_tmp))
    os.remove(file)
    with open(file_tmp, "r") as f:
        lines = f.readlines()
        with open(file, "a+") as f_tmp:
            for line in lines:
                line = re.sub(r'\(\*(.*)\*\)', '', line)
                if line.strip():
                    f_tmp.writelines(line)
    os.remove(file_tmp)

    
if __name__ == '__main__':
    # design_name = "TinyRocket"
    # cmd = 'ast'
    cmd = 'sog'
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

    for design_name in top_modules:
        file_dir = f"../test/verilog/{design_name}_{cmd}.v"
        vlg_clean(file_dir)
    


